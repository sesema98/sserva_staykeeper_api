# 🏨 StayKeeper API

## 📘 Descripción

**StayKeeper** es una API REST construida con **Django** y **Django REST Framework (DRF)** para gestionar **reservas de hotel** y la información de los **clientes**.  
Permite realizar operaciones completas de **CRUD** (Crear, Leer, Actualizar, Eliminar) y realizar **búsquedas filtradas** por cliente o habitación.

------------------------------------------------------------
## ⚙️ Tecnologías utilizadas

- 🐍 Python 3.11  
- 🌐 Django 5.2.7  
- 🧩 Django REST Framework 3.16.1  
- 💾 SQLite3 (base de datos por defecto)

------------------------------------------------------------
## 🚀 Configuración del proyecto

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/sesema98/sserva_staykeeper_api.git
```

### 2️⃣ Entrar al directorio
```bash
cd sserva_staykeeper_api
```

### 3️⃣ Crear y activar entorno virtual
```bash
python -m venv venv
venv\Scripts\activate
```

### 4️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 5️⃣ Aplicar migraciones
```bash
python manage.py migrate
```

### 6️⃣ Iniciar el servidor
```bash
python manage.py runserver
```

### 7️⃣ Acceder a la API
```
http://127.0.0.1:8000/api/
```

------------------------------------------------------------
## 📡 Endpoints disponibles

### 🧍 Clientes

| Método | Endpoint | Descripción |
|---------|-----------|-------------|
| GET | `/api/clientes/` | Listar todos los clientes |
| POST | `/api/clientes/` | Crear un nuevo cliente |
| PUT / PATCH | `/api/clientes/{id}/` | Editar un cliente existente |
| DELETE | `/api/clientes/{id}/` | Eliminar un cliente |

------------------------------------------------------------
### 🏨 Reservas

| Método | Endpoint | Descripción |
|---------|-----------|-------------|
| GET | `/api/reservas/` | Listar todas las reservas |
| POST | `/api/reservas/` | Crear una nueva reserva |
| PUT / PATCH | `/api/reservas/{id}/` | Editar una reserva existente |
| DELETE | `/api/reservas/{id}/` | Eliminar una reserva |
| GET | `/api/reservas/?search={query}` | Buscar por cliente o número de habitación |

------------------------------------------------------------
## 🧪 Ejemplos de uso

### ✳️ Crear cliente
```bash
curl -X POST -H "Content-Type: application/json" -d "{\"nombre\":\"Arnold Schwarz\", \"documento\":\"1234567890\"}" http://127.0.0.1:8000/api/clientes/
```
<img width="870" height="463" alt="image" src="https://github.com/user-attachments/assets/30ba904f-f8bc-4995-9607-dac662d2f039" />

------------------------------------------------------------
### 🗓️ Crear reserva
```bash
curl -X POST -H "Content-Type: application/json" -d "{\"fecha_ingreso\":\"2025-11-05\", \"fecha_salida\":\"2025-11-08\", \"numero_habitacion\":203, \"cliente\":1}" http://127.0.0.1:8000/api/reservas/
```
<img width="866" height="556" alt="image" src="https://github.com/user-attachments/assets/24034b43-1f99-4f27-bb61-2bad48d1f2f9" />

------------------------------------------------------------
### 🔍 Búsqueda
```bash
curl -X GET "http://127.0.0.1:8000/api/reservas/?search=Arnold"
```
<img width="930" height="604" alt="image" src="https://github.com/user-attachments/assets/dc9fa06e-b24d-4024-9618-0276104a1252" />

**Ejemplo de respuesta:**
```json
[
  {
    "id": 1,
    "fecha_ingreso": "2025-11-05",
    "fecha_salida": "2025-11-08",
    "numero_habitacion": 203,
    "cliente": 1,
    "cliente_nombre": "Arnold Schwarz"
  }
]
```

------------------------------------------------------------
## 🧾 Información del proyecto

- **Proyecto:** staykeeper_api  
- **Autor:** Sergio Serva Mariño
- **Seccion:** C24 A
- **Año:** 2025  

✨ Desarrollado con Django REST Framework — Simplicidad, claridad y orden para tu examen.
