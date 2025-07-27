# 🧠 Generador de Datos Ficticios - Python

Este proyecto genera datos ficticios simulando un entorno real para ser usados en pruebas, automatización o entrenamiento de modelos. Aplica los pilares de la programación orientada a objetos, principios SOLID, patrones de diseño, almacenamiento local en SQLite, exportación a CSV, envío de correo electrónico y ejecución en paralelo.

## 🚀 Características

- Generación de datos ficticios (nombres, emails, teléfonos, etc.)
- Uso de Programación Orientada a Objetos (POO)
- Aplicación de principios **SOLID**
- Persistencia en base de datos **SQLite**
- Exportación de resultados a **CSV**
- Envío del archivo generado por **correo electrónico**
- Soporte para ejecución en **paralelo** (multi-threading)

## 🛠 Tecnologías

- **Python 3.10+**
- SQLite (módulo `sqlite3`)
- CSV (`csv`)
- Envío de correos (`smtplib`, `email`)
- Concurrencia (`threading`)
- Buenas prácticas de arquitectura y código limpio

---

## 📦 Estructura del proyecto
generador_datos/
│
├── db_manager.py # Conexión y operaciones con SQLite
├── data_generator.py # Generación de datos con Faker
├── exporter.py # Exportación de datos a CSV
├── mailer.py # Envío de archivo CSV por correo
├── thread_manager.py # Ejecución paralela de generación
├── main.py # Orquestador del sistema
├── utils.py # Utilidades compartidas
├── config.json # Configuración externa (correo, threads, etc.)
└── requirements.txt # Dependencias del proyecto

Clonar el repositorio
bash
git clone https://github.com/Ing-Jhon-Urquijo/generador-datos-jhon.git
cd generador-datos-jhon

Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

Instalar dependencias
pip install -r requirements.txt

Configurar archivo config.json
Edita el archivo config.json para ajustar parámetros como:

Cantidad de datos a generar

Hilos a utilizar

Datos del correo de envío (servidor SMTP, email y contraseña)
{
  "num_registros": 100,
  "threads": 4,
  "email": {
    "from": "tucorreo@gmail.com",
    "password": "tu_clave",
    "to": "destinatario@gmail.com",
    "smtp_server": "smtp.gmail.com",
    "port": 587
  }
}

Ejecutar el programa
python main.py
