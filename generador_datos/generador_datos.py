import csv
import random
import sqlite3
import smtplib
from concurrent.futures import ThreadPoolExecutor
from email.message import EmailMessage
from faker import Faker

# -------------------- MODELOS Y POO --------------------

class Usuario:
    def __init__(self, nombre, correo, edad):
        self.nombre = nombre
        self.correo = correo
        self.edad = edad

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "correo": self.correo,
            "edad": self.edad
        }

# -------------------- GENERADOR --------------------

class GeneradorUsuarios:
    def __init__(self, cantidad):
        self.cantidad = cantidad
        self.faker = Faker()

    def generar(self):
        usuarios = []
        for _ in range(self.cantidad):
            nombre = self.faker.name()
            correo = self.faker.email()
            edad = random.randint(18, 65)
            usuarios.append(Usuario(nombre, correo, edad))
        return usuarios

# -------------------- EXPORTADORES --------------------

class ExportadorCSV:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo

    def exportar(self, usuarios):
        with open(self.ruta_archivo, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['nombre', 'correo', 'edad'])
            writer.writeheader()
            for usuario in usuarios:
                writer.writerow(usuario.to_dict())
        print(f"✅ Datos exportados a CSV en {self.ruta_archivo}")

class AlmacenadorSQLite:
    def __init__(self, db_name='usuarios.db'):
        self.db_name = db_name

    def almacenar(self, usuarios):
        conexion = sqlite3.connect(self.db_name)
        cursor = conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                correo TEXT,
                edad INTEGER
            )
        ''')
        for usuario in usuarios:
            cursor.execute('''
                INSERT INTO usuarios (nombre, correo, edad) VALUES (?, ?, ?)
            ''', (usuario.nombre, usuario.correo, usuario.edad))
        conexion.commit()
        conexion.close()
        print("✅ Datos almacenados en SQLite")

# -------------------- ENVÍO DE CORREO --------------------

def enviar_email(destinatario, archivo_adjunto):
    remitente = 'prueba@mailtrap.io'  # Ficticio, solo para simular
    asunto = 'Usuarios generados CSV'
    cuerpo = 'Adjunto archivo con datos de prueba.'

    msg = EmailMessage()
    msg['Subject'] = asunto
    msg['From'] = remitente
    msg['To'] = destinatario
    msg.set_content(cuerpo)

    with open(archivo_adjunto, 'rb') as f:
        contenido = f.read()
        msg.add_attachment(contenido, maintype='application', subtype='octet-stream', filename=archivo_adjunto)

    # Reemplaza con tus credenciales de Mailtrap
    smtp_host = 'sandbox.smtp.mailtrap.io'
    smtp_port = 587
    smtp_user = '7413b832cdf74c'  # ← pon aquí tu username
    smtp_pass = '395ea1f3fef880'  # ← pon aquí tu password

    with smtplib.SMTP(smtp_host, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(smtp_user, smtp_pass)
        smtp.send_message(msg)
        print("✅ Correo enviado correctamente (simulado con Mailtrap)")

# -------------------- PRINCIPAL --------------------

def proceso_principal(cantidad_usuarios=10):
    generador = GeneradorUsuarios(cantidad_usuarios)
    usuarios = generador.generar()

    exportador = ExportadorCSV('usuarios_generados.csv')
    exportador.exportar(usuarios)

    almacenador = AlmacenadorSQLite()
    almacenador.almacenar(usuarios)

# -------------------- EJECUCIÓN EN PARALELO --------------------

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=2) as executor:
        futuro1 = executor.submit(proceso_principal, 10)
        futuro1.result()

    # Enviar email con archivo CSV (simulado con Mailtrap)
    enviar_email("destinatario@correo.com", "usuarios_generados.csv")
