```markdown
# 🚀 SafeSoftPlus

**SafeSoftPlus** es una plataforma interactiva para evaluar la **calidad** y **seguridad** de aplicaciones de software.  
Está orientada a testers, desarrolladores y equipos QA que desean centralizar sus procesos de evaluación, generar reportes automáticos, visualizar resultados y recibir recomendaciones según estándares como **ISO/IEC 25010** y **OWASP**.

---

## 🧩 Características Principales

- 🧪 Evaluación de software por criterios: Fiabilidad, Eficiencia, Mantenibilidad, Usabilidad y Seguridad.
- 📊 Visualización gráfica de resultados por usuario.
- 📁 Historial de evaluaciones con filtros por usuario y fecha.
- 🔐 Inicio de sesión con roles diferenciados (Administrador / Evaluador).
- 📄 Generación automática de reportes y gráficos en PDF/PNG.
- 🧠 Recomendaciones automáticas basadas en resultados.
- 🧪 Simulador de vulnerabilidades comunes (pendiente o en desarrollo).
- ⚙️ Modo demo para exploración sin datos reales.
- 🧹 Opción para limpiar evaluaciones registradas (módulo `limpiador_excel.py`).

---

## 📁 Estructura del Proyecto

```

SafeSoftPlus/
│
├── main.py # Archivo principal para iniciar la aplicación
├── README.md # Documentación general del proyecto
├── manual_usuario.md # Manual para usuarios finales
├── manual_programador.md # Manual para desarrolladores
├── requirements.txt # Dependencias y librerías requeridas
├── evaluaciones_tk.xlsx # Archivo Excel con evaluaciones registradas
├── convertir_docx.py # Módulo para manejo de documentos .docx
├── reportes/ # Carpeta para almacenar PDFs y gráficos exportados
└── modules/ # Módulos principales
├── auth.py # Gestión de autenticación y usuarios
├── data.py # Diccionarios de usuarios y nombres
├── evaluacion.py # Lógica de evaluación (opcional)
├── limpiador_excel.py # Limpieza de datos Excel
├── reportes.py # Generación de reportes PDF
├── ui.py # Interfaz gráfica y funcionalidades
└── utils.py # Funciones utilitarias
````

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.12**
- **Tkinter** – Interfaz gráfica
- **Pandas** – Procesamiento de datos
- **Matplotlib** – Visualización de gráficos
- **openpyxl** – Lectura/escritura de archivos Excel
- **fpdf / fpdf2** – Generación de archivos PDF
- **docx** – Visualización de documentación `.docx`

---

## 🚀 Instalación y Ejecución

1. **Clonar el repositorio desde GitHub:**

```bash
git clone https://github.com/Alicia198511/SafeSoftPlus.git
cd SafeSoftPlus
````

2. **Instalar las dependencias:**

```bash
pip install -r requirements.txt
```

3. **Ejecutar la aplicación:**

```bash
python main.py
```

---

## 👥 Roles y Accesos

| Rol       | Acceso                                                             |
| --------- | ------------------------------------------------------------------ |
| Admin     | Evaluaciones, historial, generación de reportes, limpieza de datos |
| Evaluador | Solo evaluaciones y su historial propio                            |

---

## 📤 Exportación de Reportes

* Al guardar una evaluación, se genera automáticamente una gráfica con los resultados.
* Los archivos PDF/PNG se almacenan en la carpeta `/reportes/`.
* Incluye botón "📤 Exportar Gráfico" para generar manualmente.

---

## 🧼 Limpieza de Evaluaciones

Puedes usar el módulo `limpiador_excel.py` para vaciar o resetear las evaluaciones del archivo `evaluaciones_tk.xlsx`.

---

## 📄 Licencia

Este proyecto está licenciado bajo la **MIT License**. Consulta el archivo [LICENSE](LICENSE) para más información.

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas!
Puedes:

* Crear un **pull request** con mejoras o correcciones
* Reportar errores abriendo un **issue**
* Compartir ideas para nuevas funcionalidades

---

## ✍️ Autor

**Alicia Murillo**
Estudiante de Desarrollo de Software – 🇪🇨 Ecuador
Proyecto académico para la asignatura **Calidad y Seguridad de Software** (2025)
🔗 [github.com/Alicia198511/SafeSoftPlus](https://github.com/Alicia198511/SafeSoftPlus)

