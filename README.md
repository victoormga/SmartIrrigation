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
.\.venv\Scriptsctivate  # en Windows
# source .venv/bin/activate  # en Linux/Mac

# 3. Instalar dependencias
pip install -r requirements.txt  # o manualmente: django djangorestframework

# 4. Migraciones y superusuario
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# 5. Ejecutar servidor
python manage.py runserver
```

Accede en:  
➡️ http://localhost:8000/admin/ — panel de administración  
➡️ http://localhost:8000/api/parcelas/ — API REST

---

## 🧪 Pruebas rápidas de API

En **PowerShell**:

```powershell
# Crear una parcela
$body = @{
  nombre="Parcela Norte"
  cultivo="Olivo"
  superficie_ha=2.5
  lat=37.389092
  lon=-5.984459
  descripcion="Zona ligeramente inclinada"
} | ConvertTo-Json

Invoke-RestMethod -Method Post -Uri "http://localhost:8000/api/parcelas/" -Headers @{ "Content-Type" = "application/json" } -Body $body
```

---

## 📂 Estructura de carpetas

```
smart_irrigation/
├─ manage.py
├─ db.sqlite3
├─ smart_irrigation/
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
└─ parcelas/
   ├─ models.py
   ├─ serializers.py
   ├─ views.py
   ├─ urls.py
   ├─ admin.py
   └─ migrations/
```

---

## 🧭 Objetivo del proyecto

El sistema pretende evolucionar hacia una **plataforma completa de monitorización agrícola**, que permita:
- Registrar parcelas y sensores IoT (digital twin)
- Recoger y analizar lecturas (humedad, temperatura, etc.)
- Generar recomendaciones automáticas de riego
- Visualizar datos en mapas y dashboards

---

## 📅 Historial

| Fecha | Hito | Descripción breve |
|-------|-------|-------------------|
| 2025-10 | Inicio del TFG | Configuración del entorno, creación del proyecto Django |
| 2025-10 | CRUD de Parcelas y Sensores | API REST funcional con SQLite |
| _por definir_ | Próximos módulos | Reglas, alertas, mapa Leaflet, despliegue en Docker |

---

## ✨ Autor

**Víctor Manuel García Alonso**  
Trabajo Fin de Grado — I.E.S Isidra de Guzmán  
C.F.G.S Desarrollo de Aplicaciones Web

---

> 🔧 _Este README está en desarrollo. Se actualizará conforme avance el proyecto y se incorporen nuevas funcionalidades._
