import os
from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd

# Crear la clase de modelo de la tabla principal
Base = declarative_base()

class TablaSiniestro(Base):
    __tablename__ = 'siniestros'
    ID = Column(String, primary_key=True, index=True)
    N_VICTIMAS = Column(Integer)
    FECHA = Column(DateTime)
    HORA = Column(DateTime)
    LUGAR_DEL_HECHO = Column(String)
    TIPO_DE_CALLE = Column(String)
    COMUNA = Column(Integer)
    pos_x = Column('pos x', Float)
    pos_y = Column('pos y', Float)
    PARTICIPANTES = Column(String)
    VICTIMA_x = Column(String)
    ACUSADO = Column(String)
    AÑO = Column(Integer)
    ROL = Column(String)
    SEXO = Column(String)
    EDAD = Column(Integer)
    FECHA_FALLECIMIENTO = Column(DateTime)
    SEMESTRE = Column(Integer)
    FECHA_COMPLETA = Column(DateTime)
    FRANJA_HORARIA = Column(String)
    DIA_SEMANA = Column(String)
    MES = Column(Integer)


# Definir la clase de modelo de la tabla `primerKPI`
class TablaPrimerKPI(Base):
    __tablename__ = 'primerKPI'

    ID = Column(Integer, primary_key=True, index=True)
    AÑO = Column(Integer)
    SEMESTRE = Column(Integer)
    VICTIMA_x = Column(Integer)
    MES = Column(Integer)
    POBLACION_TOTAL = Column(Float)
    TASA_SEMESTRAL = Column(Float)


# Definir la clase de modelo de la tabla `segundoKPI`
class TablaSegundoKPI(Base):
    __tablename__ = 'segundoKPI'

    ID = Column(Integer, primary_key=True, index=True)
    AÑO = Column(Integer)
    VICTIMA_x = Column(Integer)
    POBLACION_TOTAL = Column(Float)
    VICTIMAS_POR_AÑO = Column(Integer)
    VARIACION = Column(Float)


# Definir la clase de modelo de la tabla `tercerKPI`
class TablaTercerKPI(Base):
    __tablename__ = 'tercerKPI'
    ID = Column(Integer, primary_key=True, index=True)
    AÑO = Column(Integer)
    N_VICTIMAS = Column(Integer)
    VICTIMAS_ANTERIORES = Column(Integer)
    VARIACION = Column(Float)
    MES = Column(Integer)

directorio_target = 'SQL'  # Nombre de la carpeta a almacenar la base de datos
# Creamos el directorio si no existe
os.makedirs(directorio_target, exist_ok=True)

# Creamos un motor que almacena los datos en el archivo 'siniestros_viales_caba.db',
# en el 'directorio_target'
engine = create_engine(f'sqlite:///{directorio_target}/siniestrosCaba.db')

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)

# Creamos una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Cargamos los dataframe que contienen la data a cargar a SQLite
dfConsolidado = pd.read_csv('DataFrames/consolidadoAccidentes.csv')
dfPrimerKPI = pd.read_csv('DataFrames/primerKPI.csv')
dfSegundoKPI = pd.read_csv('DataFrames/segundoKPI.csv')
dfTercerKPI = pd.read_csv('DataFrames/tercerKPI.csv')

# Cargamos los dataframe que contienen la data a cargar a SQLite
dfConsolidado.to_sql('siniestros', engine, if_exists='replace', index=False)
dfPrimerKPI.to_sql('primerKPI', engine, if_exists='replace', index=False)
dfSegundoKPI.to_sql('segundoKPI', engine, if_exists='replace', index=False)
dfTercerKPI.to_sql('tercerKPI', engine, if_exists='replace', index=False)



# Le damos commit a la sesión
session.commit()
# Cerramos la sesión
session.close()


