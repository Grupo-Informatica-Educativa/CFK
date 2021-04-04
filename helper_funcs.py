import pandas as pd
import streamlit as st

@st.cache
def load_data(file):
	return pd.read_excel(file)


def filtros(datos, col_preguntas):
	lista_filtros = []

	#col_preguntas = int(st.number_input('Ingrese un número', 1,50,5))
	lista_preguntas = list(datos.iloc[:,col_preguntas:].columns)
	lista_agrupadores = list(datos.iloc[:,1:col_preguntas].columns)

	pregunta = st.selectbox("Seleccione la pregunta: ", lista_preguntas)
	lista_filtros.append(st.selectbox("Seleccione el eje x", ["Pregunta"] +lista_agrupadores))
	lista_filtros.append(st.selectbox("Dividir por color", [" ", "Pregunta"] +lista_agrupadores))
	lista_filtros.append(st.selectbox("Dividir por columna", [" ", "Pregunta"] +lista_agrupadores))
	lista_filtros.append(st.selectbox("Dividir por fila",[" ", "Pregunta"] + lista_agrupadores))

	filtros_def = [None if x == ' ' else x for x in lista_filtros ]
	filtros_def = [pregunta if x == "Pregunta" else x for x in filtros_def ]
	indices = list(set(filtros_def).difference([None]))

	return pregunta, filtros_def, indices, lista_agrupadores

def pivot_data(datos, indices, columna_unica):
	return datos.pivot_table(index = indices,
							 values= columna_unica,
							 aggfunc="count").reset_index()
