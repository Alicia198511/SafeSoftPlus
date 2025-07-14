import pandas as pd

def limpiar_excel():
    print("✅ Archivo limpiado correctamente.")

# Ruta del archivo
archivo = "evaluaciones_tk.xlsx"

# Criterios esperados
columnas_requeridas = [
    "Evaluador", "Fiabilidad", "Eficiencia",
    "Mantenibilidad", "Usabilidad", "Seguridad",
    "Fecha", "Promedio"
]

try:
    df = pd.read_excel(archivo)

    # Filtrar solo las columnas válidas
    df = df[[col for col in columnas_requeridas if col in df.columns]]

    # Eliminar filas con valores vacíos
    df = df.dropna()

    # Opcional: Validar que los valores estén entre 0 y 10 en criterios
    for criterio in ["Fiabilidad", "Eficiencia", "Mantenibilidad", "Usabilidad", "Seguridad"]:
        df = df[(df[criterio] >= 0) & (df[criterio] <= 10)]

    # Guardar limpio
    df.to_excel(archivo, index=False)
    print("✅ Archivo limpiado correctamente.")
except Exception as e:
    print("❌ Error limpiando el archivo:", str(e))
