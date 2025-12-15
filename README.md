📦 Sistema de Gestión de Órdenes de Compra, Facturación y Envíos

Proyecto desarrollado como Examen Final / Proyecto Semestral, cuyo objetivo es implementar un sistema fullstack que permita gestionar el flujo completo de ventas, desde la creación de órdenes hasta el despacho de productos, integrando control de versiones y automatización CI/CD.

📌 Información General

Alumnos: Marco Parra Luis Inostroza 

Institución: Duoc UC

Asignatura: Programación / Ingeniería de Software

Año: 2025

Repositorio: GitHub (público)

🎯 Objetivo del Proyecto

Desarrollar una aplicación web que permita:

Registrar usuarios y autenticar acceso

Gestionar órdenes de compra

Emitir facturas automáticamente

Registrar envíos asociados a facturas

Integrar un pipeline CI/CD usando GitHub Actions

🧩 Arquitectura del Sistema

El proyecto utiliza una arquitectura cliente-servidor, separando claramente frontend y backend:

Backend

Lenguaje: Python

Framework: Flask

Base de datos: MySQL

Tipo: API REST

Frontend

Framework: React

Consumo de API: Fetch (HTTP)

DevOps

Repositorio: GitHub

CI/CD: GitHub Actions

📁 Estructura del Proyecto
Prueba2Github/
│
├── backend/
│   └── src/
│       ├── app.py
│       ├── database.py
│       ├── login.py
│       ├── orden_compra.py
│       ├── factura.py
│       └── envio.py
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Login.js
│   │   │   ├── Menu.js
│   │   │   ├── Ordenes.js
│   │   │   ├── Facturas.js
│   │   │   └── Envios.js
│   │   └── App.js
│   └── package.json
│
├── .github/workflows/
│   └── pipeline.yml
│
└── README.md

🔐 Requerimientos Funcionales (Rúbrica)
RF1 – Registro de Órdenes de Compra

Permite crear y listar órdenes de compra

Se almacenan en base de datos MySQL

Estado inicial: pendiente

RF2 – Login de Usuarios

Autenticación mediante usuario y contraseña

Validación directa contra la base de datos

Acceso restringido al sistema

RF3 – Menú Principal

Navegación entre módulos:

Órdenes

Facturas

Envíos

RF4 – Emisión de Facturas

Se emite factura asociada a una orden

Cálculo automático de IVA (19%)

Actualiza estado de la orden a facturada

RF5 – Envío de Productos

Registro de envíos asociados a facturas

Validación de integridad referencial

Visualización de envíos registrados

RF6 – Integración CI/CD

Pipeline configurado con GitHub Actions

Se ejecuta automáticamente al hacer push

Valida la estructura del proyecto

🧪 Flujo del Sistema

El usuario inicia sesión

Registra una orden de compra

La orden es facturada

Se genera el envío asociado

Los datos se almacenan en la base de datos

Los cambios se validan con CI/CD

▶️ Ejecución del Proyecto
Backend
cd backend/src
python app.py


Servidor disponible en:

http://localhost:5000

Frontend
cd frontend
npm install
npm start


Aplicación disponible en:

http://localhost:3000

🗄️ Base de Datos

Base de datos utilizada: MySQL

Tablas principales:

usuarios

ordenes_compra

facturas

envios

Relaciones:

Una orden puede tener una factura

Una factura puede tener un envío

🚀 Pipeline CI/CD

El proyecto incluye un pipeline configurado en:

.github/workflows/pipeline.yml


Funciones del pipeline:

Se ejecuta automáticamente con cada push

Garantiza consistencia del repositorio

Cumple con el requerimiento RF6

📸 Evidencias

Durante el desarrollo se obtuvieron evidencias de:

Login funcional

Órdenes creadas y listadas

Facturas emitidas correctamente

Envíos registrados

Pipeline ejecutado exitosamente

✅ Conclusión

Este proyecto cumple con todos los requisitos establecidos en la rúbrica del examen final, demostrando:

Desarrollo fullstack

Integración frontend y backend

Persistencia en base de datos

Automatización con CI/CD

Buen uso de Git y GitHub

🧠 Autor
Luis Inostroza
Marco Parra
Duoc UC – 2025
