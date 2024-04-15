# Listado de tareas para informe
## Exportar tareas de Bitrix
Primero exportar las tareas de Bitrix siguiendo los siguientes pasos:
1. Ir a la sección de Tareas.
2. Seleccionar el modo de visualización "Lista".
3. Asegurarse que no hayan filtros aplicados.
4. Luego exportar a Microsoft Excel con la opción "Exportar a Excel" -> "Todos los campos de la tarea".

Los pasos se resumen en la siguiente imagen:
![Exportar tareas](./exportar_tareas.png)

Luego, con el archivo de salida `tareas.txt` del scrip `main.py` y un archivo previamente generado `contrato.txt` se tendra el listado de tareas listadas en el contrato, por ejemplo:
```
1. Recopila, analiza, resume y respalda datos para apoyar decisiones estratégicas, comerciales e innovadoras.
2. Supervisa el flujo de datos para recomendar oportunidades de mejora.
3. Identifica oportunidades para la reutilización de datos en toda la institución.
4. Desarrolla e implementa modelos analíticos y descriptivos.
5. Trabaja en estrecha colaboración con áreas comerciales y equipos de proyectos de desarrollo de aplicaciones para resolver problemas de contenido y flujo de información.
6. Recopila datos y requisitos de informes, detecta y resume patrones en datos y hallazgos mediante la producción de informes simples y reporta inconsistencias.
7. Asegura la documentación adecuada y la entrega a tiempo de todos los artefactos funcionales y entregables.
8. Desarrolla procesos de análisis de datos utilizando el marco de trabajo establecido.
9. Certifica que los productos de datos cumplan con las políticas normativas y reglamentos vigentes.
10. Propone mejoras para políticas, normativas y reglamentos relacionados al análisis de datos.
```
## Convertir a formato requerido
Como el formato en el que Bitrix exporta es un psudo-Excel `.xls` se debe convertir a `.xlsx` para poder ser procesado por el script `main.py`. Para ello se puede usar Microsoft Excel, abriendo el archivo y guardandolo en formalo `.xlsx`.
## Uso de GPT
Luego de tener los archivos `tareas.txt` y `contrato.txt` se puede usar el [GPT](https://chat.openai.com/g/g-cpy0fhqB9-reporte-chn) para generar el listado final de tareas en el formato requerido:
```bash
#<codigo_tarea> - <descripcion_tarea> - <numeral_descripcion>
```