🧾 Sistema de Gestión de Órdenes de Compra, Facturación y Envíos

Proyecto desarrollado para cumplir los requerimientos del Proyecto Semestral Parcial 3, correspondiente a la asignatura de Ingeniería de Software / Programación. Incluye un sistema completo que permite gestionar órdenes de compra, emitir facturas y registrar el despacho de productos, utilizando Python, MySQL y GitHub Actions.

🎯 Objetivo del Proyecto

Desarrollar un sistema funcional que permita gestionar el ciclo completo de una compra, desde su ingreso como orden hasta la generación de una factura y su posterior despacho. Además, integrar un flujo profesional de desarrollo utilizando GitFlow y automatización continua mediante un pipeline CI/CD.

🧩 Requerimientos Funcionales Implementados ✔ RF1 – Gestión de Órdenes de Compra

Crear nuevas órdenes

Listar órdenes

Cambiar estado

✔ RF2 – Inicio de Sesión

Validación de credenciales desde la tabla usuarios

✔ RF3 – Menú Principal

Navegación completa del sistema vía consola

✔ RF4 – Facturación

Emisión de factura

Cálculo automático de IVA

Cambio de estado de la orden

Registro en la tabla facturas

✔ RF5 – Envíos

Registrar envío asociado a factura

Guardar comentario de despacho

Registrar fecha

Insertar en la tabla envios

✔ RF6 – Pipeline CI/CD

GitHub Actions configurado para ejecutar:

Instalación de dependencias

Revisión de integridad

Simulación de build

Simulación de deploy

Notificación de éxito

🏗️ Arquitectura del Sistema

Tecnologías utilizadas:

Python 3.11

MySQL (Laragon)

Git & GitHub

GitHub Actions (CI/CD)

Patrón utilizado: Modular por funcionalidades

orden_compra.py

factura.py

envio.py

login.py

database.py

menu.py

📁 Estructura del Proyecto Prueba2Github/ │ ├── src/ │ ├── app.py │ ├── database.py │ ├── login.py │ ├── menu.py │ ├── factura.py │ ├── orden_compra.py │ ├── envio.py │ └── init.py │ ├── .github/ │ └── workflows/ │ └── pipeline.yml │ ├── evidencias/ │ ├── rf4_factura.png │ ├── rf4_factura_bd.png │ ├── rf5_envio.png │ ├── rf5_envio_bd.png │ ├── pipeline_success.png │ ├── pipeline_logs.png │ ├── ramas.png │ └── kanban.png │ ├── README.md └── requirements.txt

🗄️ Base de Datos utilizada (MySQL)

Tablas:

🧑‍💼 usuarios id, usuario, password

📦 ordenes_compra id, producto, precio, cantidad, estado

🧾 facturas id, orden_id, iva, total, fecha, estado

📮 envios id, factura_id, comentario, fecha

🔀 Flujo de Trabajo Git (GitFlow)

Se utilizaron las siguientes ramas:

main → versión estable

dev → integración de funcionalidades

qa → pruebas finales

feature/* → desarrollo de cada requerimiento

Flujo de merges:

feature → dev → qa → main

🔧 Pipeline CI/CD (GitHub Actions)

El archivo se encuentra en:

.github/workflows/pipeline.yml

Incluye:

Instalación de dependencias (Flask, PyMySQL)

Simulación de build

Simulación de deploy

Notificación final

Trigger en:

Push a main o dev

Pull request a main

🖥️ Instrucciones de Instalación 1️⃣ Clonar el repositorio git clone https://github.com/Kito189/Prueba2Github.git cd Prueba2Github

2️⃣ Crear entorno virtual (opcional) python -m venv .venv

3️⃣ Activar entorno

Windows:

.venv\Scripts\activate

4️⃣ Instalar dependencias pip install flask pymysql flask-mysqldb flask-cors

5️⃣ Configurar base de datos

Importar el archivo SQL o crear las tablas manualmente.

6️⃣ Ejecutar el sistema python src/menu.py

🧪 Evidencias del Proyecto

Las evidencias se encuentran en la carpeta /evidencias/:

Factura generada

BD facturas

Envío registrado

BD envíos

Pipeline SUCCESS

Logs del pipeline

Flujo de ramas

Merges

Kanban

🙌 Autor

Luis Inostroza Marco Parra Estudiantes de Ingeniería en Informática – DUOC UC Proyecto desarrollado con fines académicos.
