import pandas as pd
from typing import Optional
import datetime as dt

def filtrar_tareas(df, fecha_inicial: Optional[str] = None, fecha_final: Optional[str] = None, nombre: Optional[str] = None, descripcion: bool = True, excluir_email: bool = True):
    """
    Filtra las tareas en el dataframe basado en una fecha inicial y una fecha final, y opcionalmente por un nombre específico.
    Si se activa excluir_email, las tareas con descripciones que comienzan con "Email:" son excluidas.
    La columna 'Fecha límite' se utiliza para filtrar por fecha.

    :param df: DataFrame de tareas.
    :param fecha_inicial: Fecha inicial para filtrar en formato 'YYYY-MM-DD'.
    :param fecha_final: Fecha final para filtrar en formato 'YYYY-MM-DD'.
    :param nombre: Nombre opcional para filtrar en 'Responsable' o 'Participantes'.
    :param descripcion: Si True, incluye la descripción en la salida.
    :param excluir_email: Si True, excluye tareas con descripciones que empiezan por "Email:".
    :return: String formateado con las tareas filtradas.
    """

    # Establecer fechas por defecto si no se proporcionan
    if not fecha_inicial:
        fecha_inicial = (dt.datetime.now() - dt.timedelta(days=30)).strftime('%Y-%m-%d')
    if not fecha_final:
        fecha_final = dt.datetime.now().strftime('%Y-%m-%d')

    fecha_inicial = pd.to_datetime(fecha_inicial)
    fecha_final = pd.to_datetime(fecha_final)

    # Filtrar por rango de fechas
    df_filtrado = df[(df['Fecha límite'] >= fecha_inicial) & (df['Fecha límite'] <= fecha_final)]
    # Filtrar por nombre si se proporciona
    if nombre:
        df_filtrado = df_filtrado[(df_filtrado['Responsable'].str.contains(nombre, na=False, case=False)) | 
                                  df_filtrado['Participantes'].str.contains(nombre, na=False, case=False)]

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
    tareas_df['Fecha límite'] = pd.to_datetime(tareas_df['Fecha límite'], dayfirst=True, format='%d/%m/%Y %H:%M:%S')

    ejemplo_salida = filtrar_tareas(tareas_df, fecha_inicial='2024-05-16', fecha_final='2024-06-12')

    with open('tareas.txt', 'w', encoding='utf-8') as f:
        f.write(ejemplo_salida)
