import streamlit as st
import pandas as pd
import plotly.express as px
import copy
from chart_funcs import *
from helper_funcs import *
#bar_chart = __import__("chart_funcs").bar_chart


st.set_page_config(layout="wide")

config = {'scrollZoom': True, 'displaylogo': False, 'responsive':True,
          'editable': True,
          'toImageButtonOptions': {
             'format': 'png', # one of png, svg, jpeg, webp
             'filename': 'custom_image',
             'height': None,
             'width': None,
             'scale': 3 # Multiply title/legend/axis/canvas sizes by this factor
  }}


def main():
	''' Esta plantilla busca que sea posible graficar la información de cualquier archivo que cumpla las condiciones:
		- Tiene una fila por cada registro
		- Ya se hizo limpieza de la información
		- Todos los valores están escritos TAL CUAL se desean presentar (variables, títulos y respuestas)
		- Respuestas del tipo (1: En desacuerdo, 6: De acuerdo) ya deben estar en formato texto
		- Las columnas 0:col_preguntas contienen información referente a cada individuo
		- Las columnas col_preguntas:(hasta el final) contienen información a graficar
	'''

	st.write("""# Plantilla Visualizaciones""")

	#La línea de abajo es una opción para cargar un archivo desde el computador
	#file = st.file_uploader('File uploader')

	#Nombre del archivo con los datos
	file = "Ejemplo2020.xlsx"
	#Nombre de la columna cuyos datos son únicos para cada respuesta
	columna_unica = 'Respuesta'
	#A partir de esta columna comienzan las preguntas (columnas de interés)
	col_preguntas = 11

	if file:
		datos = load_data(file)
		chart_type = st.radio("Tipo de visualización ",
							 ("Barras", "Dispersión", "Cajas"))

		pregunta, filtros_def, indices, lista_agrupadores = filtros(datos, col_preguntas)
		ejex, color, columna, fila = filtros_def
		height = st.slider("Ajuste el tamaño vertical de la gráfica", 500,1000)

		category_orders = categories_order(set(datos[pregunta]), pregunta)

		#Selecciona tipo de gráfica
		if chart_type == "Barras":
			""" Los diagramas de barra exigen agrupar la información antes de graficar """
			pivot = pivot_data(datos, indices, columna_unica)
			fig = bar_chart(columna_unica=columna_unica,
							pivot=pivot, ejex=ejex, color=color,
							fila=fila, columna=columna, indices=indices, category_orders=category_orders)
		elif chart_type == "Cajas":
			fig = box_chart(columna_unica=pregunta,
							pivot=datos, ejex=ejex, color=color,
							fila=fila, columna=columna, indices=indices, category_orders=category_orders)
			fig.update_yaxes(col=1, title=None)
		else:
			fig = scatter_chart(columna_unica=columna_unica,
							pivot=datos, ejex=ejex, color=color,
							fila=fila, columna=columna, lista_agrupadores=[pregunta]+lista_agrupadores,
							category_orders=category_orders)

		#Evita que los títulos de las subfiguras sean de forma VARIABLE=valor
		fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))

		fig.update_layout(height=height)

		st.plotly_chart(fig, use_container_width = True, config= config)

if __name__=="__main__":
	main()
