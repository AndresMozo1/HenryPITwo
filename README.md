<h1 align='center'>
 <b>Análisis de Siniestralidad Vial en la Ciudad de Buenos Aires 2016 - 2021</b>
</h1>


![image](https://github.com/AndresMozo1/HenryPITwo/assets/76072127/86dffe8b-7292-498b-a6bd-8de169d2aefc)


<h2 align='center'>
 <b>Proyecto Individual de Data Analytics</b>
</h2>

[Wilmer Andrés Mozo Villamil DATA PT07](https://www.linkedin.com/in/wilmer-andr%C3%A9s-23097417b/)

![image](https://github.com/AndresMozo1/HenryPITwo/assets/76072127/dd841dbd-ec0a-40b8-9e30-18b04487582d)


Buenos Aires, una ciudad donde la historia y la modernidad se entrelazan en un vibrante tapiz cultural. Desde su fundación hasta el presente, la Ciudad Autónoma de Buenos Aires (CABA) ha sido testigo de un crecimiento constante y una rica diversidad de experiencias, con sus calles impregnadas de música, arte y gastronomía. Buenos Aires es un destino turístico de renombre mundial. Sus emblemáticos barrios, como San Telmo, La Boca y Palermo, ofrecen una variedad de atracciones que cautivan a visitantes de todas partes.

Sin embargo, como muchas otras ciudades, Buenos Aires enfrenta desafíos en materia de seguridad vial. Entre 2018 y 2022, se registraron más de 19,000 muertes por siniestros viales en toda Argentina (más de 700 en solo CABA), lo que destaca la necesidad urgente de medidas para proteger a los ciudadanos en las vías. Es en este contexto que se desarrolló un proyecto de análisis de datos con el objetivo de proporcionar información valiosa a las autoridades locales. Se exploraron patrones, se identificaron áreas críticas y se propusieron soluciones para mejorar la seguridad vial en la ciudad.

A través de este proyecto, se busca no solo analizar datos, sino también contribuir a la construcción de un futuro más seguro y próspero para los habitantes de Buenos Aires. Cada vida importa, y trabajar juntos nos permite crear un entorno más seguro para todos los ciudadanos.


![image](https://github.com/AndresMozo1/HenryPITwo/assets/76072127/2abfe21b-2fb5-4f3f-a882-79b6aa03865b)



Durante el primer contacto con los datos, [EDA.ipynb](https://github.com/AndresMozo1/HenryPITwo/blob/main/EDA.ipynb), me enfoqué en analizar la composición y el tamaño de los datasets recibidos, con el propósito de observar similitudes, unificar información y avanzar hacia la visualización de los datos. Se realizó un análisis exhaustivo columna por columna en busca de información relevante o duplicada, así como la verificación del formato de los datos, con el fin de tener un panorama claro para el desarrollo del proyecto.

Seguido, empecé a buscar insights que me permitieran entender un poco más las causas de la accidentalidad vial en CABA, las zonas con mayor incidencia, los actores viales, las franjas horarias y hasta los días de la semana con el fin de tener una visión amplia y precisa que permita crear un plan de acción a corto, mediano y largo plazo; mientras se realizaba este análisis exploratorio de los datos, se empezaron a hacer visibles diferentes patrones y tendencias, datos que se pudieron verificar con fuentes oficiales y en este punto identifiqué la necesidad de 'enriquecer' los datos; partiendo del hecho que el Sistema Nacional de Información Criminal (SNIC) define la tasa de homicidios en siniestros viales como el número de víctimas fatales en accidentes de tránsito por cada 100,000 habitantes en un área geográfica durante un período de tiempo específico.


![image](https://github.com/AndresMozo1/HenryPITwo/assets/76072127/5822c851-e69c-4760-b343-d2381f3f2790)


Estos son los datos más valiosos del proceso de [EDA.ipynb](https://github.com/AndresMozo1/HenryPITwo/blob/main/EDA.ipynb):

Los picos en la accidentalidad por horas sugieren la necesidad de medidas preventivas específicas en momentos clave del día (AM).

![image](https://github.com/AndresMozo1/HenryPITwo/assets/76072127/e919f62f-09e4-413a-b0b5-14fd40a096cf)


La variación en la frecuencia de accidentes según el tipo de calles señala áreas que podrían requerir mejoras en la infraestructura vial.

![image](https://github.com/AndresMozo1/HenryPITwo/assets/76072127/11e5ef56-82e9-4bb3-8058-50af3130587c)



La distribución geográfica de la accidentalidad por comunas muestra disparidades significativas, destacando áreas que necesitan mayor atención en seguridad vial y programas educativos, empezando por la comuna 1 por su alta concentración de turistas y zonas de interés.

![image](https://github.com/AndresMozo1/HenryPITwo/assets/76072127/715b1b3c-45ca-43a9-b7d9-4b293e97a290)



Los patrones diferenciales en las víctimas y responsables, así como en los rangos de edad, resaltan la importancia de abordar los factores de riesgo asociados con mayor precisión.


![image](https://github.com/AndresMozo1/HenryPITwo/assets/76072127/71e7c258-90b0-44d1-8a5b-46be1a143c2e)






Estos hallazgos me ofrecieron una base sólida para orientar estrategias de prevención de accidentes y mejorar la seguridad vial en áreas específicas, incluyendo la Avenida General Paz y las comunas 1, 4, 7 y 9, que muestran una mayor incidencia de accidentes y requieren intervenciones diferenciadas.





![image](https://github.com/AndresMozo1/HenryPITwo/assets/76072127/449c01c4-8110-4845-afb7-2aec583cda37)




Como segundo paso desarrollé el proceso de Extracción Transformación y Carga de los datos [ETL.ipynb](https://github.com/AndresMozo1/HenryPITwo/blob/main/ETL.ipynb). Aquí obtuve datos de una [fuente oficial](https://www.indec.gob.ar/indec/web/Nivel4-Tema-2-41-165), los traté y unifiqué para empezar a perfilar los datos en búsqueda de los dos KPIs previamente suministrados y un tercero que complementase a los primeros.

<p align='center'>
  <img src="https://github.com/AndresMozo1/HenryPITwo/assets/76072127/3184ca12-4904-4845-9a73-62e1ad2d263e" alt="imagen" />
</p>




Como tercer paso, creé una base de datos para una gestión eficiente de la información previamente tratada, para esto utilicé el mapeador relacional de objetos [sqlalchemy](https://www.sqlalchemy.org/) para relacionar la base de datos creada con [sqlite3](https://www.sqlite.org/) para su posterior extracción y finalmente su carga en formato de dataframe utilizando la librería de [pandas](https://pandas.pydata.org/); este stack tecnológico brinda una infraestructura local y eficiente para administrar la información.



![image](https://github.com/AndresMozo1/HenryPITwo/assets/76072127/3711db08-5522-4e4f-a913-c80ede01a028)


Sin duda alguna, Python como herramienta potente para cualquier tipo de tratamiento con los datos (junto a sus frameworks y librerías) encaja perfectamente con un entorno de visualización igualmente potente e interactivo llamado [Streamlit](https://streamlit.io/). Después de leer parte de su documentación, ver sus gráficos, forma de crearlos y desplegarlos, tomé la decisión de realizar transformaciones extras a los datos para crear gráficos más contundentes los cuales con filtros extras muestran información precisa y clara para análisis y toma de decisiones. [Mira el Dashboard aquí](https://dashboardconectedpy-duzhzatzufew739jdcn92m.streamlit.app/).

![image](https://github.com/AndresMozo1/HenryPITwo/assets/76072127/af2a63cb-1be0-42ff-97a0-bbf8c3689ee1)


![image](https://github.com/AndresMozo1/HenryPITwo/assets/76072127/531819af-647a-489a-90fb-93bf597b6cd8)


<h1 align='center'>
 <b>Índice de recursos </b>
</h1>

## Recursos internos

-[Análisis Exploratorio de Datos](https://github.com/AndresMozo1/HenryPITwo/blob/main/EDA.ipynb)<br>
-[Extracción Transformación y Carga](https://github.com/AndresMozo1/HenryPITwo/blob/main/ETL.ipynb)<br>
-[Data Frames](https://github.com/AndresMozo1/HenryPITwo/tree/main/DataFrames)<br>
-[Base de datos](https://github.com/AndresMozo1/HenryPITwo/tree/main/SQL)<br>
-[Imágenes](https://github.com/AndresMozo1/HenryPITwo/tree/main/Imagenes)

## Fuentes de datos 

- [INDEC Instituto Nacional de Estadística de la República Argentina](https://www.indec.gob.ar/indec/web/Nivel4-Tema-2-41-165)

## Tecnologías principales 

- [sqlite3](https://www.sqlite.org/)
- [sqlalchemy](https://www.sqlalchemy.org/)
- [pandas](https://pandas.pydata.org/)
- [Streamlit](https://streamlit.io/)

## Contacto 
- [LinkedIn](https://www.linkedin.com/in/wilmer-andr%C3%A9s-23097417b/)<br>
- Correo electrónico: wmandres@gmail.com
