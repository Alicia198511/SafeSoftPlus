
```markdown
# Manual del Programador – SafeSoftPlus

---

## 1. Nombre del Proyecto

SafeSoftPlus – Plataforma de Evaluación de Calidad y Seguridad de Software

---

## 2. Objetivo del Proyecto

Desarrollar una aplicación de escritorio que permita realizar evaluaciones de calidad y seguridad sobre aplicaciones de software, aplicando criterios definidos y generando reportes automáticos con recomendaciones.

---

## 3. Requisitos del Sistema

- Python 3.12 o superior  
- Sistema operativo: Windows, Linux o macOS  
- Paquetes instalados desde `requirements.txt`  
- Entorno virtual (opcional pero recomendado)  

---

## 4. Dependencias Utilizadas

- pandas  
- matplotlib  
- openpyxl  
- fpdf  

---

## 5. Estructura del Proyecto

```

SafeSoftPlus/
├── main.py
├── README.md
├── requirements.txt
├── documentacion.docx
├── evaluaciones\_tk.xlsx
├── modules/
│   ├── auth.py
│   ├── evaluacion.py
│   ├── reportes.py
│   ├── ui.py
│   ├── utils.py
│   └── **init**.py

````

---

## 6. Explicación de los Módulos

- **main.py**: Punto de entrada de la aplicación, inicializa la interfaz y módulos.  
- **auth.py**: Módulo de autenticación con validación de usuarios por rol (admin/tester).  
- **evaluacion.py**: Lógica de evaluación de funcionalidades y vulnerabilidades.  
- **reportes.py**: Generación de reportes PDF con resultados y recomendaciones.  
- **ui.py**: Interfaz gráfica construida con Tkinter.  
- **utils.py**: Funciones auxiliares y utilitarias compartidas.  
- **evaluaciones_tk.xlsx**: Archivo local donde se almacenan las evaluaciones realizadas.  

---

## 7. Instrucciones de Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/Alicia198511/SafeSoftPlus.git
cd SafeSoftPlus
````

2. Crear entorno virtual (opcional):

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## 8. Ejecución del Sistema

Ejecutar la aplicación con:

```bash
python main.py
```

Se abrirá la interfaz principal de la plataforma.

---

## 9. Consideraciones Técnicas

* Mantener el archivo `evaluaciones_tk.xlsx` en la raíz del proyecto para evitar errores de lectura/escritura.
* El sistema no requiere conexión a internet para funcionar.
* Los reportes generados se exportan en formato PDF dentro de la carpeta `reportes/`.

---

## 10. Autor

Alicia
Estudiante de Desarrollo de Software
GitHub: [https://github.com/Alicia198511](https://github.com/Alicia198511)

Proyecto académico – Calidad y Seguridad de Software (2025)

```

