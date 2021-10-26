
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from src.utils.chart_funcs import *

color = px.colors.qualitative.Pastel

equipos = [
    {"name":"Equipo de Genero", "value":0},
    {"name":"Equipo de Visitas", "value":1},
]

paths = [
    "src/preguntas/genero/data/Insumos 2 Cohorte 2 Equipo de Género para actualización constructos.csv"
]

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


def filtros():
    df = pd.read_csv(paths[0], encoding="latin-1")

    var_demo = [{"col":"edad","name":"Edad"},{"name":"Género","col":"genero"},{"name":"Contexto","col":"contexto"},{"name":"Area Docente","col":"areadocente"}]
    var_tipo = [{"col":"test","name":"Test"},{"col":"nivel","name":"Nivel"}]
    

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

    return copy,btn_comparativa

def app_genero(copy,btn_comparativa):
    copy = copy[copy["nivel"] == "Avanzado"]
    vars_ = ["sb","r","stem","este"]
    st.markdown("---")
    var = st.selectbox("Seleccione la variable",vars_)
    title = st.text_input("Digite el título",value="Gráfica Género")
    y_text_value = st.text_input("Digite el valor de Y",value="Valor")

    if btn_comparativa:
        df_c = copy[["test",var]]
        fig = px.box(df_c, y=var, color="test",color_discrete_sequence=color,title=title)
        box_plot_annotations(df_c,fig,"test")
    else:
        df_c = copy[var]
        fig = px.box(copy, y=var, color_discrete_sequence=color,title=title)
        box_plot_annotations(df_c,fig,"x")
    fig.update_yaxes(title=y_text_value,showgrid=False)
    st.plotly_chart(fig, use_container_width=True)

def app_visitas(copy):
    copy = copy[copy["nivel"] == "Avanzado"]
    var = st.selectbox("Elija una variable",[{"name":"Repertorios","value": 0},{"name":"P40_X","value": 1}],format_func= lambda x: x["name"])["value"]
    isRelative = st.checkbox("Frencuencia Relativa")

    if var == 0:
        col = "r"
        copy = copy[col]
        
    
    else:
        col = ["p40_1", "p40_2","p40_3", "p40_4", "p40_5"]
        selected = st.multiselect("Elija las variables",col)
        copy = copy[selected]
        copy = copy.replace("--",0)
        copy = copy.melt()
        copy.columns = ["Variable","Cantidad"]
        copy["Cantidad"] = copy["Cantidad"].astype(int)
        copy = copy.groupby(["Variable"]).sum().reset_index()
        x = "Variable"
        y = "Cantidad"

    if isRelative:
        copy['Porcentaje'] = (copy["Cantidad"] / copy["Cantidad"].sum())*100
        y = "Porcentaje"
        
    title = st.text_input("Digite el título",value="Gráfica Género")
    y_text_value = st.text_input("Digite el valor de Y",value="Valor")

    fig = px.box(copy,color_discrete_sequence=color,title=title)
    box_plot_annotations(copy,fig,"x")

    if isRelative: 
        fig.update_yaxes(dict(ticksuffix=".0%"))
    fig.update_yaxes(title=y_text_value,showgrid=False)
    fig.update_layout(title_x=0.5, height=600) 
    st.plotly_chart(fig, use_container_width=True)

   

def app():
    st.write("# Gráficas del equipo de Género")
    opcion = st.radio("Elija el equipo",equipos,format_func=lambda x: x['name'])['value']
    copy,btn_comparativa = filtros()
    if opcion == 0:
        app_genero(copy,btn_comparativa )
    elif opcion == 1:
        app_visitas(copy)
    


