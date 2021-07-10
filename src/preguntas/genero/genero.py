import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np


path = "src/preguntas/genero/data/"
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
            data = zip(["min","q1","median","q3","max"],df[df[name] == t].quantile([0,0.25,0.5,0.75,1]).iloc[:,1].values)
        elif (size == 1):
            data = zip(["min","q1","median","q3","max"],df.quantile([0,0.25,0.5,0.75,1]).iloc[:,1].values)

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


# Graficas correo 1

def grafica1_repertorios():
    df = pd.read_csv(path+"Grafica_1_Genero_Repertorios.csv")
    boton = st.checkbox("Mostrar valores")
    fig = px.box(df, y="Valor", color="Tipo",
                 title="Repertorios Específicos de Nivel Avanzado en Pre y Postest", color_discrete_sequence=color)
    fig.update_layout(title_x=0.5, height=600) 
    if boton:
        box_plot_annotations(df,fig,"Tipo")
        
    st.plotly_chart(fig, use_container_width=True)

# Graficas correo 2

def grafica2_sexismonivelygenero():
    aux = pd.read_csv(path+"Grafica_2_Genero_Benevolente.csv")
    aux["Valor"] = aux["Valor"]/100
    fig = px.bar(aux, x="Nivel",
                 y="Valor",
                 color="Tipo de test",
                 barmode="group",
                 title="Sexismo Benevolente en Pretest y Postest discriminado por Nivel y Género",
                 labels=dict(Valor="Promedio"),
                 facet_col="Género",
                 color_discrete_sequence=color,
                 text="Valor")
    fig.update_layout(title_x=0.5, height=600)
    fig.update_traces(opacity=0.8)
    fig.for_each_annotation(lambda a: a.update(
        text=a.text.replace("Género=", "")))
    fig.update_traces(texttemplate='%{text:.2%}', textposition='outside')
    st.plotly_chart(fig, use_container_width=True)

def grafica21_seximobenevolbasico():
    boton = st.checkbox("Mostrar valores")
    aux_basico = pd.read_csv(path+"Grafica_21_Genero_Benevolente.csv")
    fig = px.box(aux_basico, y="Valor", color="Tipo de test",
                 title="Sexismo benevolente en Pretest y Postest para nivel básico", color_discrete_sequence=color)
    fig.update_layout(title_x=0.5, height=600)
    if boton:
        box_plot_annotations(aux_basico,fig,"Tipo de test")
    st.plotly_chart(fig, use_container_width=True)

def grafica22_seximobenevolavanzado():
    boton = st.checkbox("Mostrar valores")
    aux_avanzado = pd.read_csv(path+"Grafica_22_Genero_Benevolente.csv")
    fig = px.box(aux_avanzado, y="Valor", color="Tipo de test",
                 title="Sexismo benevolente en Pretest y Postest para nivel avanzado", color_discrete_sequence=color)
    fig.update_layout(title_x=0.5, height=600)
    if boton:
        box_plot_annotations(aux_avanzado,fig,"Tipo de test")
    st.plotly_chart(fig, use_container_width=True)

# Graficas correo 3

def grafica3_prejuicios():
    title = "Prejuicios STEM Generales por Género y Etnia en Postest"
    aux = pd.read_csv(path+"Grafica_3_Prejuicios.csv")
    aux["Promedio del Puntaje"] = aux["Promedio del Puntaje"]/100
    fig = px.bar(aux, y="Promedio del Puntaje", x="Genero", color="Etnia",
                 barmode="group", title=title, color_discrete_sequence=color,text="Promedio del Puntaje")
    fig.update_layout(title_x=0.5)
    fig.update_traces(texttemplate='%{text:.2%}', textposition='outside')
    st.plotly_chart(fig, use_container_width=True)

def grafica31_prejuicios():
    title = "Prejuicios STEM Generales por Género y Estrato Socioeconómico del Nivel Básico en Postest"
    aux = pd.read_csv(path+"Grafica_3-1_Prejuicios.csv")
    aux["Promedio del Puntaje"] = aux["Promedio del Puntaje"]/100
    fig = px.bar(aux, y="Promedio del Puntaje", x="Genero", color="Estrato",
                 barmode="group", title=title, color_discrete_sequence=color,
                 text="Promedio del Puntaje")
    fig.update_layout(title_x=0.5)
    fig.update_traces(texttemplate='%{text:.2%}', textposition='outside')
    st.plotly_chart(fig, use_container_width=True)


# Graficas correo 4

def grafica4_sociodemografica():
    aux = pd.read_csv(path+"Grafica_4_Sociodemografica.csv")
    fig = px.bar(aux, x="Respuesta", y="Porcentaje", color="Genero", barmode="group",
                 title="Hombres y mujeres cabeza de hogar", color_discrete_sequence=color,text="Porcentaje")
    fig.update_layout(title_x=0.5, height=600)
    fig.update_yaxes(tickformat="0.1%")
    fig.update_traces(texttemplate='%{text:.2%}', textposition='outside')
    st.plotly_chart(fig, use_container_width=True)

def grafica41_sociodemografica():
    title = "Número de materias de las y los profesores en primaria y bachillerato"
    aux = pd.read_csv(path+"Grafica_4-1_Sociodemografica.csv")
    fig = px.bar(aux, x="Grados", y="Porcentaje", color="Genero", barmode="group",
                 facet_col="Materia", title=title, color_discrete_sequence=color,text="Porcentaje")
    fig.update_layout(title_x=0.5, height=600)
    fig.update_xaxes(title='', visible=True, showticklabels=True)
    fig.for_each_annotation(lambda a: a.update(
        text=a.text.replace("Materia=", "")))
    fig.update_yaxes(tickformat="0.1%")
    fig.update_traces(texttemplate='%{text:.2%}', textposition='outside')
    st.plotly_chart(fig, use_container_width=True)

# Graficas correo 5

def grafica5_repertorios():
    title = "Número de Repertorios Generales en Postest de Nivel Baśico"
    aux = pd.read_csv(path+"Grafica_5_RepositoriosGenerales.csv")
    fig = px.bar(aux,
                 x="Repertorio",
                 color="Genero",
                 y="Promedio",
                 title=title,
                 barmode="group",
                 color_discrete_sequence=color,
                 labels=dict(Promedio="Porcentaje de Profesores(as) respecto al ǵenero", 
                 Repertorio="Número de Repertorios Generales reportados"),
                 text="Promedio")
    fig.update_layout(title_x=0.5, height=600)
    fig.update_yaxes(tickformat="0.1%")
    fig.update_traces(texttemplate='%{text:.2%}', textposition='outside')
    st.plotly_chart(fig, use_container_width=True)

def grafica51_repertorios():
    title = "Repertorios Generales por Género y Grupo Étnico en Nivel Básico de Postest"
    aux = pd.read_csv(path+"Grafica_5-1_RepositoriosGenerales.csv")
    fig = px.bar(aux, y="Promedio del Puntaje", x="Genero", color="Etnia",
                 barmode="group", title=title, color_discrete_sequence=color,
                 text="Promedio del Puntaje")
    fig.update_layout(title_x=0.5, height=600)
    fig.update_yaxes(tickformat="0.1%")
    fig.update_traces(texttemplate='%{text:.2%}', textposition='outside')
    st.plotly_chart(fig, use_container_width=True)

def grafica52_repertorios():
    title = "Repertorios Genearles por Estrato Socioeconómico en Nivel Básico de Postest"
    aux = pd.read_csv(path+"Grafica_5-2_RepositoriosGenerales.csv")
    fig = px.bar(aux, y="Promedio del Puntaje", x="Genero", color="Estrato",
                 barmode="group", title=title, color_discrete_sequence=color,
                 text="Promedio del Puntaje")
    fig.update_layout(title_x=0.5, height=600)
    fig.update_yaxes(tickformat="0.1%")
    fig.update_traces(texttemplate='%{text:.2%}', textposition='outside')
    st.plotly_chart(fig, use_container_width=True)

def grafica53_repertorios():
    boton = st.checkbox("Mostrar valores")
    title = "Repertorios Generales en Postest de Nivel Básico"
    aux = pd.read_csv(path+"Grafica_5-3_RepositoriosGenerales.csv")
    fig = px.box(aux, y="Puntaje", title=title, labels=dict(
        Puntaje="Puntaje de Repertorios Generales"), color_discrete_sequence=color)
    fig.update_layout(title_x=0.5, height=600)
    if boton: 
        box_plot_annotations(aux,fig,"")
    st.plotly_chart(fig, use_container_width=True)


q_list = [
    {
        "title": "Repertorios Específicos de Nivel Avanzado en Pre y Postest",
        "func": grafica1_repertorios
    },
    {
        "title": "Sexismo Benevolentes por Nivel y Género en Pre y Postest",
        "func": grafica2_sexismonivelygenero
    },
    {
        "title": "Sexismo benevolente en Pretest y Postest para nivel básico",
        "func": grafica21_seximobenevolbasico
    },
    {
        "title": "Sexismo benevolente en Pretest y Postest para nivel avanzado",
        "func": grafica22_seximobenevolavanzado
    },
    {
        "title": "Hombres y mujeres cabeza de hogar",
        "func": grafica4_sociodemografica
    },
    {
        "title": "Número de materias de las y los profesores en primaria y bachillerato",
        "func": grafica41_sociodemografica
    },
    {
        "title": "Prejuicios STEM Generales por Género y Etnia en Postest",
        "func": grafica3_prejuicios
    },
    {
        "title": "Prejuicios STEM Generales por Género y Estrato Socioeconómico del Nivel Básico en Postest",
        "func": grafica31_prejuicios
    },
    {
        "title": "Número de Repertorios Generales en Postest de Nivel Baśico",
        "func": grafica5_repertorios
    },
    {
        "title": "Repertorios Generales por Género y Grupo Étnico en Niivel Básico de Postest",
        "func": grafica51_repertorios
    },
    {
        "title": "Repertorios Genearles por Estrato Socioeconómico en Nivel Básico de Postest",
        "func": grafica52_repertorios
    },
    {
        "title": "Repertorios Generales en Postest de Nivel Básico",
        "func": grafica53_repertorios
    }
]


def app():
    st.write("# Gráficas del equipo de Género")
    grafica = st.selectbox("Seleccione una gráfica",
                           q_list, format_func=lambda i: i['title'])
    grafica["func"]()
