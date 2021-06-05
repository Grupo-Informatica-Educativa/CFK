import streamlit as st
import numpy as np
from src.utils.chart_funcs import *
from src.utils.helper_funcs import *


def app():
	st.write("""# Instrumento de Caracterización Previo al Pilotaje (Docentes)""")

	# Nombre del archivo con los datos
	file = "data/limpios/instrumento_caracterizacion_previo_pilotaje_docentes.xlsx"
	# Nombre de la columna cuyos datos son únicos para cada respuesta
	columna_unica = 'Registro'
	# A partir de esta columna comienzan las preguntas (columnas de interés)
	col_preguntas = 6

	if file:
		datos = pd.read_excel(file, sheet_name='Subhab18Mayo')

		# initialize list of lists
		columnas = list(datos.columns)
		arreglo_multi_respuesta = ['De los siguientes conceptos en computación, ¿Cuáles conoce y puede explicar? (marque todas las que apliquen)',
							 'La cafetería del colegio empacó almuerzos iguales para todos los estudiantes, menos los de Jorge ... Maritza usando el pensamiento computacional para encontrar su almuerzo? (marque todas las opciones que apliquen)',
							 'La institución educativa San Mateo decidió comprar un computador por estudiante para empezar este nuevo ... ¿Está Rosa desarrollando el pensamiento computacional de sus estudiantes? (marque todas las opciones que apliquen)']

		arreglo_prengutas = ['De los siguientes conceptos en computación, ¿Cuáles conoce y puede explicar? (marque todas las que apliquen)',
							 'Califíquese segun el siguente creiterio:  Soy capaz de explicar lo que es el pensamiento computacional',
							 'La cafetería del colegio empacó almuerzos iguales para todos los estudiantes, menos los de Jorge ... Maritza usando el pensamiento computacional para encontrar su almuerzo? (marque todas las opciones que apliquen)',
							 'La institución educativa San Mateo decidió comprar un computador por estudiante para empezar este nuevo ... ¿Está Rosa desarrollando el pensamiento computacional de sus estudiantes? (marque todas las opciones que apliquen)',
							 'Ayuda al robot verde a salir del laberinto utilizando uno de los conjuntos de instrucciones ... si por ejemplo dice que se repite 4 veces, en total se ejecutará 5 veces.'
							 ]

		indices_preguntas = [columnas.index(arreglo_prengutas[0]), columnas.index(arreglo_prengutas[1]),
							 columnas.index(arreglo_prengutas[2]), columnas.index(arreglo_prengutas[3]),
							 columnas.index(arreglo_prengutas[4])]

		# Esta arreglo de preguntas es necesario debido a que la idea es que el usuario no vea las columnas las cuales
		# segmentamos por respuestas y las convertimos en columnas
		preguntas = np.concatenate((np.array(columnas[col_preguntas:indices_preguntas[0]+1]),
									np.array(columnas[indices_preguntas[1]:indices_preguntas[2]+1]),
									np.array(columnas[indices_preguntas[3]]),
									np.array(columnas[indices_preguntas[4]:])), axis=None)
		# Tabla de preguntas
		lista_preguntas = [str("Pregunta ") + str(x + 1) for x in range(len(preguntas))]
		tabla_preguntas = np.stack((lista_preguntas, preguntas), axis=1)

		df_preguntas = pd.DataFrame(tabla_preguntas, columns=['Listado de preguntas', 'Pregunta'])
		expander = st.beta_expander("Tabla de las preguntas", expanded=True)
		with expander:
			st.table(df_preguntas)
		# Este diccionario es necesario para que el checkbox apunte a la respuesta de la BD
		diccionario_preguntas = {i + 1: list(preguntas)[i] for i in range(len(preguntas))}

		chart_type = st.radio("Tipo de visualización ",
							  ("Barras", "Dispersión", "Cajas"))

		# OJO, se modificó el método filtros (TENER ESO EN CUENTA).
		pregunta, filtros_def, indices, lista_agrupadores, lista_cursos = filtros(
			datos, col_preguntas, chart_type, True, diccionario_preguntas)

		ejex, color, columna, fila = filtros_def
		height = st.slider(
			"Ajuste el tamaño vertical de la gráfica", 500, 1000)

		if lista_cursos != []:
			datos = datos.loc[datos.Curso.isin(lista_cursos)]

		category_orders = categories_order(set(datos[pregunta]), pregunta)

		# Selecciona la respuesta que se desea analizar
		contador = 0
		for i in indices:
			if i in arreglo_multi_respuesta:
				if i == arreglo_multi_respuesta[0]:
					repeticiones = 11
					respuestas = np.array(columnas[indices_preguntas[0]+1:indices_preguntas[0] + repeticiones])
				elif i == arreglo_multi_respuesta[1]:
					repeticiones = 4
					respuestas = np.array(columnas[indices_preguntas[2]+1:indices_preguntas[2] + repeticiones])
				else:
					repeticiones = 5
					respuestas = np.array(columnas[indices_preguntas[3]+1:indices_preguntas[3] + repeticiones])
				indices_aux = st.selectbox("Seleccione la respuesta a analizar: ", respuestas)
				category_orders = categories_order(set(datos[pregunta]), indices_aux)
				ejex = indices_aux
				indices[contador] = indices_aux
			contador += 1

		# Se selecciona el tipo de grafica
		if chart_type == "Barras":
			""" Los diagramas de barra exigen agrupar la información antes de graficar """
			pivot = pivot_data(datos, indices, columna_unica)
			fig = bar_chart(columna_unica=columna_unica,
							pivot=pivot, ejex=ejex, color=color,
							fila=fila, columna=columna, indices=indices,
							category_orders=category_orders)
		elif chart_type == "Cajas":
			fig = box_chart(columna_unica=pregunta,
							pivot=datos, ejex=ejex, color=color,
							fila=fila, columna=columna, indices=indices)
			fig.update_yaxes(col=1, title=None)
		else:
			fig = scatter_chart(columna_unica=columna_unica,
								pivot=datos, ejex=ejex, color=color,
								fila=fila, columna=columna,
								lista_agrupadores=[pregunta] + lista_agrupadores,
								category_orders=category_orders)

		# Evita que los títulos de las subfiguras sean de forma VARIABLE=valor
		fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
		fig.update_yaxes(col=1, title=None)
		fig.update_xaxes(row=1, title=None)

		fig.update_layout(height=height)

		st.plotly_chart(fig, use_container_width=True, config=config_chart)

