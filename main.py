import pandas as pd
from typing import Optional
import datetime as dt

def filtrar_tareas(df, mes: int, año: int, nombre: Optional[str] = None, descripcion: bool = False):
    """
    Filtra las tareas en el dataframe basado en el mes, año, y opcionalmente por un nombre específico.
    La columna 'Cerrado el' se utiliza para filtrar por fecha.

    :param df: DataFrame de tareas.
    :param mes: Mes para filtrar.
    :param año: Año para filtrar.
    :param nombre: Nombre opcional para filtrar en 'Persona responsable' o 'Participantes'.
    :param descripcion: Si True, incluye la descripción en la salida.
    :return: String formateado con las tareas filtradas.
    """

    # Filtrar por mes y año
    df_filtrado = df[df['Fecha límite'].dt.month == mes]
    df_filtrado = df_filtrado[df_filtrado['Fecha límite'].dt.year == año]

    # Filtrar por nombre si se proporciona
    if nombre:
        df_filtrado = df_filtrado[(df_filtrado['Persona responsable'] == nombre) | 
                                  df_filtrado['Participantes'].str.contains(nombre, na=False)]

    # Formatear la salida
    salida = []
    for _, fila in df_filtrado.iterrows():
        if descripcion and pd.notna(fila["Descripción"]):
            salida.append(f'#{fila["ID"]} - {fila["Tarea"]}: {fila["Descripción"]}')
        else:
            salida.append(f'#{fila["ID"]} - {fila["Tarea"]}')

    return '\n'.join(salida)

# Ejemplo de uso de la función
# Aquí uso el mes 11 y el año 2023 como ejemplo. Se puede ajustar para otros valores.
tareas_df = pd.read_excel('tareas.xlsx')

ejemplo_salida = filtrar_tareas(tareas_df, 2, 2024, nombre='Luis Alvarado', descripcion=1)
print(ejemplo_salida)