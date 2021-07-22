import streamlit as st
import numpy as np
from src.utils.chart_funcs import *
from src.utils.helper_funcs import *


def app():
    st.write("""# GreenTIC: Pretest piloto beta""")

    # Nombre del archivo con los datos
    file = "data/limpios/formularios_greentic_docentes.xlsx"
    # Nombre de la columna cuyos datos son únicos para cada respuesta
    columna_unica = 'Registro'
    # A partir de esta columna comienzan las preguntas (columnas de interés)
    col_preguntas = 9
    files = {
        "respuestas": {
            "5": "Sí porque Maritza está dividiendo el problema en problemas más sencillos, Sí porque Maritza está usando un algoritmo para encontrar su almuerzo",
            "6": "Sí porque los estudiantes están aprendiendo a recolectar/organizar/analizar datos, Sí porque los estudiantes están aprendiendo sobre modelos computacionales para la predicción del clima",
            "8": "B",
            "9": "Alicia, Clara, Fanny, Bernardo, David, Eugenia, Henry y Gabriela",
            "10": "La botella C debe ser verde",
            "11": "C",
            "13": "Es una pequeña sección de código que realiza una tarea específica que puede o no recibir parámetros y retornar valores y puede ser utilizada varias veces dentro de un programa",
            "14": 5,
            "15": "La respuesta de Alejandra está equivocada. El valor final de Y es 120.",
            "16": "La segunda expresión es verdadera si (a O b) es verdadero",
            "17": "Primero la temperatura y luego una carita triste"
        }
    }

    if file:
        datos = pd.read_excel(file, sheet_name='subhabilidades')

        # initialize list of lists
        columnas = list(datos.columns)
        """arreglo_grafica_adicional = ['3. De los siguientes conceptos en computación, ¿Cuáles conoce y puede explicar? (marque todas las que apliquen)',
									 '4. Califíquese segun el siguente criterio']"""
        arreglo_multi_respuesta = [
            '3. De los siguientes conceptos en computación, ¿Cuáles conoce y puede explicar? (marque todas las que apliquen)',
            '4. Califíquese segun el siguente criterio',
            '5. La cafetería del colegio empacó almuerzos iguales para todos los estudiantes, menos los de ... Maritza usando el pensamiento computacional para encontrar su almuerzo? (marque todas las opciones que apliquen)',
            '6. La institución educativa San Mateo decidió comprar un computador por estudiante para empezar este ... ¿Está Rosa desarrollando el pensamiento computacional de sus estudiantes? (marque todas las opciones que apliquen)']

        arreglo_prengutas = [
            '3. De los siguientes conceptos en computación, ¿Cuáles conoce y puede explicar? (marque todas las que apliquen)',
            '4. Califíquese segun el siguente criterio',
            '4.10. Puedo utilizar la computación para resolver problemas simples',
            '5. La cafetería del colegio empacó almuerzos iguales para todos los estudiantes, menos los de ... Maritza usando el pensamiento computacional para encontrar su almuerzo? (marque todas las opciones que apliquen)',
            '6. La institución educativa San Mateo decidió comprar un computador por estudiante para empezar este ... ¿Está Rosa desarrollando el pensamiento computacional de sus estudiantes? (marque todas las opciones que apliquen)',
            '8. Ayuda al robot verde a salir del laberinto utilizando uno de los conjuntos de ... si por ejemplo dice que se repite 4 veces, en total se ejecutará 5 veces.'
        ]

        indices_preguntas = [columnas.index(arreglo_prengutas[0]), columnas.index(arreglo_prengutas[1]),
                             columnas.index(arreglo_prengutas[2]), columnas.index(
                                 arreglo_prengutas[3]),
                             columnas.index(arreglo_prengutas[4]), columnas.index(arreglo_prengutas[5])]

        # Este arreglo de preguntas es necesario debido a que la idea es que el usuario no vea las columnas las cuales
        # segmentamos por respuestas y las convertimos en columnas
        preguntas = np.concatenate((np.array(columnas[col_preguntas:indices_preguntas[0] + 1]),
                                    np.array(columnas[indices_preguntas[1]]),
                                    np.array(
                                        columnas[indices_preguntas[2]+1:indices_preguntas[3] + 1]),
                                    np.array(columnas[indices_preguntas[4]]),
                                    np.array(columnas[indices_preguntas[5]:])), axis=None)
        # Tabla de preguntas
        lista_preguntas = [str("Pregunta ") + preguntas[x].split(' ')[0][:-1]
                           for x in range(len(preguntas))]
        preguntas_tabla = [' '.join(preguntas[x].split(' ')[1:])
                           for x in range(len(preguntas))]
        tabla_preguntas = np.stack((lista_preguntas, preguntas_tabla), axis=1)

        df_preguntas = pd.DataFrame(tabla_preguntas, columns=[
                                    'Listado de preguntas', 'Pregunta'])
        expander = st.beta_expander("Tabla de las preguntas", expanded=False)
        with expander:
            st.table(df_preguntas)
        # Este diccionario es necesario para que el checkbox apunte a la respuesta de la BD

        chart_type = st.radio("Tipo de visualización ",
                              ("Barras", "Dispersión", "Cajas", "Tendencia"))

        # OJO, se modificó el método filtros (TENER ESO EN CUENTA).
        pregunta, filtros_def, indices, lista_agrupadores, lista_cursos = filtros_tabla(datos, col_preguntas,
                                                                                        chart_type, files,
                                                                                        preguntas)

        ejex, color, columna, fila = filtros_def
        height = st.slider(
            "Ajuste el tamaño vertical de la gráfica", 500, 1000)

        if color == "Eficacia":
            datos = graph_answer(datos, pregunta, files)
            # Con esto siempre el valor Correcto tendrá el primer color (El dorado) y el valor Incorrecto el azul
            datos = datos.sort_values(by=['Eficacia'], ascending=False)

        if lista_cursos != []:
            datos = datos.loc[datos.Curso.isin(lista_cursos)]

        category_orders = categories_order(set(datos[pregunta]), pregunta)

        # Selecciona la respuesta que se desea analizar
        contador = 0
        for i in indices:
            if i in arreglo_multi_respuesta:
                if i == arreglo_multi_respuesta[0]:
                    repeticiones = 12
                    respuestas = np.array(
                        columnas[indices_preguntas[0] + 1:indices_preguntas[0] + repeticiones])
                elif i == arreglo_multi_respuesta[1]:
                    repeticiones = 11
                    respuestas = np.array(
                        columnas[indices_preguntas[1] + 1:indices_preguntas[1] + repeticiones])
                elif i == arreglo_multi_respuesta[2]:
                    repeticiones = 6
                    respuestas = np.array(
                        columnas[indices_preguntas[3] + 1:indices_preguntas[3] + repeticiones])
                else:
                    repeticiones = 7
                    respuestas = np.array(
                        columnas[indices_preguntas[4] + 1:indices_preguntas[4] + repeticiones])
                indices_aux = st.selectbox(
                    "Seleccione la respuesta a analizar: ", respuestas)
                category_orders = categories_order(
                    set(datos[pregunta]), indices_aux)
                posicion_pregunta = np.where(
                    np.array(filtros_def) == pregunta)[0]
                for j in posicion_pregunta:
                    if j == 0:
                        ejex = indices_aux
                    if j == 1:
                        color = indices_aux
                    if j == 2:
                        columna = indices_aux
                    if j == 3:
                        fila = indices_aux
                indices[contador] = indices_aux
            contador += 1

        # Se selecciona el tipo de grafica
        if chart_type == "Barras":
            """ Los diagramas de barra exigen agrupar la información antes de graficar """
            pivot = pivot_data(datos, indices, columna_unica)

            if color == "Eficacia":
                pivot = pivot.sort_values(by=['Eficacia'], ascending=False)

            fig = bar_chart(columna_unica=columna_unica,
                            pivot=pivot, ejex=ejex, color=color,
                            fila=fila, columna=columna, indices=indices,
                            category_orders=category_orders)
        elif chart_type == "Cajas":
            fig = box_chart(columna_unica=pregunta,
                            pivot=datos, ejex=ejex, color=color,
                            fila=fila, columna=columna, indices=indices)
            fig.update_yaxes(col=1, title=None)
        elif chart_type == "Tendencia":
            fig = line_chart(columna_unica=columna_unica,
                             pivot=datos, ejex=ejex, color=color, indices=indices,
                             fila=fila, columna=columna,
                             lista_agrupadores=datos.columns.tolist(),
                             category_orders=category_orders)
        else:
            fig = scatter_chart(columna_unica=columna_unica,
                                pivot=datos, ejex=ejex, color=color,
                                fila=fila, columna=columna,
                                lista_agrupadores=datos.columns.tolist(),
                                category_orders=category_orders)

        # Evita que los títulos de las subfiguras sean de forma VARIABLE=valor
        fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
        fig.update_yaxes(col=1, title=None)
        fig.update_xaxes(row=1, title=None)

        fig.update_layout(height=height)

        st.plotly_chart(fig, use_container_width=True, config=config_chart)

        """if pregunta in arreglo_grafica_adicional:
			numero_pregunta = pregunta.split()[0].split('.')[0]
			if chart_type == "Barras":
				with st.beta_expander("Rendimiento general", expanded=False):
					datos_2 = pd.read_excel(file, sheet_name='pregunta_{}'.format(numero_pregunta))
					arreglo_indices = ['Preguntas', 'Respuestas']
					if fila is not None and fila not in respuestas:
						arreglo_indices.append(fila)
						fila_aux = fila
					else:
						fila_aux = None

					if columna is not None and columna not in respuestas:
						arreglo_indices.append(columna)
						columna_aux = columna
					else:
						columna_aux = None
					tabla = pd.pivot_table(datos_2, values='Registro', index=arreglo_indices,
										   aggfunc='count').reset_index()
					tabla = tabla.sort_values(by=['Respuestas'], ascending=False)
					fig_2 = bar_chart(columna_unica=columna_unica,
									pivot=tabla, ejex='Preguntas', color='Respuestas',
									fila=fila_aux, columna=columna_aux, indices=indices,
									category_orders=category_orders, color_discrete=px.colors.qualitative.Plotly,
									key='2')
					#fig_2 = absolute_bar_chart('Registro', tabla, 'Preguntas', 'Respuestas', fila_aux, columna_aux,
					#						   category_orders, px.colors.qualitative.Plotly)
					fig_2.update_layout(barmode='stack')
					fig_2.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
					fig_2.update_yaxes(col=1, title=None)
					fig_2.update_xaxes(row=1, title=None)

					fig_2.update_layout(height=height)
					st.plotly_chart(fig_2, use_container_width=True, config=config_chart)"""
