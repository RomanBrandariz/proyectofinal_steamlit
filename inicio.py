import streamlit as st
import pandas as pd



# Insertar la imagen con el ancho calculado en píxeles
st.image("logo.png", width=200)



ruta_archivo ='datosparastreamlit.csv'
df = pd.read_csv(ruta_archivo)
st.title('Busqueda y Recomendación')
# Definir el diccionario de mapeo
estados = {
    'TX': 'Texas',
    'CA': 'California',
    'PA': 'Pennsylvania',
    'NY': 'New York',
    'FL': 'Florida'
}
if st.checkbox('Buscar Restaurant '):
    # Obtener la selección del usuario
    opcion_abreviada = st.radio('Estado', ('CA','PA','FL','NY','TX',), format_func=lambda x: estados[x], horizontal=True)
    # Obtener el nombre completo del estado seleccionado
    nombre_completo = estados[opcion_abreviada]
    df_estado_seleccionado = df[df['state'] == opcion_abreviada]
    # Obtener la lista de ciudades únicas para el estado seleccionado
    ciudades_estado_seleccionado = df_estado_seleccionado['city'].unique().tolist()
    ciudade = st.selectbox('Elija ciudad', ciudades_estado_seleccionado)
    #nombres = df[(df['estado'] == opcion_abreviada) & (df['ciudad'] == ciudade)]['name'].unique().tolist()
    nombres = df[(df['state'] == opcion_abreviada) & (df['city'] == ciudade)]['name'].tolist()
    nombres_formateados = [f"{nombre} - {indice}" for indice, nombre in enumerate(nombres)]
    nombres_seleccionados = st.selectbox('Elija local', nombres_formateados)
    
    # Obtener el índice seleccionado
    indice_seleccionado = nombres_formateados.index(nombres_seleccionados)
    
    # Obtener los datos del restaurante seleccionado
    datos_seleccionados = df_estado_seleccionado[df_estado_seleccionado['name'] == nombres[indice_seleccionado]]
    
    # Crear un nuevo DataFrame con los datos seleccionados
    seleccion = pd.DataFrame(datos_seleccionados)
    #st.map(seleccion)
    nombre = seleccion['name'].iloc[0]
    direccion = seleccion['address'].iloc[0]
    catagoria = seleccion['category'].iloc[0]
    estrellas = str(seleccion['avg_rating'].iloc[0])
    web = seleccion['url'].iloc[0]
    
    col1,col2 = st.columns(2)
    with col1:
        st.map(seleccion)
    with col2:
        st.write('Nombre Local :', nombre)
        st.write('Direccion :', direccion)
        st.write('Categoria :', catagoria)
        st.write('Valoracion :', estrellas)
        st.write('web :', web)
    if st.checkbox('Ver Recomendacion '):
        seleccion_id = seleccion['id_sitio'].iloc[0] + 1
        recomendacion = df[df['id_sitio'] == seleccion_id]

        nombrer = recomendacion['name'].iloc[0]
        direccionr = recomendacion['address'].iloc[0]
        catagoriar = recomendacion['category'].iloc[0]
        estrellasr = str(recomendacion['avg_rating'].iloc[0])
        webr = recomendacion['url'].iloc[0]
        col3,col4 = st.columns(2)
        with col3:
            st.write('Nombre Local :', nombrer)
            st.write('Direccion :', direccionr)
            st.write('Categoria :', catagoriar)
            st.write('Valoracion :', estrellasr)
            st.write('web :', webr)
        with col4:
            st.map(recomendacion.iloc[[0]])

if st.button('Busqueda Aleatoria'):
    # Selecciona un dato aleatorio del DataFrame
    dato = df.sample()    
    nombrea = dato['name'].iloc[0]
    direcciona = dato['address'].iloc[0]
    catagoriaa = dato['category'].iloc[0]
    estrellasa = str(dato['avg_rating'].iloc[0])
    weba = dato['url'].iloc[0]
    col5,col6 = st.columns(2)
    with col5:
        st.map(dato)
    with col6:
        st.write('Nombre Local :', nombrea)
        st.write('Direccion :', direcciona)
        st.write('Categoria :', catagoriaa)
        st.write('Valoracion :', estrellasa)
        st.write('web :', weba)