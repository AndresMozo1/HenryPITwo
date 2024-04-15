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

Sin embargo, como muchas otras ciudades, Buenos Aires enfrenta desafíos en materia de seguridad vial. Entre 2018 y 2022, se registraron más de 19,000 muertes por siniestros viales en toda Argentina (más de 700 en solo CABA), lo que destaca la necesidad urgente de medidas para proteger a los ciudadanos en las vías. Es en este contexto se desarrolló un proyecto de análisis de datos con el objetivo de proporcionar información valiosa a las autoridades locales. Se exploraron patrones, se identificaron áreas críticas y se propusieron soluciones para mejorar la seguridad vial en la ciudad.

A través de este proyecto, se busca no solo analizar datos, sino también contribuir a la construcción de un futuro más seguro y próspero para los habitantes de Buenos Aires. Cada vida importa, y trabajar juntos nos permite crear un entorno más seguro para todos los ciudadanos.


![image](https://github.com/AndresMozo1/HenryPITwo/assets/76072127/2abfe21b-2fb5-4f3f-a882-79b6aa03865b)



Durante el primer contacto con los datos, [EDA.ipynb](https://github.com/AndresMozo1/HenryPITwo/blob/main/EDA.ipynb), me enfoqué en analizar la composición y el tamaño de los datasets recibidos, con el propósito de observar similitudes, unificar información y avanzar hacia la visualización de los datos. Se realizó un análisis exhaustivo columna por columna en busca de información relevante o duplicada, así como la verificación del formato de los datos, con el fin de tener un panorama claro para el desarrollo del proyecto.

Paso seguido, empecé a buscar insights que me permitieran entender un poco más las causas de la accidentalidad vial en CABA, las zonas con mayor incidencia, los actores viales, las franjas horarias y hasta los días de la semana con el fin de tener una visión amplia y precisa que permita crear un plan de acción a corto, mediano y largo plazo; mientras se realizaba este análisis exploratorio de los datos, se empezaron a hacer visibles diferentes patrones y tendencias, datos que se pudieron verificar con fuentes oficiales y en este punto identifiqué la necesidad de 'enriquecer' los datos; partiendo del hecho que el Sistema Nacional de Información Criminal (SNIC) define la tasa de homicidios en siniestros viales como el número de víctimas fatales en accidentes de tránsito por cada 100,000 habitantes en un área geográfica durante un período de tiempo específico.


![image](https://github.com/AndresMozo1/HenryPITwo/assets/76072127/5822c851-e69c-4760-b343-d2381f3f2790)


Estos son los datos más valiosos del proceso de [EDA.ipynb](https://github.com/AndresMozo1/HenryPITwo/blob/main/EDA.ipynb):

Los picos en la accidentalidad por horas sugieren la necesidad de medidas preventivas específicas en momentos clave del día (AM), pues durante esta franja se han reportado mas de 160 accidentes en el preriodo 2016/2021 de los cuales solamente las comunas 1 y 8 aportan más de 50 siniestros con victimas mortales. Otras comunas que deben tener una vigilancia y control diferencial son las comunas 4, 9 y 14 , las tres tienen una paridad de accidentalidad de 15 accidentes cada una en el mismo periodo de tiempo.

![image](https://github.com/AndresMozo1/HenryPITwo/assets/76072127/e919f62f-09e4-413a-b0b5-14fd40a096cf)


La variación en la frecuencia de accidentes según el tipo de calles señala áreas que podrían requerir mejoras en la infraestructura vial, especificamente la Avenida General Paz siendo una autopista de 24,3 km de extensión en la Ciudad Autónoma de Buenos Aires, Argentina. Es utilizada mayoritariamente como vía de acceso a la Ciudad de Buenos Aires por los habitantes de la zona norte y oeste del Gran Buenos Aires. Aporta la misma cantidad de accidentes que todas las demás autopistas juntas, razón por la cual decidí mantenerla diferenciada en este punto del analisis; la principal conclusión es que en las avenidas es donde más víctimas fatales se están presentando, es necesario revisar el estado de las avenidas, la velocidad máxima permitida, la cantidad de puentes, la cantidad de semáforos, entre otros factores, para identificar puntos de mejora con más detalle.

![image](https://github.com/AndresMozo1/HenryPITwo/assets/76072127/11e5ef56-82e9-4bb3-8058-50af3130587c)



La distribución geográfica de la accidentalidad por comunas muestra disparidades significativas, destacando áreas que necesitan mayor atención en seguridad vial y programas educativos, empezando por la comuna 1 por su alta concentración de turistas y zonas de interés , toda la zona que comprende BUENOS AIRES CENTRAL BUSSINES , el teatro colon , la avenida Santa Fé , MONSERRAT entre otros ,   la comuna 8 por sus parques, instituciones educativas, centros de salud, cuya linea principal de acceso con mayor accidentalidad es la AV GRAL PAZ , entre la AV 27 de febrero y la AV Castañares.

![image](https://github.com/AndresMozo1/HenryPITwo/assets/76072127/715b1b3c-45ca-43a9-b7d9-4b293e97a290)



Los patrones diferenciales en las víctimas y responsables, así como en los rangos de edad, resaltan la importancia de abordar los factores de riesgo asociados con mayor precisión. El dato mas revelador es que el rango de edad de 21 a 40 años es el que más víctimas fatales aporta, con alrededor de 350 personas, seguido del rango de 41 a 60 años, con alrededor de 210 víctimas. Entre los 21 y los 60 años, estos rangos de edad aportan el 70% del total de las víctimas fatales, demostrando que la imprudencia no diferencia edades.


![image](https://github.com/AndresMozo1/HenryPITwo/assets/76072127/71e7c258-90b0-44d1-8a5b-46be1a143c2e)






Estos hallazgos me ofrecieron una base sólida para orientar estrategias de prevención de accidentes y mejorar la seguridad vial en áreas específicas, incluyendo la Avenida General Paz y las comunas 1, 4, 8 y 9, que muestran una mayor incidencia de accidentes y requieren intervenciones diferenciadas en los lugares previamente mecionados.





![image](https://github.com/AndresMozo1/HenryPITwo/assets/76072127/449c01c4-8110-4845-afb7-2aec583cda37)




Como segundo paso, y teniendo presente la necesidad de obtener datos poblacionales que me dieran puntos de referencia para los indicadores clave de rendimiento (KPI), desarrollé el proceso de Extracción Transformación y Carga de los datos [ETL.ipynb](https://github.com/AndresMozo1/HenryPITwo/blob/main/ETL.ipynb). Aquí obtuve datos de una [fuente oficial](https://www.indec.gob.ar/indec/web/Nivel4-Tema-2-41-165), los traté y unifiqué para empezar a perfilar los datos en búsqueda de los dos KPIs previamente suministrados y un tercero que complementase a los primeros. 

## Primer KPI 

Reducir en un 10% la tasa de homicidios en siniestros viales de los últimos seis meses en la Ciudad Autónoma de Buenos Aires (CABA), en comparación con la tasa del semestre anterior.teniendo en cuenta que el Sistema Nacional de Información Criminal (SNIC) define la tasa de homicidios en siniestros viales como el número de víctimas fatales en accidentes de tránsito por cada 100,000 habitantes en un área geográfica durante un período de tiempo específico. Su fórmula es: (Número de homicidios en siniestros viales / Población total) * 100,000.

## Segundo KPI 

Reducir en un 7% la cantidad de accidentes mortales de motociclistas en el último año en la Ciudad Autónoma de Buenos Aires (CABA), en comparación con el año anterior.

Se define la cantidad de accidentes mortales de motociclistas en siniestros viales como el número absoluto de accidentes fatales en los que estuvieron involucradas víctimas que viajaban en moto en un determinado periodo temporal. La fórmula para medir la evolución de los accidentes mortales con víctimas en moto es: (Número de accidentes mortales con víctimas en moto en el año anterior - Número de accidentes mortales con víctimas en moto en el año actual) / (Número de accidentes mortales con víctimas en moto en el año anterior) * 100.

## Tercer KPI 

Sin duda alguna, las motos y los peatones, los actores viales más desprotegidos, son los que más mueren. Deben ser los primeros objetivos en las campañas de concientización por esta razón despúes de haber planteado el KPI de reducción de accidentalidad en moto en un 7% , como tercer KPI propongo la reduccion de accidentalidad en peatones de un 10%  en el ultimo año . debido a la relación victima/victimario y su alta vulnerabilidad.

 


<p align='center'>
  <img src="https://github.com/AndresMozo1/HenryPITwo/assets/76072127/3184ca12-4904-4845-9a73-62e1ad2d263e" alt="imagen" />
</p>

## Creacion de la Base de Datos


Como tercer paso, creé una base de datos para una gestión eficiente de la información previamente tratada, para esto utilicé el mapeador relacional de objetos [sqlalchemy](https://www.sqlalchemy.org/) para relacionar la base de datos creada con [sqlite3](https://www.sqlite.org/) para su posterior extracción y finalmente su carga en formato de dataframe utilizando la librería de [pandas](https://pandas.pydata.org/); este stack tecnológico brinda una infraestructura local y eficiente para administrar la información.



![image](https://github.com/AndresMozo1/HenryPITwo/assets/76072127/3711db08-5522-4e4f-a913-c80ede01a028)


## Diseño del Tablero de Control

Python como herramienta potente para cualquier tipo de tratamiento con los datos (junto a sus frameworks y librerías) encaja perfectamente con un entorno de visualización igualmente potente e interactivo llamado [Streamlit](https://streamlit.io/). Después de leer parte de su documentación, ver sus gráficos, forma de crearlos y desplegarlos, tomé la decisión de realizar transformaciones extras a los datos para crear gráficos más contundentes los cuales con filtros extras muestran información precisa y clara para análisis y toma de decisiones. [Mira el Dashboard aquí](https://dashboardconectedpy-duzhzatzufew739jdcn92m.streamlit.app/).

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

- [INDEC Instituto Nacional de Estadística de la República Argentina](https://www.indec.gob.ar/indec/web/Nivel4-Tema-2-41-165) <br>
- [Buenos Aires Data](https://www.indec.gob.ar/indec/web/Nivel4-Tema-2-41-165)

## Tecnologías principales 

- [sqlite3](https://www.sqlite.org/)
- [sqlalchemy](https://www.sqlalchemy.org/)
- [pandas](https://pandas.pydata.org/)
- [Streamlit](https://streamlit.io/)

## Contacto 
- [LinkedIn](https://www.linkedin.com/in/wilmer-andr%C3%A9s-23097417b/)<br>
- Correo electrónico: wmandres@gmail.com
