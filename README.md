<h1 align='center'>
 <b>Analisis Siniestralidad vial Ciudad de Buenos Aires 2016 - 2021</b>
</h1>


![image](https://github.com/AndresMozo1/HenryPITwo/assets/76072127/86dffe8b-7292-498b-a6bd-8de169d2aefc)


<h2 align='center'>
 <b> Proyecto Individual Data Analytics </b>
</h2>

<p align='center'>
    Wilmer Andrés Mozo Villamil DATA PT07
</p>


   

<div style="text-align:center">
  <img src="https://github.com/AndresMozo1/secondHenry/assets/76072127/f95b8b0f-8cb2-4a1a-b10d-b64caffcd10a" alt="imagen" />
</div>

Buenos Aires, una ciudad donde la historia y la modernidad se entrelazan en un vibrante tapiz cultural. Desde su fundación hasta el presente, la Ciudad Autónoma de Buenos Aires (CABA) ha sido testigo de un crecimiento constante y una rica diversidad de experiencias, con sus calles impregnadas de música, arte y gastronomía. Buenos Aires es un destino turístico de renombre mundial. Sus emblemáticos barrios, como San Telmo, La Boca y Palermo, ofrecen una variedad de atracciones que cautivan a visitantes de todas partes.

Sin embargo, como muchas otras ciudades, Buenos Aires enfrenta desafíos en materia de seguridad vial. Entre 2018 y 2022, se registraron más de 19,000 muertes por siniestros viales en toda Argentina (más de 700 en solo CABA), lo que destaca la necesidad urgente de medidas para proteger a los ciudadanos en las vías. Es en este contexto que se desarrolló un proyecto de análisis de datos con el objetivo de proporcionar información valiosa a las autoridades locales. Se exploraron patrones, se identificaron áreas críticas y se propusieron soluciones para mejorar la seguridad vial en la ciudad.

A través de este proyecto, se busca no solo analizar datos, sino también contribuir a la construcción de un futuro más seguro y próspero para los habitantes de Buenos Aires. Cada vida importa, y trabajar juntos nos permite crear un entorno más seguro para todos los ciudadanos.


![image](https://github.com/AndresMozo1/HenryPITwo/assets/76072127/9b253b8c-1561-4c4c-a6d8-ad2529fb6b93)


Durante el  primer contacto con los datos, [EDA.ipynb](https://github.com/AndresMozo1/HenryPITwo/blob/main/EDA.ipynb) me enfoque en analizar la composición y el tamaño de los datasets recibidos, con el propósito de observar similitudes, unificar información y avanzar hacia la visualización de los datos. Se realizó un análisis exhaustivo columna por columna en busca de información relevante o duplicada, así como la verificacion el formato de los datos, con el fin de tener un panorama claro para el desarrollo del proyecto.

Paso seguido empece a buscar Insights que me permitieran entender un poco mas las causas de la accidentalidad vial en CABA , las zonas con mayor insidencia, los actores viales, las franjas horarias y hasta los dias de la semana con el fin de tener una vision amplia y precisa que permita crear un plan de accion a corto , mediano y largo plazo; mientras se realizaba este analsis exploratorio de los datos, se empezaron a hacer visibles diferentes patrones y tendencias , datos que se pudieron verificar con fuentes oficiales y en este punto identifique la necesidad de 'enriquecer' los datos; partiendo del hecho que  el Sistema Nacional de Información Criminal (SNIC) define la tasa de homicidios en siniestros viales como el número de víctimas fatales en accidentes de tránsito por cada 100,000 habitantes en un área geográfica durante un período de tiempo específico.

<p align='center'>
  <img src="https://github.com/AndresMozo1/secondHenry/assets/76072127/9a7c0ec6-016a-449d-a32a-665ecdc5a6f8" alt="imagen" />
<p>

Eston son los datos mas valiosos del proceso de [EDA.ipynb](https://github.com/AndresMozo1/secondHenry/blob/master/EDA.ipynb)

Los picos en la accidentalidad por horas sugieren la necesidad de medidas preventivas específicas en momentos clave del día (AM).

<p align='center'>
  <img src="https://github.com/AndresMozo1/secondHenry/assets/76072127/c7912477-b444-4aca-8f2e-71e4aac03843" alt="imagen" />
<p>

La variación en la frecuencia de accidentes según el tipo de calles señala áreas que podrían requerir mejoras en la infraestructura vial.

<p allign='center'>
  <img src="https://github.com/AndresMozo1/secondHenry/assets/76072127/e52f80b5-8c16-4ab2-b7d1-a7c80e43a77b" alt="imagen" />
<p>

La distribución geográfica de la accidentalidad por comunas muestra disparidades significativas, destacando áreas que necesitan mayor atención en seguridad vial y programas educativos, empezando por la

<p allign='center'>
  <img src="https://github.com/AndresMozo1/secondHenry/assets/76072127/86d0dda6-3245-4b5f-9022-d0127428b7da" alt="imagen" />
<p>

Los patrones diferenciales en las víctimas y responsables, así como en los rangos de edad, resaltan la importancia de abordar los factores de riesgo asociados con mayor precisión.

<p allign='center'>
  <img src="https://github.com/AndresMozo1/secondHenry/assets/76072127/7c5dd3fc-79e9-4164-9667-d62639c40639" alt="imagen" />
<p>

Estos hallazgos mw ofrecieron una base sólida para orientar estrategias de prevención de accidentes y mejorar la seguridad vial en áreas específicas, incluyendo la Avenida General Paz y las comunas 1, 4, 7 y 9, que muestran una mayor incidencia de accidentes y requieren intervenciones diferenciadas.

Como segundo paso desarrolle el proceso de Extraccion Transformacion y Carga de los datos [ETL.ipynb](https://github.com/AndresMozo1/secondHenry/blob/master/ETL.ipynb) Aqui obtuve datos de una [fuente oficial](https://www.indec.gob.ar/indec/web/Nivel4-Tema-2-41-165)  los trate y unifique para empezar a perfilar los datos en busqueda de los dos KPIS previamente suministrados y un tercero que complementase a los primeros.

<p align='center'>
  <img src="https://github.com/AndresMozo1/secondHenry/assets/76072127/6dee670f-3511-41ce-b026-2a67bb0f4bef" alt="imagen" />
</p>

Como tercer paso cree una base de datos para una gestion eficiente de la informacion previamente tratada, para esto utilice el mapeador relacional de objetos [sqlalchemy](https://www.sqlalchemy.org/) para relacionar la base de datos creada con [sqlite3](https://www.sqlite.org/) para su posterior extraccion y finalmente su carga en formato de dataframe utilizando la libreria de [pandas](https://pandas.pydata.org/); este estack tecnologico brinda una infraestructura local y eficiente para administrar la informacion.

<p align='center'>
  <img src="https://github.com/AndresMozo1/secondHenry/assets/76072127/e69c59e3-41b9-4954-a682-50f042dadb02" alt="imagen" />
</p>

Sin duda alguna python como herramienta potentisima para cualquier tipo de tratamiento con los datos (junto a sus frameworks y librerias) empalma perfectamente con  un entorno de visualizacion igualmente potente e interactivo llamado [Streamlit](https://streamlit.io/), despues de leer parte de su documentacion, ver sus graficos, forma de crearlos y deplegarlos , tomo la decision de realizar transformaciones extras a los datos para crear graficos mas contundentes los cuales con filtros extras muestran informacion precisa, contundente y clara para analisis y toma de decisiones. [Streamlit](https://streamlit.io/).

<p align='center'>
  <img src="https://github.com/AndresMozo1/secondHenry/assets/76072127/16c87a22-12fe-433a-9a9c-a292185ed129" alt="imagen" />
</p>

<p align='center'>
  <img src="https://github.com/AndresMozo1/secondHenry/assets/76072127/38e6e450-d215-4a1a-af77-aee195b6b6c6" alt="imagen" />
</p>

<p align='center'>
  <img src="https://github.com/AndresMozo1/secondHenry/assets/76072127/57806263-497c-4efe-863e-56082537a4bb" alt="imagen" />
</p>
