# modules/ui.py
import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
import os
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from modules.data import usuarios_nombres
from modules.reportes import generar_reporte_pdf

archivo_excel = "evaluaciones_tk.xlsx"
criterios = ["Fiabilidad", "Eficiencia", "Mantenibilidad", "Usabilidad", "Seguridad"]

# Resto del código igual (no requiere cambios adicionales)
# ...


def guardar_en_excel(nombre, datos_criterios):
    datos = {"Evaluador": nombre}
    for i, criterio in enumerate(criterios):
        try:
            valor = float(datos_criterios[i].get())
            if not (0 <= valor <= 10):
                raise ValueError
            datos[criterio] = valor
        except ValueError:
            messagebox.showerror("Error", f"El valor para '{criterio}' debe estar entre 0 y 10.")
            return

    datos["Fecha"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if os.path.exists(archivo_excel):
        df_existente = pd.read_excel(archivo_excel)
        df_nuevo = pd.concat([df_existente, pd.DataFrame([datos])], ignore_index=True)
    else:
        df_nuevo = pd.DataFrame([datos])

    df_nuevo["Promedio"] = df_nuevo[criterios].mean(axis=1).round(2)
    df_nuevo.to_excel(archivo_excel, index=False)

    messagebox.showinfo("Éxito", f"Evaluación de {nombre} guardada correctamente.")

    # Generar reporte PDF después de guardar
    promedio_ultimo = df_nuevo.iloc[-1]["Promedio"]
    datos_ultimo = {c: df_nuevo.iloc[-1][c] for c in criterios}
    generar_reporte_pdf(nombre, datos_ultimo, promedio_ultimo, usuarios_nombres)

def ver_excel():
    if not os.path.exists(archivo_excel):
        messagebox.showinfo("Información", "No hay evaluaciones registradas aún.")
        return

    df = pd.read_excel(archivo_excel)

    ventana_excel = tk.Toplevel()
    ventana_excel.title("Evaluaciones Registradas")
    ventana_excel.geometry("900x400")

    tabla = ttk.Treeview(ventana_excel)
    tabla.pack(expand=True, fill="both")

    tabla["columns"] = list(df.columns)
    tabla["show"] = "headings"

    for col in df.columns:
        tabla.heading(col, text=col)
        tabla.column(col, anchor="center")

    for _, row in df.iterrows():
        tabla.insert("", "end", values=list(row))

def mostrar_historial_con_graficos(usuario):
    if not os.path.exists(archivo_excel):
        messagebox.showinfo("Información", "No hay evaluaciones aún.")
        return

    df = pd.read_excel(archivo_excel)
    df_usuario = df[df["Evaluador"] == usuario]

    if df_usuario.empty:
        messagebox.showinfo("Sin datos", "Este usuario no tiene evaluaciones registradas.")
        return

    nombre_completo = usuarios_nombres.get(usuario, usuario)

    ventana_historial = tk.Toplevel()
    ventana_historial.title("📊 Historial de Evaluaciones y Gráficos")
    ventana_historial.geometry("1100x600")
    ventana_historial.configure(bg="#f5f5f5")

    paned = tk.PanedWindow(ventana_historial, orient=tk.HORIZONTAL)
    paned.pack(fill="both", expand=True, padx=10, pady=10)

    frame_tabla = tk.Frame(paned, width=250, bg="white")
    paned.add(frame_tabla)

    frame_grafico = tk.Frame(paned, bg="white")
    paned.add(frame_grafico)

    tabla = ttk.Treeview(frame_tabla)
    tabla.pack(expand=True, fill="both", padx=5, pady=5)

    tabla["columns"] = list(df_usuario.columns)
    tabla["show"] = "headings"

    for col in df_usuario.columns:
        tabla.heading(col, text=col)
        tabla.column(col, anchor="center", width=100, stretch=False)

    for _, row in df_usuario.iterrows():
        tabla.insert("", "end", values=list(row))

    scrollbar_tabla = ttk.Scrollbar(frame_tabla, orient="vertical", command=tabla.yview)
    tabla.configure(yscrollcommand=scrollbar_tabla.set)
    scrollbar_tabla.pack(side="right", fill="y")

    fig, ax = plt.subplots(figsize=(5.5, 4))

    try:
        df_usuario = df_usuario.sort_values(by="Fecha").reset_index(drop=True)
        df_usuario[criterios].plot(kind="bar", ax=ax)
        ax.set_title(f"Evaluaciones realizadas por {nombre_completo}")
        ax.set_xlabel("Evaluación N°")
        ax.set_ylabel("Puntaje (0-10)")
        ax.set_ylim(0, 10)
        ax.legend(loc="upper right", fontsize="small")
        fig.tight_layout()
    except Exception as e:
        ax.text(0.5, 0.5, f"No se pudo generar el gráfico\n{str(e)}",
                ha="center", va="center", fontsize=12, color="red")

    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True, padx=5, pady=5)

    def exportar_grafico():
        carpeta = "reportes"
        os.makedirs(carpeta, exist_ok=True)
        nombre_archivo_base = f"grafico_{usuario.replace(' ', '_')}"
        ruta_png = os.path.join(carpeta, f"{nombre_archivo_base}.png")
        ruta_pdf = os.path.join(carpeta, f"{nombre_archivo_base}.pdf")

        fig.savefig(ruta_png)
        fig.savefig(ruta_pdf)
        messagebox.showinfo("Éxito", f"Gráfico exportado como:\n{ruta_png}\n{ruta_pdf}")

    tk.Button(frame_grafico, text="📤 Exportar Gráfico", command=exportar_grafico,
              font=("Arial", 11), bg="#FF9800", fg="white").pack(pady=10)

def crear_interfaz(evaluador):
    root = tk.Tk()
    root.title("Evaluación de Calidad de Software")
    root.geometry("400x600")
    root.configure(bg="#f0f0f0")

    nombre_completo = usuarios_nombres.get(evaluador, evaluador)

    tk.Label(root, text="🧪 Evaluación de Calidad de Software", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)
    tk.Label(root, text=f"Evaluador: {nombre_completo}", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="blue").pack(pady=5)

    entradas_criterios = []
    for criterio in criterios:
        tk.Label(root, text=f"{criterio} (0 a 10):", font=("Arial", 12), bg="#f0f0f0").pack()
        entry = tk.Entry(root, font=("Arial", 12))
        entry.pack(pady=5)
        entradas_criterios.append(entry)

    tk.Button(root, text="Guardar Evaluación", command=lambda: guardar_en_excel(evaluador, entradas_criterios),
              font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=10)

    tk.Button(root, text="Ver Evaluaciones", command=ver_excel,
              font=("Arial", 12), bg="#2196F3", fg="white").pack(pady=10)

    tk.Button(root, text="📈 Ver Historial y Gráficos", command=lambda: mostrar_historial_con_graficos(evaluador),
              font=("Arial", 12), bg="#9C27B0", fg="white").pack(pady=10)

    root.mainloop()
