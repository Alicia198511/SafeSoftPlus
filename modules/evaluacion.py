# modules/evaluacion.py
import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
import os
from datetime import datetime

archivo_excel = "data/evaluaciones_tk.xlsx"
criterios = ["Fiabilidad", "Eficiencia", "Mantenibilidad", "Usabilidad", "Seguridad"]

def guardar_evaluacion(nombre, entradas):
    datos = {"Evaluador": nombre}
    for i, criterio in enumerate(criterios):
        try:
            valor = float(entradas[i].get())
            if not (0 <= valor <= 10):
                raise ValueError
            datos[criterio] = valor
        except:
            messagebox.showerror("Error", f"'{criterio}' debe estar entre 0 y 10")
            return

    datos["Fecha"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if os.path.exists(archivo_excel):
        df = pd.read_excel(archivo_excel)
        df = pd.concat([df, pd.DataFrame([datos])], ignore_index=True)
    else:
        df = pd.DataFrame([datos])

    df["Promedio"] = df[criterios].mean(axis=1).round(2)
    df.to_excel(archivo_excel, index=False)
    messagebox.showinfo("Guardado", "Evaluación registrada con éxito.")

def formulario_evaluacion(usuario):
    root = tk.Tk()
    root.title("Formulario de Evaluación")
    root.geometry("400x550")

    tk.Label(root, text=f"Evaluador: {usuario}", font=("Arial", 12)).pack(pady=5)

    entradas = []
    for crit in criterios:
        tk.Label(root, text=f"{crit} (0-10):").pack()
        e = tk.Entry(root)
        e.pack(pady=4)
        entradas.append(e)

    tk.Button(root, text="Guardar Evaluación", bg="green", fg="white",
              command=lambda: guardar_evaluacion(usuario, entradas)).pack(pady=10)

    tk.Button(root, text="Ver Evaluaciones", bg="blue", fg="white",
              command=mostrar_evaluaciones).pack(pady=10)

    root.mainloop()

def mostrar_evaluaciones():
    if not os.path.exists(archivo_excel):
        messagebox.showinfo("Sin datos", "No hay evaluaciones aún.")
        return

    df = pd.read_excel(archivo_excel)

    ventana = tk.Toplevel()
    ventana.title("Historial de Evaluaciones")
    ventana.geometry("900x400")

    tabla = ttk.Treeview(ventana)
    tabla.pack(expand=True, fill="both")

    tabla["columns"] = list(df.columns)
    tabla["show"] = "headings"

    for col in df.columns:
        tabla.heading(col, text=col)
        tabla.column(col, anchor="center")

    for _, row in df.iterrows():
        tabla.insert("", "end", values=list(row))
