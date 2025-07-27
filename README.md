# ✈️ Proyecto LATAM – Serenity + Cucumber

Este proyecto consiste en la automatización UI de la funcionalidad de **búsqueda de vuelos** en el sitio web oficial de [LATAM Airlines](https://www.latamairlines.com/co/es), utilizando el framework Serenity BDD con Cucumber.

Forma parte de una prueba técnica donde se solicitó implementar 3 casos de prueba sobre la búsqueda de vuelos, siguiendo principios de arquitectura de automatización, reutilización de datos y buenas prácticas de pruebas automatizadas.

---

## 🧪 Objetivos de la automatización

- Automatizar casos de prueba funcionales en la búsqueda de vuelos.
- Aplicar principios de diseño BDD (Behavior Driven Development).
- Utilizar datos previamente generados como entrada a las pruebas.
- Implementar un framework estructurado y escalable con Serenity.

---

## 🛠️ Tecnologías utilizadas

| Herramienta       | Descripción                                |
|-------------------|--------------------------------------------|
| Java 11           | Lenguaje principal                         |
| Maven             | Gestión de dependencias y construcción     |
| Serenity BDD      | Framework de automatización + reportes     |
| Cucumber          | Definición de escenarios en Gherkin        |
| Selenium WebDriver| Automatización de navegador web            |
| GitHub            | Repositorio de código y colaboración       |

---

## 📂 Estructura del pr
latam-serenity/
│
├── src/
│ └── test/
│ ├── java/
│ │ └── com.latam.test/
│ │ ├── runners/ # Clase Runner de ejecución
│ │ ├── stepdefinitions/ # Definiciones de pasos Cucumber
│ │ └── tasks / questions / ... # Clases auxiliares de Serenity
│ └── resources/
│ └── features/
│ └── busqueda_vuelos.feature # Escenarios en Gherkin
│
├── pom.xml # Configuración de dependencias y plugins
├── serenity.properties # Configuración del proyecto Serenity
└── README.md # Documentación general del proyecto
## ✅ Casos de prueba implementados

1. **Búsqueda de vuelo solo ida con origen y destino válidos**
2. **Búsqueda de vuelo ida y regreso en fechas futuras**
3. **Validación de mensaje cuando los campos requeridos están vacíos**

Los escenarios están definidos en el archivo `busqueda_vuelos.feature` utilizando el lenguaje Gherkin.

---

## ▶️ Cómo ejecutar el proyecto

### 🔧 Pre-requisitos

- Java 11 instalado y configurado (`JAVA_HOME`)
- Maven instalado (`mvn -v`)
- Google Chrome instalado
- Clonar el repositorio: git clone https://github.com/Ing-Jhon-Urquijo/latam-serenity.git
cd latam-serenity
- Ejecutar: mvn clean verify
