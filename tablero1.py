import pandas as pd
import numpy as np  
import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout= 'centered', page_title= 'TALENTO TECH', page_icon= ':smile:')

#titulo pagina
t1, t2 = st.columns([0.3, 0.7])
t1.image('foto.jpeg', width=200)
t2.title('MI PRIMER TABLERO CON TALENTO TECH')
t2.markdown('**Tel:** 123 | **email:** manuela.gchica@udea.edu.co')

#secciones
#pestaña 1

steps= st.tabs(['Pestaña 1', 'Pestaña 2', 'Pestaña 3'])
with steps[0]:
    st.header('Graficos y Tablas')
    st.markdown('**Voy agregar mi primera tabla de datos**')
    st.write('Esta es una tabla de ejemplo con datos aleatorios:')
    st.image('grafico.avif', width=100)
    data= {'Nombre: ': ['Manuela', 'Juan', 'Pedro', 'Ana'], 'Fecha: ': ['2023-02-16', '2007-08-01', '1987-03-10', '2000-04-23'],
          'Edad: ': [23, 30, 25, 28]}
    df = pd.DataFrame(data)
    #st.table(df)
    st.dataframe(df) #este es lo mismo del renglon 24 (para imprimir la tabla)

with steps[0]:
    camp_df=pd.read_csv('Campanhas.csv', encoding='latin-1', sep=';')
    camp=st.selectbox('Escoger una Campanha:', camp_df['ID_Campana'], help='Selecciona una campaña para ver sus detalles')
    met_df=pd.read_csv('Metricas.csv', encoding='latin-1', sep=';') #encoding latin-1 para evitar problemas con caracteres especiales

    m1, m2, m3 = st.columns([1,1,1])

    id1 = met_df[(met_df['ID_Campana'] == camp)] #| (met_df['ID_Campana'] == 1)]
    id2 = met_df[(met_df['ID_Campana'] == camp)]
    m1.write('**Métrica filtradas:**')
   
    m1.metric(label='Métrica 1', value=sum(id1['Conversiones']), 
              delta=str(sum(id1['Rebotes'])) + 'Total de rebotes', 
              delta_color='inverse')
    m2.metric(label='Métrica 2', value=np.mean(id2['Clics']), 
              delta=str(np.mean(id2['Impresiones'])) + 'Total de rebotes', 
              delta_color='inverse')
    with steps[0]:
        varx=st.selectbox('Escoger ID Metrica: ', met_df['ID_Metrica'])
        vary=st.selectbox('Escoger numero de conversions: ', met_df['Conversiones'])
        fig, ax = plt.subplots()
        ax=sns.scatterplot(data=met_df, x=varx, y=vary, hue='ID_Campana')
        st.pyplot(fig)

#pestaña 2

with steps[1]:
    if st.button('Boton 1', key='Boton 1'):
        st.session_state['Boton 1_presionado']= True
    if st.session_state.get('Boton 1_presionado', False):
        st.write('El boton ha sido presionado')

with steps[1]:
    df= pd.read_csv('https://raw.githubusercontent.com/diplomado-bigdata-machinelearning-udea/Curso1/master/s03/dataVentas2009.csv')
    df.Fecha=pd.to_datetime(df.Fecha, format='%d/%m/%Y')
    df.set_index('Fecha', inplace=True)
    st.table(df)
    varx=st.selectbox('Escoja la variable x', df.columns)
    ax=sns.histplot(data=df, x=varx)
    st.pyplot(fig)


#pestaña 3
with steps[2]:
    st.selectbox('Selecciona una opción:', ['Opción 1', 'Opción 2', 'Opción 3'])
    st.slider('Selecciona un valor:', 0, 100, 50)
