````markdown
# Manual del Usuario – SafeSoftPlus

---

## 1. ¿Qué es SafeSoftPlus?

SafeSoftPlus es una aplicación de escritorio que permite a los usuarios realizar evaluaciones de calidad y seguridad sobre software, ofreciendo una interfaz amigable y herramientas para generar reportes automáticos en PDF, así como visualizar gráficos con resultados y recomendaciones.

---

## 2. Requisitos previos

- Tener instalado Python 3.12 o superior.  
- Instalar las dependencias listadas en el archivo `requirements.txt`.  
- No tener abierto el archivo `evaluaciones_tk.xlsx` en otras aplicaciones mientras se usa SafeSoftPlus.

---

## 3. Cómo abrir la aplicación

1. Abre la terminal o consola.  
2. Navega a la carpeta del proyecto SafeSoftPlus.  
3. Ejecuta el comando:

```bash
python main.py
````

Aparecerá la ventana principal de la aplicación con la pantalla de bienvenida.

---

## 4. Uso de la aplicación

### a) Pantalla de Login

* Ingresa tu usuario y contraseña para iniciar sesión.
* Los usuarios pueden tener roles distintos (por ejemplo, admin o tester).

### b) Evaluación

* Completa los campos de evaluación para los criterios:

  * Fiabilidad
  * Eficiencia
  * Mantenibilidad
  * Usabilidad
  * Seguridad
* Los valores deben estar entre 0 y 10.
* Haz clic en **Guardar Evaluación** para almacenar la información en el archivo Excel.

### c) Reportes y análisis

* Usa el botón **Ver Evaluaciones** para consultar las evaluaciones registradas.
* Usa el botón **Ver Historial y Gráficos** para visualizar tu historial de evaluaciones y gráficos comparativos.
* La aplicación genera automáticamente reportes en PDF con recomendaciones basadas en tus evaluaciones, guardados en la carpeta `reportes/`.

---

## 5. Consejos útiles

* Guarda tu trabajo regularmente.
* No abras el archivo `evaluaciones_tk.xlsx` en otra aplicación mientras usas SafeSoftPlus para evitar conflictos.
* Consulta el manual del programador si requieres información técnica o deseas colaborar en el desarrollo.

---

## 6. Contacto para soporte

Para dudas o soporte técnico, contacta a:

**Alicia**
GitHub: [https://github.com/Alicia198511](https://github.com/Alicia198511)


