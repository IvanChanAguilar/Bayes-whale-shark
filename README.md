#Análisis Bayesiano: Distribución del Tiburón Ballena (*Rhincodon typus*)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
![Data Science](https://img.shields.io/badge/Data_Science-FF6F00?style=for-the-badge&logo=jupyter&logoColor=white)

#Descripción del Proyecto
Este proyecto de Ciencia de Datos evalúa la probabilidad de presencia del tiburón ballena en dos zonas clave del Caribe Mexicano: la franja costera de Holbox y la zona marina real de agregación. 

El objetivo principal no solo fue calcular probabilidades, sino **auditar la representatividad de las bases de datos oficiales** (colecciones científicas) frente a la realidad ecológica observada en campo.

#El Dataset
* **Volumen:** +850,000 registros de ocurrencia de peces.
* **Fuentes:** SNIB-CONABIO y la red GBIF para México.
* **Variables clave:** Taxonomía (filtrado por *Rhincodon typus* y nombres comunes), Georreferencias (Latitud/Longitud).

#Stack Tecnológico y Metodología
1. ETL (Extracción, Transformación y Carga): Ingesta automatizada de múltiples archivos CSV utilizando la librería `glob`.
   * Manejo de excepciones y limpieza de datos espaciales masivos.
   * Serialización de datos en formato `.pkl` para optimizar tiempos de cómputo en la etapa de análisis.
2. **Filtrado Espacial (Bounding Boxes):**
   * Creación de variables categóricas espaciales mediante funciones `lambda` para segmentar los registros dentro de los polígonos de interés (costa vs. mar abierto).
3. **Modelado Estadístico:**
   * Aplicación del **Teorema de Bayes** para calcular la probabilidad condicionada de la presencia de la especie dado el cuadrante geográfico.
Resultados y Conclusiones: El Sesgo de los Datos Oficiales
* **Zona Costera (Holbox):** El modelo arrojó una probabilidad condicionada de presencia del **1.4%**.
* **Zona Marina de Agregación:** A pesar de ser el área donde la especie se congrega masivamente cada año, la probabilidad conjunta en la base de datos oficial fue de **0**.

**¿Qué significa este resultado?** Este "cero estadístico" comprobó matemáticamente un sesgo crítico de muestreo. Las bases de datos científicas tradicionales presentan un enorme vacío de información en mar abierto. 

**Próximos Pasos (Domain Knowledge):**
La solución a este vacío de datos existe en forma de "ciencia ciudadana". El siguiente paso evolutivo del proyecto es la digitalización y cruce de datos de las bitácoras físicas de los guías turísticos locales (quienes registran conteos exactos, tallas y geolocalización diaria) para crear un modelo de distribución verdaderamente representativo.

## Cómo ejecutar este proyecto
1. Clona este repositorio.
2. Asegúrate de tener instaladas las dependencias: `pip install pandas`.
3. Ejecuta el script principal `pecesss.py` (Nota: Requiere la base de datos local del SNIB en formato `.csv` o el archivo `.pkl` generado).
