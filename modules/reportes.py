import os
from fpdf import FPDF
from datetime import datetime

def generar_recomendaciones(datos):
    recomendaciones = []
    for criterio, valor in datos.items():
        if valor < 3:
            recomendaciones.append(
                f"El criterio '{criterio}' tiene un puntaje bajo ({valor}). Se recomienda revisar y mejorar este aspecto."
            )
        elif valor < 4:
            recomendaciones.append(
                f"El criterio '{criterio}' tiene un puntaje aceptable ({valor}), pero puede optimizarse para mayor calidad."
            )
        else:
            recomendaciones.append(
                f"El criterio '{criterio}' cumple satisfactoriamente con los estándares ({valor})."
            )
    return "\n".join(recomendaciones)

def generar_reporte_pdf(evaluador, datos, promedio, usuarios_nombres=None):
    carpeta = "reportes"
    os.makedirs(carpeta, exist_ok=True)

    fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nombre_archivo = os.path.join(carpeta, f"reporte_{evaluador}_{fecha}.pdf")

    if usuarios_nombres is None:
        nombre_completo = evaluador
    else:
        nombre_completo = usuarios_nombres.get(evaluador, evaluador)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(0, 10, "SafeSoft+ - Reporte de Evaluación", ln=True)
    pdf.cell(0, 10, f"Evaluador: {nombre_completo}", ln=True)
    pdf.cell(0, 10, f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
    pdf.ln(10)

    pdf.set_font("Arial", size=11)
    for criterio, valor in datos.items():
        pdf.cell(0, 10, f"{criterio}: {valor}", ln=True)

    pdf.ln(5)
    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(0, 10, f"Promedio Total: {promedio}", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(0, 10, "Recomendaciones:", ln=True)

    pdf.set_font("Arial", size=11)
    recomendaciones_texto = generar_recomendaciones(datos)
    pdf.multi_cell(0, 10, recomendaciones_texto)

    pdf.output(nombre_archivo)
    print(f"✅ Reporte PDF generado: {nombre_archivo}")
