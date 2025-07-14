# modules/auth.py
import tkinter as tk
from tkinter import messagebox
from modules.ui import crear_interfaz
from modules.data import usuarios_validos, usuarios_nombres

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

    tk.Button(ventana_login, text="Iniciar Sesión", command=validar_login,
              font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=15)
    ventana_login.mainloop()
