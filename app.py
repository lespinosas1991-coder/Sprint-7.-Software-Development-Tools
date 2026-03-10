# Importar Librerías:
 
import pandas as pd 
import streamlit as st
import plotly.express as px
import os 

st.subheader('Análisis de anuncios de automóviles x LCES.')
st.write("Usando un conjunto de datos de anuncios de automóviles, se crearon dos gráficos a continuación que muestran cómo ciertos atributos impactan las ventas de autos usados.")

st.divider()

# Crea ruta variable a .csv:

path = os.path.dirname(__file__)
my_file = path+'/vehicles_us.csv'

# Lee archivo .csv:

vehicles = pd.read_csv(my_file)

# Reemplaza valores ausentes:

vehicles['model_year'].fillna(0, inplace=True)

vehicles['cylinders'] = vehicles['cylinders'].fillna(vehicles.groupby('type')['cylinders'].transform('median'))

vehicles['odometer'] = vehicles['odometer'].fillna(vehicles.groupby('type')['odometer'].transform('median'))

vehicles['paint_color'].fillna('Unknown', inplace=True)

vehicles['is_4wd'].fillna(0, inplace=True)

# Convierte los  tipos de datos:
vehicles['price'] = vehicles['price'].astype(float)
vehicles['model_year'] = vehicles['model_year'].astype('Int64')
vehicles['model'] = vehicles['model'].astype(str)
vehicles['condition'] = vehicles['condition'].astype(str)
vehicles['cylinders'] = vehicles['cylinders'].astype('Int64')
vehicles['fuel'] = vehicles['fuel'].astype(str)
vehicles['odometer'] = vehicles['odometer'].astype(float)
vehicles['transmission'] = vehicles['transmission'].astype(str)
vehicles['type'] = vehicles['type'].astype(str)
vehicles['paint_color'] = vehicles['paint_color'].astype(str)
vehicles['is_4wd'] = vehicles['is_4wd'].astype('Int64')
vehicles['date_posted'] = vehicles['date_posted'].astype('datetime64[ns]')
vehicles['days_listed'] = vehicles['days_listed'].astype('Int64')

# Crea un encabezado:

st.header("Cómo cada atributo afecta el precio de venta de un automóvil.")

# Crea un interruptor que permite al usuario ocultar o mostrar el gráfico de dispersión. El valor predeterminado del interruptor es "verdadero":

plot_one = st.toggle('Desactivar para ocultar el diagrama de dispersión.', value=True)

# Si el interruptor está configurado como verdadero, se muestra el diagrama de dispersión:

if plot_one:

    # Utilice el botón de opción para permitir que los usuarios elijan qué atributo desean utilizar para comparar con el precio:
    
    genre = st.radio("Elija qué atributo desea utilizar como eje X para comparar:"
                    , ["cylinders", "model_year", "condition"]
                    , index=0
                    , horizontal=True
                    )
    
    # Agregar control deslizante para ajustar la fecha y filtrar el año 0:

    values = st.slider(
        'Seleccione los años del modelo de interés',
        0, 2020, (0, 2020))

    # Cree un marco de datos de vehículos que filtre con el control deslizante del año del modelo:

    vehicles_filtered = vehicles[vehicles["model_year"].between(values[0], values[1])]

    # Configurar parámetros del diagrama de dispersión:
    fig_one = px.scatter(vehicles_filtered, x=genre, y="price", color = "condition", symbol="condition", hover_data=['model'], title= "Scatter plot of " + genre + " vs. price")
    
    # Imprime el diagrama de dispersión:

    st.plotly_chart(fig_one, theme="streamlit", use_container_width=True)

# Crea un interruptor que permite al usuario ocultar o mostrar el histograma. El valor predeterminado del interruptor es "verdadero":

plot_two = st.toggle('Desactivar el interrumptor para ocultar histograma', value=True)

# Si el interruptor está configurado como verdadero, se muestra el histograma:

if plot_two:

    # Utilice el cuadro de selección que permita que los usuarios elijan qué atributo desean utilizar como opción de color.
    # El histograma mostrará el recuento por año del modelo y opción de color.

    option = st.selectbox("Le gustaría ver el recuento de ventas de automóviles por año del modelo y..."
                         , ('type', 'paint_color', 'transmission', 'condition')
                         )
    
    # Agregar control deslizante para ajustar la fecha y filtrar el año 0:

    values_two = st.slider(
        'Seleccione los años del modelo de interés:',
        0, 2020, (0, 2020))

    # Cree un dataframe de vehículos que filtre con el control deslizante el año del modelo:

    vehicles_filtered = vehicles[vehicles["model_year"].between(values_two[0], values_two[1])]

    # Configurar parámetros del histograma:

    fig_two = px.histogram(vehicles_filtered, x="model_year", color= option, title= "Histograma de año del modelo vs. " + option)
    
    # Imprime HIstograma:
    
    st.plotly_chart(fig_two, theme="streamlit", use_container_width=True)
