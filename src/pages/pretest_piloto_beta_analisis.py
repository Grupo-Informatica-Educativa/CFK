import streamlit as st
import numpy as np
from src.utils.chart_funcs import *
from src.utils.helper_funcs import *


def app():
	st.write("""# GreentTIC Análisis: Pretest piloto beta (Diagrama de barras)""")

	# Nombre del archivo con los datos
	file = "data/limpios/formularios_greentic_docentes.xlsx"
	# Nombre de la columna cuyos datos son únicos para cada respuesta
	columna_unica = 'Registro'
	# A partir de esta columna comienzan las preguntas (columnas de interés)
	col_preguntas = 9
	files = {
		"respuestas": {}
	}

	if file:
		datos = pd.read_excel(file, sheet_name='subhabilidades')

		# initialize list of lists
		columnas = list(datos.columns)
		arreglo_grafica_adicional = [
			'3. De los siguientes conceptos en computación, ¿Cuáles conoce y puede explicar? (marque todas las que apliquen)',
			'4. Califíquese segun el siguente criterio']

		indices_preguntas = [columnas.index(arreglo_grafica_adicional[0]), columnas.index(arreglo_grafica_adicional[1])]

		preguntas = np.concatenate((np.array(columnas[indices_preguntas[0]]), np.array(columnas[indices_preguntas[1]])),
								   axis=None)
		# Tabla de preguntas
		lista_preguntas = [str("Pregunta ") + preguntas[x].split(' ')[0][:-1] for x in range(len(preguntas))]
		preguntas_tabla = [' '.join(preguntas[x].split(' ')[1:]) for x in range(len(preguntas))]
		tabla_preguntas = np.stack((lista_preguntas, preguntas_tabla), axis=1)

		df_preguntas = pd.DataFrame(tabla_preguntas, columns=['Listado de preguntas', 'Pregunta'])
		expander = st.beta_expander("Tabla de las preguntas", expanded=False)
		with expander:
			st.table(df_preguntas)

		# OJO, se modificó el método filtros (TENER ESO EN CUENTA).
		pregunta, filtros_def, indices, lista_agrupadores, lista_cursos = filtros_tabla(datos, col_preguntas,
																						"Barras", files,
																						preguntas,True)

		ejex, color, columna, fila = filtros_def
		height = st.slider(
			"Ajuste el tamaño vertical de la gráfica", 500, 1000)

		"""if color == "Eficacia":
			datos = graph_answer(datos, pregunta, files)"""

		if lista_cursos != []:
			datos = datos.loc[datos.Curso.isin(lista_cursos)]

		category_orders = categories_order(set(datos[pregunta]), pregunta)

		numero_pregunta = pregunta.split()[0].split('.')[0]
		datos_2 = pd.read_excel(file, sheet_name='pregunta_{}'.format(numero_pregunta))
		arreglo_indices = ['Preguntas', 'Respuestas']
		if fila is not None:
			arreglo_indices.append(fila)
			fila_aux = fila
		else:
			fila_aux = None

		if columna is not None:
			arreglo_indices.append(columna)
			columna_aux = columna
		else:
			columna_aux = None
		tabla = pd.pivot_table(datos_2, values='Registro', index=list(set(arreglo_indices)), aggfunc='count').reset_index()
		tabla = tabla.sort_values(by=['Respuestas'], ascending=False)
		fig = bar_chart(columna_unica=columna_unica,
						pivot=tabla, ejex='Preguntas', color='Respuestas',
						fila=fila_aux, columna=columna_aux, indices=indices,
						category_orders=category_orders, color_discrete=px.colors.qualitative.Plotly,
						key='2')

		fig.update_layout(barmode='stack')
		fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
		fig.update_yaxes(col=1, title=None)
		fig.update_xaxes(row=1, title=None)

		fig.update_layout(height=height)
		st.plotly_chart(fig, use_container_width=True, config=config_chart)


