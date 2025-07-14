import sys
import os
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Asegurar que se puedan importar módulos desde la carpeta 'modules'
sys.path.append(os.path.join(os.path.dirname(__file__), "modules"))

# Importar módulos del sistema
from limpiador_excel import limpiar_excel
from auth import usuarios_validos, usuarios_nombres
from ui import crear_interfaz

def mostrar_bienvenida():
    texto = """
📄 SafeSoft+: Plataforma de Evaluación de Calidad y Seguridad

🔹 Introducción

SafeSoft+ es una plataforma interactiva diseñada para evaluar la calidad y seguridad de aplicaciones de software.  
Permite a desarrolladores, testers y docentes realizar auditorías rápidas sobre aspectos fundamentales  
como funcionalidad, usabilidad, confiabilidad y medidas básicas de seguridad.

🎯 Objetivo General

Desarrollar una herramienta interactiva que permita evaluar y reportar el cumplimiento de criterios de calidad del software  
(como funcionalidad, usabilidad y confiabilidad) y verificar medidas básicas de seguridad (como autenticación, manejo de errores  
y protección de datos) en aplicaciones desarrolladas bajo metodologías ágiles o tradicionales.

👥 ¿A quién está dirigido?

- Estudiantes y docentes de carreras de informática o software.  
- Equipos de desarrollo que deseen validar sus entregables.  
- Testers o QA que necesiten aplicar validaciones rápidas.  
- Proyectos académicos o de investigación sobre calidad y seguridad de software.

🛠️ Funcionalidades del sistema

• Inicio de sesión con roles diferenciados (Administrador y Evaluador).  
• Formulario de evaluación por criterios: Fiabilidad, Eficiencia, Mantenibilidad, Usabilidad, Seguridad.  
• Almacenamiento de evaluaciones en Excel con historial filtrable por usuario y fecha.  
• Cálculo automático del promedio por evaluación.  
• Visualización del historial por usuario con gráficos comparativos para análisis detallado.  
• Generación automática de reportes en PDF con recomendaciones personalizadas.  
• Visualización integrada del archivo README y manuales técnicos directamente desde la interfaz.  
• Módulo para manejo y conversión de documentos `.docx` si es necesario.  
• Uso de GitHub para control de versiones y colaboración eficiente durante el desarrollo.

📂 Estructura del Proyecto

 SafeSoftPlus/
│
├── main.py                       # Archivo principal para ejecutar la app
├── README.md                     # Documentación general
├── manual_usuario.md             # Manual del usuario final
├── manual_programador.md         # Manual del programador
├── requirements.txt              # Librerías necesarias
├── evaluaciones_tk.xlsx          # Base de datos de evaluaciones en Excel
├── convertir_docx.py             # Conversión o lectura de archivos .docx
│
├── reportes/                     # Carpeta de reportes generados (PDF, imágenes)
│   └── ... (se generan dinámicamente)
│
├── modules/                      # Lógica modular del proyecto
│   ├── __init__.py               # (opcional, puede estar vacío)
│   ├── auth.py                   # Usuarios y contraseñas (login)
│   ├── data.py                   # Diccionarios, configuraciones
│   ├── evaluacion.py             # Reglas de evaluación (opcional)
│   ├── limpiador_excel.py        # Limpieza de datos previos en Excel
│   ├── reportes.py               # Generación de reportes en PDF
│   ├── ui.py                     # Interfaz principal tras login
│   └── utils.py                  # Funciones auxiliares
"""

    ventana = tk.Tk()
    ventana.title("Bienvenida a SafeSoft+")
    ventana.geometry("850x600")

    texto_area = scrolledtext.ScrolledText(ventana, wrap="word", font=("Arial", 11))
    texto_area.insert("1.0", texto)
    texto_area.config(state="disabled")
    texto_area.pack(expand=True, fill="both", padx=10, pady=10)

    tk.Button(ventana, text="Iniciar Aplicación", command=ventana.destroy).pack(pady=10)
    ventana.mainloop()

def mostrar_login():
    ventana_login = tk.Tk()
    ventana_login.title("Login - Evaluación de Software")
    ventana_login.geometry("300x200")
    ventana_login.configure(bg="#f0f0f0")

    tk.Label(ventana_login, text="Usuario:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
    entry_usuario = tk.Entry(ventana_login, font=("Arial", 12))
    entry_usuario.pack(pady=5)

    tk.Label(ventana_login, text="Contraseña:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
    entry_contrasena = tk.Entry(ventana_login, show="*", font=("Arial", 12))
    entry_contrasena.pack(pady=5)

    def validar_login():
        usuario = entry_usuario.get().strip()
        contrasena = entry_contrasena.get().strip()

        if usuario in usuarios_validos and usuarios_validos[usuario] == contrasena:
            ventana_login.destroy()
            crear_interfaz(usuario)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    tk.Button(ventana_login, text="Iniciar Sesión", command=validar_login, font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=15)
    ventana_login.mainloop()

if __name__ == "__main__":
    try:
        limpiar_excel()  # limpia datos inválidos del Excel antes de comenzar
    except Exception as e:
        print(f"[!] Error al limpiar Excel: {e}")

    mostrar_bienvenida()
    mostrar_login()
