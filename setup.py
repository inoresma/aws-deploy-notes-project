#!/usr/bin/env python3
"""
Script de configuración para el proyecto de notas
"""
import os
import subprocess
import sys

def run_command(command, cwd=None):
    """Ejecuta un comando y maneja errores"""
    try:
        subprocess.run(command, shell=True, check=True, cwd=cwd)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error ejecutando: {command}")
        print(f"Error: {e}")
        return False

def setup_backend():
    """Configura el backend de Django"""
    print("Configurando backend...")
    
    # Crear entorno virtual
    if not os.path.exists("backend/venv"):
        print("Creando entorno virtual...")
        if not run_command("python -m venv venv", cwd="backend"):
            return False
    
    # Activar entorno virtual e instalar dependencias
    if sys.platform == "win32":
        pip_cmd = "venv\\Scripts\\pip"
        python_cmd = "venv\\Scripts\\python"
    else:
        pip_cmd = "venv/bin/pip"
        python_cmd = "venv/bin/python"
    
    print("Instalando dependencias de Python...")
    if not run_command(f"{pip_cmd} install -r requirements.txt", cwd="backend"):
        return False
    
    # Crear archivo .env si no existe
    env_file = "backend/.env"
    if not os.path.exists(env_file):
        print("Creando archivo .env...")
        with open(env_file, "w") as f:
            f.write("SECRET_KEY=django-insecure-change-this-in-production\n")
            f.write("DEBUG=True\n")
            f.write("DB_NAME=notes_db\n")
            f.write("DB_USER=postgres\n")
            f.write("DB_PASSWORD=\n")
            f.write("DB_HOST=localhost\n")
            f.write("DB_PORT=5432\n")
    
    # Ejecutar migraciones
    print("Ejecutando migraciones...")
    if not run_command(f"{python_cmd} manage.py makemigrations", cwd="backend"):
        return False
    
    if not run_command(f"{python_cmd} manage.py migrate", cwd="backend"):
        return False
    
    print("Backend configurado correctamente!")
    return True

def setup_frontend():
    """Configura el frontend de Vue.js"""
    print("Configurando frontend...")
    
    print("Instalando dependencias de Node.js...")
    if not run_command("npm install", cwd="frontend"):
        return False
    
    print("Frontend configurado correctamente!")
    return True

def main():
    """Función principal"""
    print("=== Configuración del Proyecto de Notas ===")
    print()
    
    # Verificar que PostgreSQL esté instalado
    print("IMPORTANTE: Asegúrate de tener PostgreSQL instalado y corriendo.")
    print("También crea una base de datos llamada 'notes_db'")
    print()
    
    # Configurar backend
    if not setup_backend():
        print("Error configurando el backend")
        return
    
    # Configurar frontend
    if not setup_frontend():
        print("Error configurando el frontend")
        return
    
    print()
    print("=== Configuración completada ===")
    print()
    print("Para ejecutar el proyecto:")
    print()
    print("1. Backend (Django):")
    print("   cd backend")
    if sys.platform == "win32":
        print("   venv\\Scripts\\activate")
        print("   python manage.py runserver")
    else:
        print("   source venv/bin/activate")
        print("   python manage.py runserver")
    print()
    print("2. Frontend (Vue.js):")
    print("   cd frontend")
    print("   npm run dev")
    print()
    print("3. Acceder a:")
    print("   - Frontend: http://localhost:5173")
    print("   - Backend API: http://localhost:8000/api/")
    print("   - Admin Django: http://localhost:8000/admin")

if __name__ == "__main__":
    main() 