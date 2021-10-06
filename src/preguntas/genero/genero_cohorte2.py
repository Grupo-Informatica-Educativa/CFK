
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np


path = "src/preguntas/genero/data/Genero_Cohorte2.csv"
df = pd.read_csv(path, encoding="latin-1")
var_demo = [{"col":"edad","name":"Edad"},{"name":"Género","col":"genero"},{"name":"Contexto","col":"contexto"},{"name":"Area Docente","col":"areadocente"}]
var_tipo = [{"col":"test","name":"Test"},{"col":"nivel","name":"Nivel"}]
vars_ = ["sb","r","stem"]


color = px.colors.qualitative.Pastel


def box_plot_annotations(df,fig,name):
    colors = []
    tipo = []
    size = len(fig["data"])

    if(size == 2):
        x_pos = [-0.17,0.18]
    else:
        x_pos = [0]
    for val in fig["data"]:
        colors.append(val["marker"]["color"])
        tipo.append(val["legendgroup"])
    for i,t in enumerate(tipo):
        if (size == 2):
            data = zip(["min","q1","median","q3","max"],df[df[name] == t].quantile([0,0.25,0.5,0.75,1]).iloc[:,0].values)
        elif (size == 1):
            data = zip(["min","q1","median","q3","max"],df.quantile([0,0.25,0.5,0.75,1]).values)

        for y in data:
            fig.add_annotation(
                y=y[1],
                x=x_pos[i],
                text=y[0] + ": " + str(round(y[1],4)),
                showarrow=False,
                xref="x",
                yref="y",
                font=dict(
                    size=12,
                    color="#31333F"
                    ),
                align="center",
                ax=20,
                ay=-30,
                bordercolor="#c7c7c7",
                borderwidth=2,
                borderpad=4,
                bgcolor=colors[i],
                opacity=0.9
            )
    fig.update_layout(title_x=0.5, height=700)

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

    btn_comparativa = False
    if not btn_test:
        btn_comparativa = st.checkbox("Comparar Pretest con Postest")



    st.markdown("---")
    var = st.selectbox("Seleccione la variable",vars_)
    if btn_comparativa:
        df_c = copy[["test",var]]
        fig = px.box(df_c, y=var, title=f"Genero - {var}", color="test",color_discrete_sequence=color)
        box_plot_annotations(df_c,fig,"test")
    else:
        df_c = copy[var]
        fig = px.box(copy, y=var, title=f"Genero - {var}", color_discrete_sequence=color)
        box_plot_annotations(df_c,fig,"x")
    fig.update_layout(title_x=0.5, height=600) 
    st.plotly_chart(fig, use_container_width=True)


