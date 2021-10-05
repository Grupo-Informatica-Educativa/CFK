
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np


path = "src/preguntas/genero/data/Genero_Cohorte2.csv"
df = pd.read_csv(path)
var_demo = [{"col":"edad","name":"Edad"},{"name":"Género","col":"genero"},{"name":"Contexto","col":"contexto"},{"name":"Area Docente","col":"areadocente"}]
var_tipo = [{"col":"test","name":"Test"},{"col":"nivel","name":"Nivel"}]
vars_ = ["sb","r","stem"]


color = px.colors.qualitative.Pastel

def app():
    st.write("# Gráficas del equipo de Género")
    copy = df.copy()
    btn_demo = st.checkbox("Habilitar Sociodemográfico")    
    if btn_demo:
        demo = st.multiselect("Variable Sociodemografica",var_demo,format_func=lambda x: x["name"])
        st.write("Si no selecciona ningun se entiende que no quiere filtrar por variable demografica.")
        if demo != []:
            for col in demo:
                st.write(f"### {col['name']}")
                v = col["col"]
                demo_inc = st.multiselect("Elije las que quiere añadir",copy[col["col"]].unique(),key=v)
                copy = copy[copy[col["col"]].isin(demo_inc)]

    st.markdown("---")
    btn_test = st.checkbox("Habilitar Tipo de test")   
    if btn_test:
        test = st.multiselect("Variable Test",var_tipo,format_func=lambda x: x["name"])
        st.write("Si no selecciona ningun se entiende que no quiere filtrar por tipo de test.")
        if test != []:
            for col in test:
                st.write(f"### {col['name']}")
                test_inc = st.multiselect("Elije las que quiere añadir",copy[col["col"]].unique())
                copy = copy[copy[col["col"]].isin(test_inc)]

    st.markdown("---")
    var = st.selectbox("Seleccione la variable",vars_)
    fig = px.box(copy, y=var, title=f"Genero - {var}", color_discrete_sequence=color)
    fig.update_layout(title_x=0.5, height=600) 
    st.plotly_chart(fig, use_container_width=True)


