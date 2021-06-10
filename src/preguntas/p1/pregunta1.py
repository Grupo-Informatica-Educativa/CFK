import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from plotly.colors import n_colors

'''
20. Cuando un estudiante se enfrenta a una dificultad creando un programa y no sabe si está correcto, qué tan a menudo, en una escala
de 1-10 (donde 10 es siempre), usted
'''


def app():
    st.write("Pregunta 1")
    datos = pd.read_excel("src/preguntas/p1/pregunta1.xlsx")
    datos = datos.drop("Unnamed: 0",axis=1)
    # Filtros
    
    # Get the columns
    preguntas = []

    preguntas.extend([x for x in datos.columns if x.startswith("20")])
    datos = datos[preguntas].dropna(axis=0,how='any')
    pivote = datos.apply(pd.value_counts).reset_index().drop("index",axis=1)
    pivote = pivote[:-1]
    st.write(pivote)
    fig = go.Figure()
    for index, col in enumerate(pivote.columns):
        fig.add_trace(go.Scatter(x=list(range(0,11)), y=np.full(11, (index*1000)),mode='lines',line_color='white'))
        fig.add_trace(go.Scatter(x=list(range(0,11)),y=pivote[col]+(index*1000),mode='lines',fill='tonexty',name=f'{col}'))
        fig.add_annotation(x=3,y=(index*1000),text=f'{col}',showarrow=False,yshift=30)
    fig.update_layout(title='Pregunta 20',showlegend=False,xaxis=dict(title='Preferencias'),yaxis=dict(showticklabels=False),width=1100,height=600)


    st.plotly_chart(fig, use_container_width=True)
    
    
    



# Dejare esta funcion para mostrar como se hizo el calculo sin embargo, se utilizaran datos ya cargados
'''
def calculo():
    datos = pd.read_excel("data/limpios/pretest_inicial.xlsx")
    columnas = [x for x in datos.columns if x.startswith("20") and len(x.split(' ')[0]) > 3]
    filtros = ['Nombre','Apellido','Curso','Cédula','Edad','Contexto IE','Género','Grupo Étnico','Estrato']
    datos = datos[filtros+columnas]
    datos.to_excel("Pregunta1.xlsx")
'''