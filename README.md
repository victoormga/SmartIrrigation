# 🌱 Smart Irrigation — TFG

Proyecto de **gestión inteligente de riego agrícola**, desarrollado con **Django** y **Django REST Framework (DRF)**.  
El objetivo es construir una API que represente digitalmente un conjunto de **parcelas agrícolas**, sus **sensores IoT** y las **lecturas** que generan (digital twin básico).

---

## 🚀 Estado actual (versión inicial)

### 🔹 Backend (Django + DRF)
- CRUD funcional de **Parcelas** (`/api/parcelas/`)
- CRUD funcional de **Sensores** (`/api/sensores/`)
- API para registrar y consultar **Lecturas** (`/api/lecturas/`)
- Validaciones básicas (`lat`, `lon`, `superficie_ha`)
- Permisos de lectura anónima / escritura autenticada
- Paginación por defecto en DRF
- Base de datos actual: **SQLite** (modo desarrollo)

### 🧩 Próximos pasos (pendientes)
- Migrar a **PostgreSQL** y configurar entorno con **Docker Compose**
- Añadir **autenticación JWT** (SimpleJWT)
- Implementar **reglas y alertas** (umbrales por tipo de sensor)
- Integrar **mapa Leaflet** para visualizar parcelas y sensores
- Añadir **panel de control web** con gráficas (Chart.js o similar)
- Crear **servicio de ingesta** para sensores reales (HTTP/MQTT)
- Desplegar en **Vercel / Railway / Render / VPS**

---

## 🧰 Requisitos

- Python 3.11 o superior  
- pip o pipenv / virtualenv  
- (Opcional) PostgreSQL y Docker (para entorno avanzado)

---

## ⚙️ Instalación rápida (modo desarrollo)

```bash
# 1. Clonar el repositorio
git clone <url-del-repo>
cd smart_irrigation

# 2. Crear y activar entorno virtual
python -m venv .venv
.\.venv\Scripts\activate  # en Windows
# source .venv/bin/activate  # en Linux/Mac

# 3. Instalar dependencias
pip install -r requirements.txt  # o manualmente: django djangorestframework

# 4. Migraciones y superusuario
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# 5. Ejecutar servidor
python manage.py runserver
