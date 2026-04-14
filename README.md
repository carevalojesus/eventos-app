# 🎉 Gestión de Eventos — Monorepo Didáctico

Proyecto didáctico **full-stack** con:

- **Backend:** Django 5 + Django REST Framework + MongoEngine (MongoDB Atlas)
- **Frontend:** Astro + Tailwind CSS (SSR/estático + islas)

Pensado para la asignatura de **Lenguaje de Programación II (LP2)** y similares.

---

## 📁 Estructura

```
eventos-app/
├── backend/          # API REST con Django + MongoEngine
│   └── eventos_api/
└── frontend/         # Cliente web con Astro
```

---

## 🚀 Puesta en marcha rápida

### 1. Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env              # edita con tu URI de MongoDB Atlas
cd eventos_api
python manage.py runserver
```

API disponible en: `http://localhost:8000/api/eventos/`

### 2. Frontend

```bash
cd frontend
npm install
npm run dev
```

Web disponible en: `http://localhost:4321`

---

## 🔑 Variables de entorno

### Backend (`backend/.env`)

```env
SECRET_KEY=django-insecure-cambia-esto-en-produccion
DEBUG=True
MONGODB_URI=mongodb+srv://USUARIO:PASSWORD@cluster0.xxxxx.mongodb.net/
MONGODB_DB=eventos_db
CORS_ORIGIN=http://localhost:4321
```

### Frontend (`frontend/.env`)

```env
PUBLIC_API_URL=http://localhost:8000/api
```

---

## 📚 Endpoints

| Método | URL                        | Descripción                    |
|--------|----------------------------|--------------------------------|
| GET    | `/api/eventos/`            | Listar todos los eventos       |
| POST   | `/api/eventos/`            | Crear un nuevo evento          |
| GET    | `/api/eventos/{id}/`       | Obtener un evento por ID       |
| PUT    | `/api/eventos/{id}/`       | Actualizar un evento completo  |
| PATCH  | `/api/eventos/{id}/`       | Actualizar campos parciales    |
| DELETE | `/api/eventos/{id}/`       | Eliminar un evento             |

---

## 🧪 Probar rápido con cURL

```bash
# Crear
curl -X POST http://localhost:8000/api/eventos/ \
  -H "Content-Type: application/json" \
  -d '{"titulo":"Charla Python","descripcion":"Intro a OOP","fecha":"2026-05-20T18:00:00","lugar":"FISI-UNAP","cupo":50}'

# Listar
curl http://localhost:8000/api/eventos/
```
