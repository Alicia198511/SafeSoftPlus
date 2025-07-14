def mostrar_readme():
    import tkinter as tk
    from tkinter import scrolledtext

    try:
        with open("README.md", "r", encoding="utf-8") as file:
            contenido = file.read()
    except FileNotFoundError:
        contenido = "❌ El archivo README.md no fue encontrado."

    ventana_readme = tk.Toplevel()
    ventana_readme.title("📘 Documentación del Proyecto")
    ventana_readme.geometry("700x600")

    texto = scrolledtext.ScrolledText(ventana_readme, wrap=tk.WORD, font=("Arial", 12))
    texto.insert(tk.END, contenido)
    texto.pack(expand=True, fill="both")
    texto.configure(state="disabled")
