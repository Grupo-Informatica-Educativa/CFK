import pandas as pd
import streamlit as st


# @st.cache
def load_data(file):
    return pd.read_excel(file)

filtros_dict = [
    "Grupo",
    "Monitor",
    "Mentor",
    "Edad",
    "Género",
    "Departamento",
    "Estrato",
    "Pertecene a etnia",
    "Etnia",
    "Nivel educativo",
    "Cargo",
    "Acceso a internet",
    "Modelo educativo actual",
    "Participó 2020",
    "Contexto IE",
    "¿Es usted cabeza de hogar?",
    "¿Es usted líder comunitario?"
]

def filtros(datos, col_preguntas, tipo_grafica,preguntas):
    lista_filtros = []

    # col_preguntas = int(st.number_input('Ingrese un número', 1,50,5))
    lista_preguntas = list(datos.iloc[:, col_preguntas:].columns)
    try:
        lista_comentarios = list(datos.filter(
            regex='omentario*', axis=1).columns)
    except:
        lista_comentarios = []

    lista_agrupadores = filtros_dict

    pregunta = st.selectbox("Seleccione la pregunta: ",
                            sorted(preguntas))
    
    numero = pregunta.split(' ')[0]
    respuestas_preguntas = [x for x in datos.columns if x.startswith(numero)]
    if len(respuestas_preguntas) > 1:
        respuesta = st.selectbox("Seleccione las respuestas",respuestas_preguntas[1:])
   

    try:
        cursos = datos.Grupo.unique()
        # st.write(cursos)
        cursos.sort()
        lista_cursos = st.multiselect(
            'Seleccione los cursos que desea visualizar', cursos)
    except:
        lista_cursos = []

    if tipo_grafica == 'Cajas' or tipo_grafica == 'Dispersión':
        lista_filtros.append(st.selectbox(
            "Seleccione el eje x", lista_agrupadores))
    else:
        lista_filtros.append(st.selectbox("Seleccione el eje x", [
            "Pregunta"] + lista_agrupadores))
  

    filtros_cols = st.beta_columns(3)

    cols = st.beta_columns(3)
    for index,col in enumerate(cols):
        with col:
            if index == 0:
                lista_filtros.append(st.selectbox("Dividir por color", [" ", "Pregunta"] + lista_agrupadores))
            elif index == 1:
                lista_filtros.append(st.selectbox("Dividir por columna", [" ", "Pregunta"] + lista_agrupadores))
            elif index == 2:
                lista_filtros.append(st.selectbox("Dividir por fila", [" ", "Pregunta"] + lista_agrupadores))

    filtros_def = [None if x == ' ' else x for x in lista_filtros]
    filtros_def = [respuesta if x == "Pregunta" else x for x in filtros_def]
    indices = list(set(filtros_def).difference([None]))

    return respuesta, filtros_def, indices, lista_agrupadores, lista_cursos#, respuestas


def pivot_data(datos, indices, columna_unica):
	return datos.pivot_table(index=indices,
							 values=columna_unica,
							 aggfunc="count").reset_index()
