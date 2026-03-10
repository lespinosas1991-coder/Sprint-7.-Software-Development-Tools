# project_7_repository

Repositorio de Proyecto 7. DS.

-- Herramientas de desarrollo de software. --

Habilidades aprendidas en el Sprint:

Desarrollar e implementar una aplicación web en un servicio en la nube para que sea accesible al público.

Bibliotecas utilizadas:
pandas,  streamlit,  plotly.express

Planteamiento del problema y tarea:

Utilizando un conjunto de datos de anuncios de automóviles (vehicles_us.csv), se busca desarrollar e implementar una aplicación web en un servicio en la nube.

Para este proyecto, creé una aplicación Streamlit alojada en Render que permite a los usuarios interactuar con el conjunto de datos de anuncios de automóviles para obtener información sobre qué atributos de los automóviles pueden aumentar su valor en el mercado secundario.

El conjunto de datos de anuncios de autos contiene información sobre ventas de autos usados, como precio, año del modelo, modelo, estado del auto, número de cilindros, tipo de combustible, kilometraje, tipo de transmisión, color de la pintura, tracción en las cuatro ruedas, fecha de publicación y días de publicación. Este proyecto busca descubrir información sobre los atributos que influyen en el precio y permite a los usuarios interactuar con los gráficos para descubrir sus propios hallazgos.

Se utilizó Vs Code para escribir el código y desarrollar el repositorio del proyecto localmente. En cuanto a los métodos y bibliotecas utilizados en las pruebas locales, utilicé pandas, streamlit y plotly.express.

Primero, se leyó el archivo CSV y para convertirlo en un dataframe. Luego, realicé un análisis exploratorio de datos ligero y limpié y transformé el conjunto de datos. Usando plotly.express, creé algunos gráficos para visualizar algunas tendencias dentro del conjunto de datos de anuncios de coches. Streamlit se utiliza como marco para mostrar todas las visualizaciones al implementarse como aplicación web o al realizar pruebas locales.

Una vez compilado y ejecutado el proyecto localmente, creé una cuenta en Render y la vinculé a mi repositorio de GitHub. Dado que la compilación local se ejecutó sin errores y la estructura de carpetas era correcta, solo hay que realizar algunos cambios adicionales para implementar la aplicación en Render.

1: se crea el archivo requirements.txt en la raíz de la carpeta del proyecto.

2: necesitamos agregar el archivo de configuración a su repositorio de Git. Crea el directorio .streamlit y añade allí el archivo config.toml (puedes hacerlo con el menú contextual en la pestaña izquierda de VS Code). Este archivo de configuración le indicará a Render dónde buscar para escuchar tu aplicación Streamlit al alojarla en sus servidores.

3. Crear un nuevo servicio web vinculado a tu repositorio de GitHub:
Configuramos el nuevo servicio web de Render. En el comando de compilación, añade pip install streamlit y pip install -r requirements.txt.
En el comando de inicio, añade streamlit run app.py.

Implementa en Render y espera a que la compilación se complete correctamente.

Deberías ver un enlace a tu sitio web y, si estos pasos se realizan correctamente, tu aplicación Streamlit debería estar funcionando.

Cómo ejecutar este proyecto localmente:

Si te interesa ejecutar este proyecto localmente en tu propio equipo, sigue los pasos que se indican a continuación:

Clonar este repositorio y almacenarlo localmente.

A medida que añades nuevos componentes de Streamlit para desarrollar tu aplicación, puedes ejecutar el comando streamlit run app.py desde la terminal para ver el resultado.

Hazlo en tu equipo local (preferiblemente desde una terminal del sistema) para comprobar que todo funciona correctamente antes de confirmar y subir los cambios a tu repositorio de GitHub, si así lo deseas.

Después de ejecutar streamlit run app.py, deberías poder acceder a tu implementación de prueba local mediante el puerto http://0.0.0.0:10000.
Si la ejecución es correcta, deberías ver tu aplicación en Streamlit. Sin embargo, si no, verás un mensaje que indica la posible causa de una compilación fallida. Corrige el error, guarda y vuelve a ejecutar el comando.
