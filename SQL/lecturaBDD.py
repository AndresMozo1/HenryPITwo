import pandas as pd
from sqlalchemy import create_engine


# Creamos un motor, apuntando la base de datos de interes
engine = create_engine('sqlite:///SQL/siniestrosCaba.db')
# Cargamos la data de SQL a dataframes
dfconsolidadoAccidentes = pd.read_sql_table('siniestros', con=engine)
dfprimerKPI = pd.read_sql_table('primerKPI', con=engine)
dfsegundoKPI = pd.read_sql_table('segundoKPI', con=engine)
dftercerKPI = pd.read_sql_table('tercerKPI', con=engine)

# Imprimimos para confirmar el contenido de los dataframe
print(dfconsolidadoAccidentes, dfprimerKPI, dfsegundoKPI, dftercerKPI)

