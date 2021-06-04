import pandas as pd
import streamlit as st


# @st.cache
def load_data(file):
    return pd.read_excel(file)


def filtros(datos, col_preguntas, tipo_grafica):
    lista_filtros = []

    # col_preguntas = int(st.number_input('Ingrese un número', 1,50,5))
    lista_preguntas = list(datos.iloc[:, col_preguntas:].columns)
    try:
        lista_comentarios = list(datos.filter(
            regex='omentario*', axis=1).columns)
    except:
        lista_comentarios = []

    preguntas_filtro = list(
        set(lista_preguntas).difference(set(lista_comentarios)))
    lista_agrupadores = list(datos.iloc[:, 1:col_preguntas].columns)

    pregunta = st.selectbox("Seleccione la pregunta: ",
                            sorted(preguntas_filtro))

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
    lista_filtros.append(st.selectbox("Dividir por color", [
                         " ", "Pregunta"] + lista_agrupadores))
    lista_filtros.append(st.selectbox("Dividir por columna", [
                         " ", "Pregunta"] + lista_agrupadores))
    lista_filtros.append(st.selectbox("Dividir por fila", [
                         " ", "Pregunta"] + lista_agrupadores))

    filtros_def = [None if x == ' ' else x for x in lista_filtros]
    filtros_def = [pregunta if x == "Pregunta" else x for x in filtros_def]
    indices = list(set(filtros_def).difference([None]))

    return pregunta, filtros_def, indices, lista_agrupadores, lista_cursos


def pivot_data(datos, indices, columna_unica):
    return datos.pivot_table(index=indices,
                             values=columna_unica,
                             aggfunc="count").reset_index()
