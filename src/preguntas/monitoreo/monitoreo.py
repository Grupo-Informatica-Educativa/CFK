import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np


path = "src/preguntas/monitoreo/data/"
color = px.colors.qualitative.Pastel


def grafica1_cohorte_1():
    df1 = pd.read_csv(path+"Grafica_1.csv",sep=";")
    df1["Fecha"] = pd.to_datetime(df1["Fecha"],format='%d-%b')
    df1["Mes"] = df1["Fecha"].dt.strftime("%b")
    df1["Día"] = df1["Fecha"].dt.strftime("%d")
    df1["Día"] = pd.to_numeric(df1["Día"])
    df1['Fecha'] = df1['Fecha'] + pd.DateOffset(years=121)
    fig = px.line(df1,x="Fecha",y="Audencia",color="Mes",color_discrete_sequence=color,title="Alcance Página Facebook")
    fig.update_layout(title_x=0.5, height=600) 
    st.plotly_chart(fig, use_container_width=True)

def grafica2_cohorte_1():
    df2 = pd.read_csv(path+"Grafica_2.csv",sep=",")
    df2["Fecha"] = pd.to_datetime(df2["Fecha"],format='%b-%d')
    df2["Mes"] = df2["Fecha"].dt.strftime("%b")
    df2["Día"] = df2["Fecha"].dt.strftime("%d")
    df2["Día"] = pd.to_numeric(df2["Día"])
    df2['Fecha'] = df2['Fecha'] + pd.DateOffset(years=121)
    fig = px.line(df2,
              x="Fecha",
              y="Miembros totales",
              color="Mes",
              color_discrete_sequence=color,
              title="Crecimiento por días CAP")
    fig.update_layout(title_x=0.5, height=600) 
    st.plotly_chart(fig, use_container_width=True)
    
def grafica3_cohorte_1():
    df2 = pd.read_csv(path+"Grafica_2.csv",sep=",")
    df2["Fecha"] = pd.to_datetime(df2["Fecha"],format='%b-%d')
    df2["Mes"] = df2["Fecha"].dt.strftime("%b")
    df2["Día"] = df2["Fecha"].dt.strftime("%d")
    df2["Día"] = pd.to_numeric(df2["Día"])
    df2['Fecha'] = df2['Fecha'] + pd.DateOffset(years=121)
    fig = px.line(df2,
              x="Fecha",
              y="Miembros activos",
              color="Mes",
              color_discrete_sequence=color,
              title="Miembros Activos CAP",
              text="Miembros activos")
    fig.update_layout(title_x=0.5, height=600) 
    st.plotly_chart(fig, use_container_width=True)

def grafica4_cohorte_1():
    df3 = pd.read_csv(path+"Grafica_3.csv")
    df3 = df3.melt(["Mes","Día","Miembros activos"])
    df3.columns = ["Mes","Día","Miembros activos","Interaccion","Valor"]
    df3 = df3.groupby(["Mes","Interaccion"]).sum().reset_index()
    fig = px.bar(df3,
             x="Valor",
             y="Mes",
             color="Interaccion",
             barmode="stack",
             color_discrete_sequence=color,
             title="Interacciones CAP",
             text="Valor")
    fig.update_layout(title_x=0.5, height=600) 
    st.plotly_chart(fig, use_container_width=True)

def grafica5_cohorte_1():
    df4 = pd.read_csv(path+"Grafica_4.csv")
    df4 = df4.melt(["Edad"])
    df4.columns = ["Edad","Sexo","Valor"]
    fig = px.bar(df4,
             x="Valor",
             y="Edad",
             color="Sexo",
             barmode="stack",
             color_discrete_sequence=color,
             title="Likes Página Facebook",
             text="Valor")
    fig.update_layout(title_x=0.5, height=600) 
    fig.update_xaxes(tickformat="0.1%")
    fig.update_traces(texttemplate='%{text:.2%}', textposition='inside')
    st.plotly_chart(fig, use_container_width=True)

def grafica6_cohorte_1():
    labels = {
        1: "Personas y experiencias destacadas e inspiradoras",
        2: "Temas transversales de formación",
        3: "Fichas didácticas",
        4: "Minichallenges",
        5: "Recursos alternativos",
        6: "Divulgación y comunicación",
        7: "Encuentros educativos "
    }
    df5 = pd.read_csv(path+"Grafica_5.csv")
    df5 = df5.replace({"Línea Temática": labels})
    df5 = df5.melt(["Línea Temática","Mes"])
    df5.columns = ["Línea Temática","Mes","Reacción","Valor"]
    df5 = df5[df5["Reacción"] !=  "Alcance"]
    df5 = df5.groupby(["Línea Temática","Reacción"]).sum().reset_index()
    fig = px.bar(df5,
             x="Reacción",
             y="Valor",
             color="Línea Temática",
             color_discrete_sequence=color,
             title="Reacción Por tipo de Post",
             barmode="group")
    fig.update_layout(title_x=0.5, height=600) 
    st.plotly_chart(fig, use_container_width=True)

def grafica7_cohorte_1():
    labels = {
        1: "Personas y experiencias destacadas e inspiradoras",
        2: "Temas transversales de formación",
        3: "Fichas didácticas",
        4: "Minichallenges",
        5: "Recursos alternativos",
        6: "Divulgación y comunicación",
        7: "Encuentros educativos "
    }
    df6 = pd.read_csv(path+"Grafica_5.csv")
    df6 = df6.replace({"Línea Temática": labels})
    df6 = df6.melt(["Línea Temática","Mes"])
    df6.columns = ["Línea Temática","Mes","Reacción","Valor"]
    df6 = df6.groupby(["Línea Temática"]).sum().reset_index()
    fig = px.bar(df6,
             x="Valor",
             y="Línea Temática",
             color_discrete_sequence=color,
             title="Alcance por tipo de post",
             text="Valor")
    fig.update_layout(title_x=0.5, height=600) 
    st.plotly_chart(fig, use_container_width=True)

def grafica8_cohorte_1():
    df8 = pd.read_csv("DataMonitoreo/Grafica_6.csv")
    df6 = df6.replace({"Línea Temática": labels})
    df6 = df6.melt(["Línea Temática","Mes"])
    df6.columns = ["Línea Temática","Mes","Reacción","Valor"]
    df6 = df6.groupby(["Línea Temática"]).sum().reset_index()
    fig = px.bar(df6,
             x="Valor",
             y="Línea Temática",
             color_discrete_sequence=color,
             title="Alcance por tipo de post",
             text="Valor")
    fig.update_layout(title_x=0.5, height=600) 
    st.plotly_chart(fig, use_container_width=True)

def grafica9_cohorte_1():
    df9 = pd.read_csv(path+"Grafica_7.csv")
    df9 = df9.sort_values("Linea",ascending=False)
    fig = px.bar(df9,
             x="Valor",
             y="Linea",
             color_discrete_sequence=color,
             title="Cumplimiento de actividades CAP",
             color="Tipo",
             barmode="group",
             text="Valor")
    fig.update_layout(title_x=0.5, height=600)  
    st.plotly_chart(fig, use_container_width=True)

q_list = [
    {
        "title": "Alcance Página Facebook",
        "func": grafica1_cohorte_1
    },
    {
        "title": "Crecimiento por días CAP",
        "func": grafica2_cohorte_1
    },
    {
        "title": "Miembros Activos CAP",
        "func": grafica3_cohorte_1
    },
    {
        "title": "Interacciones CAP",
        "func": grafica4_cohorte_1
    },
    {
        "title": "Likes Página Facebook",
        "func": grafica5_cohorte_1
    },
    {
        "title": "Reacción Por tipo de Post",
        "func": grafica6_cohorte_1
    },
    {
        "title": "Alcance por tipo de post",
        "func": grafica7_cohorte_1
    },
    {
        "title": "Cumplimiento actividades por líneas tematicas",
        "func": grafica9_cohorte_1
    },
   
]

'''
{
    "title": "Cumplimiento de actividades CAP",
    "func": grafica8_cohorte_1
},
'''

def app():
    st.write("# Gráficas del equipo de Monitoreo")
    q_list_sorted = sorted(q_list, key=lambda k: k['title']) 
    grafica = st.selectbox("Seleccione una gráfica",
                           q_list_sorted, format_func=lambda i: i['title'])
    grafica["func"]()
