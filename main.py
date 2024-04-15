import pandas as pd
from typing import Optional
import datetime as dt

def filtrar_tareas(df, mes: int, año: int, nombre: Optional[str] = None, descripcion: bool = False, excluir_email: bool = False):
    """
    Filtra las tareas en el dataframe basado en el mes, año, y opcionalmente por un nombre específico.
    Si se activa excluir_email, las tareas con descripciones que comienzan con "Email:" son excluidas.
    La columna 'Fecha límite' se utiliza para filtrar por fecha.

    :param df: DataFrame de tareas.
    :param mes: Mes para filtrar.
    :param año: Año para filtrar.
    :param nombre: Nombre opcional para filtrar en 'Responsable' o 'Participantes'.
    :param descripcion: Si True, incluye la descripción en la salida.
    :param excluir_email: Si True, excluye tareas con descripciones que empiezan por "Email:".
    :return: String formateado con las tareas filtradas.
    """

    # Filtrar por mes y año
    df_filtrado = df[df['Fecha límite'].dt.month == mes]
    df_filtrado = df_filtrado[df_filtrado['Fecha límite'].dt.year == año]

    # Filtrar por nombre si se proporciona
    if nombre:
        df_filtrado = df_filtrado[(df_filtrado['Responsable'] == nombre) | 
                                  df_filtrado['Participantes'].str.contains(nombre, na=False)]

    # Excluir tareas cuya descripción empieza por "Email:" si se activa el flag
    if excluir_email:
        df_filtrado = df_filtrado[~df_filtrado['Tarea'].str.startswith('Email:', na=False)]

    # Formatear la salida
    df_filtrado = df_filtrado.sort_values(by='Fecha límite', ascending=True)    
    salida = []
    for _, fila in df_filtrado.iterrows():
        if descripcion and pd.notna(fila["Descripción"]):
            salida.append(f'#{fila["ID"]} - {fila["Tarea"]}: {fila["Descripción"]}')
        else:
            salida.append(f'#{fila["ID"]} - {fila["Tarea"]}')

    return '\n'.join(salida)

if __name__ == '__main__':
    tareas_df = pd.read_excel('tareas.xlsx')

    ejemplo_salida = filtrar_tareas(tareas_df, 3, 2024, nombre='Luis Alvarado', descripcion=True, excluir_email=True)

    with open('tareas.txt', 'w', encoding='utf-8') as f:
        f.write(ejemplo_salida)
