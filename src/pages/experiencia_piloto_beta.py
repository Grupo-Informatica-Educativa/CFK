import streamlit as st
import numpy as np
from src.utils.chart_funcs import *
from src.utils.helper_funcs import *


def app():
    st.write("""# GreentTIC: Experiencia piloto beta""")

    # Nombre del archivo con los datos
    file = "data/limpios/formularios_greentic_docentes.xlsx"
    # Nombre de la columna cuyos datos son únicos para cada respuesta
    columna_unica = 'Registro'
    # A partir de esta columna comienzan las preguntas (columnas de interés)
    col_preguntas = 9
    files = {
        "respuestas": {}
    }

    # poner eficacia en el metodo Filtro
    # ver como acomarem al metodo graph_answer

    if file:
        datos = pd.read_excel(file, sheet_name='experiencia')

        # initialize list of lists
        columnas = list(datos.columns)

        arreglo_multi_respuesta = ['4. ¿Cuáles de las siguientes palabras describen sus impresiones al iniciar el proceso de uso de la aplicación GreenTIC?',
                                   '8. ¿Qué aspecto valora de su experiencia con la aplicación GreenTIC?',
                                   '20. ¿Cuáles de los siguientes elementos describen las razones que no le permitieron completar la experiencia?',
                                   '26. ¿Qué elemento(s) considera que generaron una impresión diferenciada entre niños y niñas?']

        arreglo_prengutas = ['4. ¿Cuáles de las siguientes palabras describen sus impresiones al iniciar el proceso de uso de la aplicación GreenTIC?',
                             '5. ¿Qué tan satisfecho se siente con el proceso de registro en GreenTIC?',
                             '8. ¿Qué aspecto valora de su experiencia con la aplicación GreenTIC?',
                             '9. ¿Qué mejoraría de la aplicación?',
                             '20. ¿Cuáles de los siguientes elementos describen las razones que no le permitieron completar la experiencia?',
                             '21. ¿En cuanto al uso de la aplicación en sus estudiantes, cuáles de las siguientes emociones logró percibir entre ellos? Interés en completar la experiencia',
                             '26. ¿Qué elemento(s) considera que generaron una impresión diferenciada entre niños y niñas?',
                             '27. ¿Por qué?.1']

        indices_preguntas = [columnas.index(arreglo_prengutas[0]), columnas.index(arreglo_prengutas[1]),
                             columnas.index(arreglo_prengutas[2]), columnas.index(
                                 arreglo_prengutas[3]),
                             columnas.index(arreglo_prengutas[4]), columnas.index(
                                 arreglo_prengutas[5]),
                             columnas.index(arreglo_prengutas[6]), columnas.index(arreglo_prengutas[7])]

        # Esta arreglo de preguntas es necesario debido a que la idea es que el usuario no vea las columnas las cuales
        # segmentamos por respuestas y las convertimos en columnas
        preguntas = np.concatenate((np.array(columnas[col_preguntas:indices_preguntas[0] + 1]),
                                    np.array(
                                        columnas[indices_preguntas[1]: indices_preguntas[2] + 1]),
                                    np.array(
                                        columnas[indices_preguntas[3]: indices_preguntas[4] + 1]),
                                    np.array(
                                        columnas[indices_preguntas[5]: indices_preguntas[6] + 1]),
                                    np.array(columnas[indices_preguntas[7]:])), axis=None)
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

        if lista_cursos != []:
            datos = datos.loc[datos.Curso.isin(lista_cursos)]

        category_orders = categories_order(set(datos[pregunta]), pregunta)

        # Selecciona la respuesta que se desea analizar
        contador = 0
        for i in indices:
            if i in arreglo_multi_respuesta:
                if i == arreglo_multi_respuesta[0]:
                    repeticiones = 18
                    respuestas = np.array(
                        columnas[indices_preguntas[0] + 1:indices_preguntas[0] + repeticiones])
                elif i == arreglo_multi_respuesta[1]:
                    repeticiones = 11
                    respuestas = np.array(
                        columnas[indices_preguntas[2] + 1:indices_preguntas[2] + repeticiones])
                elif i == arreglo_multi_respuesta[2]:
                    repeticiones = 12
                    respuestas = np.array(
                        columnas[indices_preguntas[4] + 1:indices_preguntas[4] + repeticiones])
                else:
                    repeticiones = 17
                    respuestas = np.array(
                        columnas[indices_preguntas[6] + 1:indices_preguntas[6] + repeticiones])
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
