# project_7_repository

Repositorio de Proyecto 7. DS.

-- Herramientas de desarrollo de software. --

* Habilidades aprendidas en el Sprint:
Desarrollar e implementar una aplicación web en un servicio en la nube para que sea accesible al público.

* Bibliotecas utilizadas:
pandas,  streamlit,  plotly.express

* Planteamiento del problema y tarea:
Utilizando un conjunto de datos de anuncios de automóviles (vehicles_us.csv), se busca desarrollar e implementar una aplicación web en un servicio en la nube.

Para este proyecto, creé una aplicación Streamlit alojada en Render que permite a los usuarios interactuar con el conjunto de datos de anuncios de automóviles con el objetivo de obtener información sobre qué atributos de los automóviles pueden aumentar su valor en el mercado secundario.

El conjunto de datos de anuncios de autos contiene información sobre ventas de autos usados, como precio, año, modelo, estado del auto, número de cilindros, tipo de combustible, kilometraje, transmisión, color de la pintura, tracción en las cuatro ruedas, fecha de publicación y días de publicación.

Este proyecto busca descubrir información sobre los atributos que influyen en el precio y permite a los usuarios interactuar con los gráficos.

Se utilizó VS Code para escribir el código y desarrollar el repositorio del proyecto localmente. En cuanto a los métodos y bibliotecas utilizados en las pruebas locales, utilicé pandas, streamlit y plotly.express.

Primero, se leyó el archivo CSV y para convertirlo en un dataframe. Luego, realicé un análisis exploratorio de datos, limpié y transformé el conjunto de datos. Usando plotly.express, creé algunos gráficos para visualizar algunas tendencias dentro del conjunto de datos de anuncios de automóviles. Streamlit se utiliza como marco para mostrar todas las visualizaciones al implementarse como aplicación web o al realizar pruebas locales.

* Cómo ejecutar este proyecto localmente:
A medida que se añaden nuevos componentes de Streamlit para desarrollar la aplicación, se puede ejecutar el comando streamlit run app.py desde la terminal para ver el resultado.

Se hace preferiblemente desde la terminal del sistema para comprobar que todo funciona correctamente antes de confirmar y subir los cambios a este repositorio de GitHub.

Una vez compilado y ejecutado el proyecto localmente, se creó una cuenta en Render y la vinculé a este repositorio de GitHub. Dado que la compilación local se ejecutó sin errores y la estructura de carpetas era correcta, solo hay que realizar algunos cambios adicionales para implementar la aplicación en Render.

1: Se crea el archivo requirements.txt en la raíz de la carpeta del proyecto.

2: Se necesita agregar el archivo de configuración al repositorio de Git. Se crea el directorio .streamlit y se añade allí el archivo config.toml.  Este archivo de configuración le indicará a Render dónde buscar para "escuchar" la aplicación Streamlit al alojarla en sus servidores.

3: Se crear un nuevo servicio web vinculado a tu repositorio de GitHub:
Se configura el nuevo servicio web de Render. En el comando de compilación, se añade pip install --upgrade pip & pip install -r requirements.txt.
En el comando de inicio, se añade streamlit run app.py.

Se implementa en Render y hay que esperar a que la compilación se complete correctamente.

Se debe ver un enlace al sitio web de la aplicación y, si estos pasos se realizan correctamente, la aplicación Streamlit debería estar funcionando. A continuación, comparto el enlace de mi proyecto alojado en Render:

https://project-7-tvaz.onrender.com/
