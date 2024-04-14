import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import altair as alt
import plotly.graph_objects as go
import plotly.express as px
from sqlalchemy import create_engine
# Deshabilitar la advertencia PyplotGlobalUseWarning
import warnings
warnings.filterwarnings("ignore", message="Global instance of matplotlib.pyplot")


@st.cache_data
def cargarDatos(rutaArchivo):
    """Cargue los datos desde un archivo SQL."""
    # Creamos un motor, apuntando a la base de datos de SQLite
    engine = create_engine(f'sqlite:///{rutaArchivo}')
    
    # Consulta SQL para seleccionar todos los registros de la tabla 'siniestros'
    consultaSQL = "SELECT * FROM siniestros"
    
    # Leer los datos de la tabla en un DataFrame de Pandas
    datos = pd.read_sql_query(consultaSQL, con=engine)
    
    # Renombrar las columnas de las coordenadas
    datos.rename(columns={'pos x': 'longitude', 'pos y': 'latitude'}, inplace=True)
    
    return datos


def tablaVictimasPorTipoActorVialYAnio(datos, columnaAnio, columnaTipoVictima, tipos_victimas):
    """Muestra una tabla con el número de víctimas por tipo de actor vial y año."""

    # Filtrar datos solo para los tipos de víctimas especificados
    datos_filtrados = datos[datos[columnaTipoVictima].isin(tipos_victimas)]

    # Agrupar por tipo de víctima y año y sumar el número de víctimas
    tabla_victimas = datos_filtrados.groupby([columnaTipoVictima, columnaAnio])[columnaTipoVictima].count().unstack()

    # Mostrar la tabla
    st.write(tabla_victimas)



columnaDiaSemana ='DIA_SEMANA'
columnaFranjaHoraria ='FRANJA_HORARIA'
columnaTipoVictima = 'VICTIMA_x'





def convertirAFecha(datos, columnaFecha):
    """Convertí la columna de fecha a tipo datetime."""
    datos[columnaFecha] = pd.to_datetime(datos[columnaFecha])
    return datos

def filtrarDatos(datos, columnaAño, columnaSemestre, columnaComuna, rangoAños, semestreSeleccionado, comunaSeleccionada, franjaHorariaSeleccionada, díaSeleccionado, tipoVíctimaSeleccionado):
    """Filtré los datos por año, semestre, comuna y franja horaria."""
    datosFiltrados = datos[
        (datos[columnaAño].between(rangoAños[0], rangoAños[1])) &
        ((datos[columnaSemestre] == semestreSeleccionado) | (semestreSeleccionado is None)) &
        ((datos[columnaComuna] == comunaSeleccionada) | (comunaSeleccionada is None)) &
        ((datos[columnaFranjaHoraria] == franjaHorariaSeleccionada) | (franjaHorariaSeleccionada is None)) &
        ((datos[columnaDiaSemana] == díaSeleccionado) | (díaSeleccionado is None)) &
        ((datos[columnaTipoVictima] == tipoVíctimaSeleccionado) | (tipoVíctimaSeleccionado is None))
    ]
    return datosFiltrados

def calcularTotalVictimas(datos, columnaVictimas):
    """Calculé el número total de víctimas."""
    totalVictimas = datos[columnaVictimas].sum()
    return totalVictimas


def graficarVictimasPorDiaSemanaYTipoDeVictima(datos, columnaTipoVictima, color_discrete_sequence=None):
    """Visualiza la cantidad de víctimas por día de la semana y por tipo de víctima."""
    
    # Convertir los valores de la columna 'VICTIMA_x' a título (primera letra mayúscula y resto minúscula)
    datos['VICTIMA_x'] = datos['VICTIMA_x'].str.title()
    
    # Definir el orden de los días de la semana
    orden_dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    
    # Paleta de colores personalizada predefinida
    customColors = ['#91634f', '#007bc7', '#ffdb2e']

    try:
        # Crear el gráfico de líneas utilizando Altair
        fig = alt.Chart(datos).mark_line(point=True).encode(
            x=alt.X('DIA_SEMANA', title='Día de la semana', sort=orden_dias_semana),
            y=alt.Y('VICTIMA_x', title='Número de víctimas', axis=alt.Axis(labelAngle=0, titleFontSize=14)),
            color=alt.Color(columnaTipoVictima, scale=alt.Scale(range=customColors)),
            tooltip=['DIA_SEMANA', columnaTipoVictima, 'VICTIMA_x']
        ).properties(
            title="Comparación entre actores viales por día de la semana",
            width=800
        ).configure_axis(
            labelFontSize=12,
            titleFontSize=14
        ).configure_title(
            fontSize=16
        )

        # Mostrar el gráfico
        st.altair_chart(fig, use_container_width=True)

    except Exception as e:
        st.error(f"Se ha producido un error: {e}")




def graficarDistribucionVictimasPorAnioYSemestre(datos, columnaAnio, columnaSemestre, columnaVictimas):
    """Visualiza la distribución de víctimas por año y semestre con un gráfico de línea con marcadores."""
    datosAgrupados = datos.groupby([columnaAnio, columnaSemestre])[columnaVictimas].sum().reset_index()
    
    titulo_grafico = f"Distribución de víctimas por año y semestre"
    
    # Define la paleta de colores
    paleta_colores = ['#3c4b5c', '#6cb2e0','#063970 ','#ffdb2e', '#91634f', '21130d']  
    
    grafico = alt.Chart(datosAgrupados).mark_line(point=True).encode(
        x=alt.X(columnaAnio, title='Año'),
        y=alt.Y(columnaVictimas, title='Número de víctimas'),
        color=alt.Color(columnaSemestre, scale=alt.Scale(range=paleta_colores)),
        tooltip=[columnaAnio, columnaSemestre, columnaVictimas]
    ).properties(
        title=titulo_grafico
    ).interactive().configure_view(
        strokeWidth=0
    ).configure_title(
        fontSize=12,
        anchor='middle'
    ).configure_axis(
        labelFontSize=12,
        titleFontSize=12
    ).configure_legend(
        labelFontSize=12
    )

    st.altair_chart(grafico, use_container_width=True)



def graficarVictimasPorMes(datos, columnaFecha, columnaVictimas):
    """Visualiza la cantidad de víctimas por mes."""
    meses = datos[columnaFecha].dt.month_name(locale='es_ES')  # Cambia los nombres de los meses a español
    victimasPorMes = datos.groupby(meses)[columnaVictimas].sum().reset_index()
    
    # Ordenar los meses cronológicamente
    orden_meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    victimasPorMes[columnaFecha] = pd.Categorical(victimasPorMes[columnaFecha], categories=orden_meses, ordered=True)
    victimasPorMes = victimasPorMes.sort_values(columnaFecha)
    
    titulo_grafico = f"Cantidad de víctimas por mes"
    
    # Define la paleta de colores
    paleta_colores = ['#3c4b5c', '#96adbe', '#ffdb2e', '#91634f', '#6cb2e0']  
    
    grafico = alt.Chart(victimasPorMes).mark_bar().encode(
        x=alt.X(columnaFecha, title='Mes', axis=alt.Axis(labelAngle=90)),  # Girar las etiquetas del eje x
        y=alt.Y(columnaVictimas, title='Número de víctimas'),
        tooltip=[columnaFecha, columnaVictimas],
        color=alt.Color(columnaFecha, scale=alt.Scale(range=paleta_colores))
    ).properties(
        title=titulo_grafico
    ).interactive().configure_view(
        strokeWidth=0
    ).configure_title(
        fontSize=14
    ).configure_axis(
        labelFontSize=12,
        titleFontSize=12
    ).configure_legend(
        labelFontSize=12
    )
    
    st.altair_chart(grafico, use_container_width=True)


def graficarVictimasPorMes(datos, columnaFecha, columnaVictimas):
    """Visualiza la cantidad de víctimas por mes."""
    meses = datos[columnaFecha].dt.month_name(locale='es_ES')  # Cambia los nombres de los meses a español
    victimasPorMes = datos.groupby(meses)[columnaVictimas].sum().reset_index()

    # Ordenar los meses cronológicamente
    orden_meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                   'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    victimasPorMes[columnaFecha] = pd.Categorical(victimasPorMes[columnaFecha], categories=orden_meses, ordered=True)
    victimasPorMes = victimasPorMes.sort_values(columnaFecha)

    titulo_grafico = f"Cantidad de víctimas por mes"

    # Define la paleta de colores
    paleta_colores = ['#3c4b5c', '#96adbe', '#ffdb2e', '#91634f', '#6cb2e0']

    grafico = alt.Chart(victimasPorMes).mark_bar().encode(
        x=alt.X(columnaFecha, title='Mes', axis=alt.Axis(labelAngle=90)),  # Girar las etiquetas del eje x
        y=alt.Y(columnaVictimas, title='Número de víctimas'),
        tooltip=[columnaFecha, columnaVictimas],
        color=alt.Color(columnaFecha, scale=alt.Scale(range=paleta_colores))
    ).properties(
        title=titulo_grafico
    ).interactive().configure_view(
        strokeWidth=0
    ).configure_title(
        fontSize=14
    ).configure_axis(
        labelFontSize=12, titleFontSize=12
    ).configure_legend(
        labelFontSize=12
    )

    st.altair_chart(grafico, use_container_width=True)




def graficarDistribucionPorSexos(datos, columnaSexo):
    """Visualiza la distribución de víctimas por sexo en un gráfico de dona."""
    conteos = datos[columnaSexo].value_counts().reset_index()
    conteos.columns = [columnaSexo, 'conteo']

    titulo_grafico = "Distribución por sexos"
    
    # Define la paleta de colores
    paleta_colores = ['#ffdb2e', '#6cb2e0', '#91634f']

    # Crear la figura de dona
    fig = go.Figure(data=[go.Pie(labels=conteos[columnaSexo], values=conteos['conteo'], hole=0.4)])
    fig.update_traces(marker=dict(colors=paleta_colores))
    fig.update_layout(title=titulo_grafico, width=380, height=380)

    st.plotly_chart(fig)






def graficarVictimasPorTipoCalle(datos, columnaTipoCalle, columnaVictimas):
    """Visualiza la cantidad de víctimas por tipo de calle con un gráfico de tipo rosquilla."""
    datosAgrupados = datos.groupby(columnaTipoCalle)[columnaVictimas].sum().reset_index()

    titulo_grafico = f"Cantidad de víctimas por tipo de calle"
    
    # Define la paleta de colores
    paleta_colores = ['#3c4b5c', '#6cb2e0', '#ffdb2e', '#91634f', '#6cb2e0']

    # Crear la figura de dona
    fig = go.Figure(data=[go.Pie(labels=datosAgrupados[columnaTipoCalle], values=datosAgrupados[columnaVictimas], hole=0.5)])
    fig.update_traces(marker=dict(colors=paleta_colores))
    fig.update_layout(title=titulo_grafico, width=350, height=350)

    st.plotly_chart(fig)




def graficarDistribucionVictimasPorFranjaHoraria(datosFiltrados):
    """Visualiza la distribución de víctimas por franja horaria."""
    datosAgrupados = datosFiltrados['FRANJA_HORARIA'].value_counts().reset_index()
    datosAgrupados.columns = ['FRANJA_HORARIA', 'Número de víctimas']
    titulo_grafico = f"Distribución de víctimas por franja horaria"
    
    # Definir los colores de la paleta
    colores_paleta = ['#3c4b5c', '#96adbe', '#ffdb2e', '#91634f', '#6cb2e0']
    
    # Crear el gráfico de barras
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=datosAgrupados['Número de víctimas'],
        y=datosAgrupados['FRANJA_HORARIA'],
        orientation='h',
        marker=dict(
            color=colores_paleta
        )
    ))
    
    # Configurar el diseño del gráfico
    fig.update_layout(
        xaxis_title='Número de víctimas',
        yaxis_title='Franja horaria',
        font=dict(size=12),
        title=dict(
            text=titulo_grafico,
            font=dict(size=14)
        ),
        yaxis=dict(tickfont=dict(size=12)),
        legend=dict(
            title=None,
            font=dict(size=12)
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)

    


def graficarVictimasPorComuna(datos, columnaComuna, columnaVictimas):
    """Visualiza la cantidad de víctimas por comuna."""
    datosAgrupados = datos.groupby(columnaComuna)[columnaVictimas].sum().reset_index()
    titulo_grafico = f"Cantidad de víctimas por comuna"

    # Convertir la columna de comuna a categórica y ordenarla
    datosAgrupados[columnaComuna] = datosAgrupados[columnaComuna].astype(int)
    datosAgrupados = datosAgrupados.sort_values(columnaComuna)
    datosAgrupados[columnaComuna] = datosAgrupados[columnaComuna].astype(str)
    datosAgrupados[columnaComuna] = pd.Categorical(datosAgrupados[columnaComuna], categories=datosAgrupados[columnaComuna].unique(), ordered=True)

    # Definir la paleta de colores
    paleta_colores = ['#3c4b5c', '#96adbe', '#ffdb2e', '#91634f', '#6cb2e0']

    grafico = alt.Chart(datosAgrupados).mark_bar().encode(
        x=alt.X(columnaComuna, title='Comuna'),
        y=alt.Y(columnaVictimas, title='Número de víctimas'),
        tooltip=[columnaComuna, columnaVictimas],
        color=alt.Color(columnaComuna, scale=alt.Scale(range=paleta_colores))
    ).properties(
        title=titulo_grafico
    ).interactive().configure_view(
        strokeWidth=0
    ).configure_title(
        fontSize=14
    ).configure_axis(
        labelFontSize=12, titleFontSize=12
    ).configure_legend(
        labelFontSize=12
    )

    st.altair_chart(grafico, use_container_width=True)


def graficarVictimasPorEdad(datos, columnaEdad, columnaVictimas):
    """Visualiza la cantidad de víctimas por rango de edad."""
    datosAgrupados = datos.groupby(columnaEdad)[columnaVictimas].count().reset_index()

    titulo_grafico = f"Cantidad de víctimas por rango de edad"
    
    # Definir los colores de la paleta
    colores_paleta = ['#3c4b5c', '#96adbe', '#ffdb2e', '#91634f', '#6cb2e0']

    grafico = alt.Chart(datosAgrupados).mark_bar().encode(
        x=alt.X(columnaEdad, title='Rango de edad'),
        y=alt.Y(columnaVictimas, title='Número de víctimas'),
        tooltip=[columnaEdad, columnaVictimas],
        color=alt.Color(columnaEdad, scale=alt.Scale(range=colores_paleta))
    ).properties(
        title=titulo_grafico
    ).configure_view(
        strokeWidth=0
    ).configure_title(
        fontSize=18
    ).configure_axis(
        labelFontSize=12,
        titleFontSize=14
    ).configure_legend(
        labelFontSize=12
    ).interactive()

    st.altair_chart(grafico, use_container_width=True)


def graficarVictimasPorDiaSemana(datos):
    """Visualiza la cantidad de víctimas por día de la semana."""
    datosAgrupados = datos['DIA_SEMANA'].value_counts().reset_index()
    datosAgrupados.columns = ['Día de la semana', 'Número de víctimas']
    
    # Definir el orden de los días de la semana
    diasSemana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    
    # Definir la paleta de colores
    colores_paleta = ['#3c4b5c', '#96adbe', '#ffdb2e', '#91634f', '#6cb2e0']
    
    grafico = alt.Chart(datosAgrupados).mark_bar().encode(
        y=alt.Y('Día de la semana', title='Día de la semana', sort=diasSemana),
        x=alt.X('Número de víctimas', title='Número de víctimas'),
        color=alt.Color('Día de la semana', scale=alt.Scale(range=colores_paleta)),
        tooltip=['Día de la semana', 'Número de víctimas']
    ).configure_view(
        strokeWidth=0
    ).configure_title(
        fontSize=14,
        anchor='middle'
    ).configure_axis(
        labelFontSize=12,
        titleFontSize=12
    ).configure_legend(
        labelFontSize=12
    ).interactive()
    
    st.altair_chart(grafico, use_container_width=True)



def mostrarPrimerKpiG(df):
    """
    Muestra el indicador del primer KPI: reducción porcentual en la tasa de homicidios en siniestros viales
    para los últimos seis meses, en comparación con el semestre anterior.

    Args:
    - df: DataFrame que contiene los datos relevantes.

    Returns:
    - chart: Gráfico de barras comparando la tasa de homicidios por semestre.
    """
    # Agrupar los datos por año y semestre, y calcular la tasa de homicidios
    dfGrouped = df.groupby(['AÑO', 'SEMESTRE']).sum().reset_index()
    dfGrouped['Tasa de homicidios'] = dfGrouped['VICTIMA_x'] / dfGrouped['POBLACION TOTAL'] * 100000

    # Crear una columna con el año y semestre en el formato deseado
    dfGrouped['Año-Semestre'] = dfGrouped['AÑO'].astype(str) + '-' + dfGrouped['SEMESTRE'].astype(str)

    # Crear una lista con los años y semestres en el orden deseado
    anosSemestres = sorted(dfGrouped['Año-Semestre'].unique())

    # Crear el gráfico de barras
    chart = alt.Chart(dfGrouped).mark_bar().encode(
        x=alt.X('Año-Semestre:N', sort=anosSemestres),
        y='Tasa de homicidios:Q',
        color=alt.Color('SEMESTRE:N', scale=alt.Scale(range=['#ffdb2e', '#6cb2e0'])),
        tooltip=['AÑO', 'SEMESTRE', 'Tasa de homicidios']
    ).properties(
        width=800,
        height=400,
        title='Tasa homicidios en siniestros viales 2021. Ultimo semestre: 1.32 - Penultimo semestre:1.70 (-22,6)'
    )

    return chart 



def mostrarSegundoKpi(df):
    """
    Muestra el indicador del segundo KPI: variación en la cantidad de accidentes mortales en moto.

    Args:
    - df: DataFrame que contiene los datos relevantes.

    Returns:
    - fig: Gráfico de barras comparando la cantidad de accidentes mortales en moto por año y la variación porcentual.
    """
    # Calcular la variación en la cantidad de accidentes mortales en moto
    variacion = df['VARIACION'].iloc[-1]

    # Crear el gráfico de barras con Plotly
    fig = px.bar(df, x='AÑO', y='VICTIMA_x', color='VARIACION', 
                title="Accidentes Mortales en moto 2021 :43 vs 2020 : 27 (-59,3) ",
                labels={'VICTIMA_x': 'Víctimas', 'AÑO': 'Año'},
                color_continuous_scale=['#3c4b5c', '#96adbe', '#ffdb2e', '#91634f', '#6cb2e0'])

    # Actualizar el título de la barra de colores
    fig.update_layout(coloraxis_colorbar_title='Variación')

    return fig



def mostrarTercerKpi(df):
    """
    Muestra el indicador del tercer KPI: variación en la accidentalidad de peatones.

    Args:
    - df: DataFrame que contiene los datos relevantes.

    Returns:
    - fig: Gráfico que muestra la cantidad de accidentes de peatones por año y la variación porcentual.
    """
    # Calcular la reducción porcentual en la accidentalidad de peatones para el último año
    accidentalidadUltimoAnio = df['N_VICTIMAS'].iloc[-1]
    accidentalidadAnioAnterior = df['VICTIMAS_ANTERIORES'].iloc[-1]
    variacion_accidentalidad = ((accidentalidadAnioAnterior - accidentalidadUltimoAnio) / accidentalidadAnioAnterior) * 100

    # Definir el color manualmente
    color = '#ffdb2e'

    # Crear la gráfica con Plotly
    fig = go.Figure()

    # Añadir el gráfico de líneas para visualizar la cantidad de accidentes de peatones por año
    fig.add_trace(go.Scatter(x=df['AÑO'], y=df['N_VICTIMAS'], mode='lines', name='Accidentalidad '))

    # Añadir el gráfico de barras para visualizar la variación en la cantidad de accidentes de peatones por año
    fig.add_trace(go.Bar(x=df['AÑO'], y=df['VARIACION'], name='Variación ', marker_color=color))

    # Configurar el diseño del gráfico
    fig.update_layout(
        title='Victimas mortales peatones año 2021: 33 vs 2020 : 32 (-2,94)',
        xaxis_title='Año',
        yaxis_title='Cantidad / Variación (%)',
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
        yaxis=dict(
            tickformat="%.2f"  # Formato de dos dígitos en el eje y
        )
    )

    return fig

def mostrarPrimerKpi(df):
    """
    Muestra el indicador del primer KPI: reducción porcentual en la tasa de homicidios
    en siniestros viales para los últimos seis meses, en comparación con el semestre anterior.

    Args:
    - df: DataFrame que contiene los datos relevantes.

    Returns:
    - fig: Figura del indicador tipo velocímetro.
    """

    # Filtrar los datos por el último semestre
    ultimo_semestre = df[df['SEMESTRE'] == 2].iloc[-1]
    semestre_anterior = df[df['SEMESTRE'] == 1].iloc[-1]

    # Calcular la tasa de homicidios para los últimos seis meses
    tasa_ultimo_semestre = ultimo_semestre['VICTIMA_x'] / ultimo_semestre['POBLACION TOTAL'] * 100000

    # Calcular la tasa de homicidios para el semestre anterior
    tasa_semestre_anterior = semestre_anterior['VICTIMA_x'] / semestre_anterior['POBLACION TOTAL'] * 100000

    # Calcular la reducción porcentual negativa
    reduccion_porcentual_negativa = ((tasa_ultimo_semestre - tasa_semestre_anterior) / tasa_semestre_anterior) * 100

    # Crear la figura del indicador tipo velocímetro
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=reduccion_porcentual_negativa,
        title={'text': "Siniestralidad -10%"},
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [-100, 100]},
            'bar': {'color': "#ffdb2e"},  # Utilizar el primer color de la paleta Viridis
            'steps': [
                {'range': [-100, 0], 'color': "#ffdb2e"},  # Utilizar otro color de la paleta Viridis
                {'range': [0, 100], 'color': "#6cb2e0"}  # Utilizar un color de la paleta Viridis
            ],
            'threshold': {
                'line': {'color': "red", 'width': 2},
                'thickness': 0.80,
                'value': reduccion_porcentual_negativa }
        }
    ))

    # Ajustar el tamaño del gráfico
    fig.update_layout(
        width=140,
        height=140,
        margin=dict(l=20, r=20, t=50, b=20)
    )

    return fig
