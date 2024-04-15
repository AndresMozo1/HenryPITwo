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
import herramientaSt as hst 

st.set_page_config(
    
    page_title="Análisis Ciudad de Buenos Aires",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)


rutaArchivo = "SQL/siniestrosCaba.db"



# Definir columnas
columnaFecha = 'FECHA'
columnaAnio = 'AÑO'
columnaSemestre = 'SEMESTRE'
columnaVictimas = 'N_VICTIMAS'
columnaSexo = 'SEXO'
columnaTipoCalle = 'TIPO_DE_CALLE'
columnaComuna = 'COMUNA'
columnaEdad = 'EDAD'
columnaDiaSemana ='DIA_SEMANA'
columnaHora = 'HORA'
columnaFranjaHoraria ='FRANJA_HORARIA'
columnaTipoVictima = 'VICTIMA_x'
tipos_victimas = ['MOTO', 'AUTO', 'PEATON', 'BICICLETA', 'CARGAS']



# Creé una página de Streamlit


col1, col2 = st.columns([1,3])

with col1: 
    st.markdown(
        f"""
        <div style='
            border-radius: 10px;
            background-color: #ffed94;
            padding: 5px;
            text-align: center;
            box-shadow: 0 8px 4px 0 rgba(0, 0, 0, 0.2);
            width: 100%;
            margin: 0 auto; /* Esto centra el contenedor horizontalmente */
            '>
            <h3 style='color: #6cb2e0 ;'>
                Siniestralidad vial con victimas fallecidas Ciudad de Buenos Aires 2016-2021
            </h3>
        </div>
        """,
        unsafe_allow_html=True
    )
# Creamos un motor, apuntando a la base de datos de SQLite
engine = create_engine(f'sqlite:///{rutaArchivo}')

# Cargar los datos desde la base de datos
dfPrimerKpi = pd.read_sql_table('primerKPI', con=engine)
dfSegundoKpi = pd.read_sql_table('segundoKPI', con=engine)
dfTercerKpi = pd.read_sql_table('tercerKPI', con=engine)


container_style = """
<style>
.kpi-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 20px 0;
}
</style>
"""
st.write(container_style, unsafe_allow_html=True)

with col2:
    subcol1, subcol2, subcol3 = st.columns(3)

    with subcol1:
        with st.container():
            st.markdown('<div class="kpi-container">', unsafe_allow_html=True)
            fig1 = hst.mostrarPrimerKpi(dfPrimerKpi)
            st.plotly_chart(fig1, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

    with subcol2:
        with st.container():
            st.markdown('<div class="kpi-container">', unsafe_allow_html=True)
            variacion = dfSegundoKpi['VARIACION'].iloc[-1]
            fig2 = go.Figure(go.Indicator(
                mode="gauge+number",
                value=variacion,
                title={'text': "Motociclistas -7%"},
                domain={'x': [0, 1], 'y': [0, 1]},
                gauge={
                    'axis': {'range': [-100, 100]},
                    'bar': {'color': "#ffdb2e" },
                    'steps': [
                    {'range': [-100, 0], 'color': "#ffdb2e"},  # Utilizar otro color de la paleta Viridis
                    {'range': [0, 100], 'color': "#6cb2e0"} 
                    ],
                    'threshold': {
                    'line': {'color': "red", 'width': 2},
                    'thickness': 0.80,
                    'value': variacion }
                }
            ))
            fig2.update_layout(
                width=140,
                height=140,
                margin=dict(l=20, r=20, t=50, b=20)
            )
            st.plotly_chart(fig2, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

    with subcol3:
        with st.container():
            st.markdown('<div class="kpi-container">', unsafe_allow_html=True)
            variacion3 = dfTercerKpi['VARIACION'].iloc[-1]
            fig3 = go.Figure(go.Indicator(
                mode="gauge+number",
                value=variacion3,
                title={'text': "Peatones -10%"},
                domain={'x': [0, 1], 'y': [0, 1]},
                gauge={
                    'axis': {'range': [-100, 100]},
                    'bar': {'color': "#ffdb2e"},
                    'steps': [
                    {'range': [-100, 0], 'color': "#ffdb2e"},  # Utilizar otro color de la paleta Viridis
                    {'range': [0, 100], 'color': "#6cb2e0"}  
                    ],
                    'threshold': {
                    'line': {'color': "red", 'width': 2},
                    'thickness': 0.80,
                    'value': variacion3 }
                }
            ))
            fig3.update_layout(
                width=140,
                height=140,
                margin=dict(l=20, r=20, t=50, b=20)
            )
            st.plotly_chart(fig3, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)


# URL de la imagen
imagen_url = "https://github.com/AndresMozo1/HenryPITwo/blob/main/Imagenes/Insight%20logo.jpg?raw=true"

# Agregar la imagen en la barra lateral
with st.sidebar:
    # Mostrar la imagen con un título opcional
    st.image(imagen_url, caption='Insight Logo', use_column_width=True)




# Barra lateral
with st.sidebar:
    st.title('Filtros')
    
    # Lista de años únicos en orden inverso
    datos = hst.cargarDatos(rutaArchivo)
    yearList = list(datos[columnaAnio].unique())[::-1]
    
    # Seleccioné un rango de años
    rangoAnios = st.slider('Seleccionar un rango de años', min(yearList), max(yearList), (min(yearList), max(yearList)), step=1)
    
     # Lista de tipo de victima
    tiposDeVictimas = ['MOTO', 'AUTO', 'PEATON', 'BICICLETA', 'CARGAS']
    opciones = ['Todas'] + [victima.capitalize() for victima in tiposDeVictimas]

    victimaSeleccionada =  st.selectbox('Seleccionar un tipo de victima', opciones)
    if victimaSeleccionada == 'Todas':
        victimaSeleccionada = None
    else:
        victimaSeleccionada = victimaSeleccionada.upper()

    # Seleccioné un semestre
    semestreList = list(datos[columnaSemestre].unique())
    semestreSeleccionado = st.selectbox('Seleccionar un semestre', ['Todos'] + semestreList)
    if semestreSeleccionado == 'Todos':
        semestreSeleccionado = None
    
    # Seleccioné una comuna
    comunaList = list(datos[columnaComuna].unique())
    comunaSeleccionada = st.selectbox('Seleccionar una comuna', ['Todas'] + comunaList)
    if comunaSeleccionada == 'Todas':
        comunaSeleccionada = None

         # Lista de días de la semana
    diasSemana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    diaSeleccionado = st.selectbox('Seleccionar un día de la semana', ['Todos'] + diasSemana)
    if diaSeleccionado == 'Todos':
        diaSeleccionado = None

     # Lista de franjas horarias
    franjasHorarias = ['00:00 - 03:59', '04:00 - 07:59', '08:00 - 11:59', '12:00 - 15:59', '16:00 - 19:59', '20:00 - 23:59']
    franjaSeleccionada = st.selectbox('Seleccionar una franja horaria', ['Todas'] + franjasHorarias)
    if franjaSeleccionada == 'Todas':
        franjaSeleccionada = None 


   



# Convertí la columna de fecha a tipo datetime
datos = hst.convertirAFecha(datos, columnaFecha)

# Filtré los datos según los criterios seleccionados
datosFiltrados = hst.filtrarDatos(datos, columnaAnio, columnaSemestre, columnaComuna, rangoAnios, semestreSeleccionado, comunaSeleccionada, franjaSeleccionada, diaSeleccionado, victimaSeleccionada)

# Eliminé filas con valores nulos en las columnas de coordenadas
datosFiltrados = datosFiltrados.dropna(subset=['latitude', 'longitude'])

# Calcular el total de víctimas
totalVictimas = hst.calcularTotalVictimas(datosFiltrados, columnaVictimas)


# Mostrar el número total de víctimas en un cuadro con un tamaño de fuente más grande
st.write(f"<div style='font-size: 24px; color:#007bc7 ;'>Total de víctimas para el periodo seleccionado: {totalVictimas}</div>", unsafe_allow_html=True)

# Organizar los gráficos en tres columnas
col1, col2, col3 = st.columns(3)

# Gráfico de distribución de víctimas por año y semestre
with col1:
    
    hst.graficarDistribucionVictimasPorAnioYSemestre(datosFiltrados, columnaAnio, columnaSemestre, columnaVictimas)

# Gráfico de cantidad de víctimas por mes
with col2:
    
    hst.graficarVictimasPorMes(datosFiltrados, columnaFecha, columnaVictimas)

# Gráfico de distribución por sexos
with col3:
    
    hst.graficarVictimasPorTipoCalle(datosFiltrados, columnaTipoCalle, columnaVictimas)

col14, col15,  = st.columns([0.85,3.15])

with col14:
    st.subheader("Actor vial-año.")
    hst.tablaVictimasPorTipoActorVialYAnio(datos, columnaAnio, columnaTipoVictima, tipos_victimas)

with col15:
    hst.graficarVictimasPorDiaSemanaYTipoDeVictima(datosFiltrados,columnaTipoVictima,victimaSeleccionada)


# Organizar los gráficos en tres columnas
col16, col17  = st.columns(2)

# Gráfico de cantidad de víctimas por tipo de calle
with col16:
    hst.graficarDistribucionVictimasPorFranjaHoraria(datosFiltrados)
    

# Gráfico de cantidad de víctimas por comuna
with col17:
    
    hst.graficarVictimasPorComuna(datosFiltrados, columnaComuna, columnaVictimas)


   

col8, col9 = st.columns(2)

with col8:

    heatmapData = datosFiltrados.groupby(['longitude', 'latitude']).size().reset_index(name='count')
    st.map(heatmapData, zoom=11, use_container_width=False)


# Visualizar distribución de víctimas por franja horaria
with col9:
    
    hst.graficarVictimasPorDiaSemana(datosFiltrados)

# Organizar los gráficos en tres columnas
co20, col21 = st.columns(2)

# Mapa de calor de la distribución de accidentes por ubicación
with co20:
    
    hst.graficarDistribucionPorSexos(datosFiltrados, columnaSexo)
    


with col21:
    
    hst.graficarVictimasPorEdad(datosFiltrados, columnaEdad, columnaVictimas)



st.markdown(
        f"""
        <div style='
            border-radius: 10px;
            background-color: #f3f6f9;
            padding: 5px;
            text-align: center;
            box-shadow: 0 0px 0px 0 rgba(0, 0, 0, 0.2);
            width: 100%;
            margin: 0 auto; /* Esto centra el contenedor horizontalmente */
            '>
            <h2 style='color: '#91634f'  ;'>
                Indicadores Clave de Rendimiento 
            </h2>
        </div>
        """,
        unsafe_allow_html=True
    )


# Mostrar los KPIs
st.altair_chart(hst.mostrarPrimerKpiG(dfPrimerKpi), use_container_width=True)

col22, col23 = st.columns(2)

with col22: 
    # Mostrar el segundo KPI
    figSegundoKpi = hst.mostrarSegundoKpi(dfSegundoKpi)
    st.plotly_chart(figSegundoKpi)

with col23:
    # Mostrar el tercer KPI
    figTercerKpi = hst.mostrarTercerKpi(dfTercerKpi)
    st.plotly_chart(figTercerKpi)

