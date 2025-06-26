# Proyecto de Notas - Vue.js + Django + PostgreSQL

Un proyecto básico para crear y gestionar notas con Vue.js en el frontend y Django en el backend.

## Estructura del Proyecto

```
aws-project/
├── frontend/          # Aplicación Vue.js
├── backend/           # API Django
└── README.md
```

## Requisitos

- Python 3.8+
- Node.js 16+
- PostgreSQL
- pip
- npm

## Instalación

### Backend (Django)

1. Crear entorno virtual:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Configurar base de datos:
```bash
python manage.py migrate
```

4. Crear superusuario:
```bash
python manage.py createsuperuser
```

5. Ejecutar servidor:
```bash
python manage.py runserver
```

### Frontend (Vue.js)

1. Instalar dependencias:
```bash
cd frontend
npm install
```

2. Ejecutar servidor de desarrollo:
```bash
npm run dev
```

## Uso

- Backend API: http://localhost:8000
- Frontend: http://localhost:5173
- Admin Django: http://localhost:8000/admin 