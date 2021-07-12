import streamlit as st
import numpy as np
from src.utils.chart_funcs import *
from src.utils.helper_funcs import *


def app():
    st.write("""# GreentTIC: Datos App partidas""")

    # Nombre del archivo con los datos
    file = "data/limpios/datos_greentic_app.xlsx"
    # Nombre de la columna cuyos datos son únicos para cada respuesta
    columna_unica = 'usuario_id'
    # A partir de esta columna comienzan las preguntas (columnas de interés)
    col_preguntas = 11
    files = {
        "respuestas": {}
    }

    # poner eficacia en el metodo Filtro
    # ver como acomarem al metodo graph_answer

    if file:
        datos = pd.read_excel(file, sheet_name='partidas')

        # initialize list of lists
        columnas = list(datos.columns)

        arreglo_multi_respuesta = []

        arreglo_prengutas = []

        indices_preguntas = []

        # Esta arreglo de preguntas es necesario debido a que la idea es que el usuario no vea las columnas las cuales
        # segmentamos por respuestas y las convertimos en columnas
        preguntas = columnas[col_preguntas:]

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

        # if color == "Eficacia":
        #	datos = graph_answer(datos, pregunta, files)

        if lista_cursos != []:
            datos = datos.loc[datos.Curso.isin(lista_cursos)]

        category_orders = categories_order(set(datos[pregunta]), pregunta)

        # Se selecciona el tipo de grafica
        if chart_type == "Barras":
            """ Los diagramas de barra exigen agrupar la información antes de graficar """
            # st.write(indices)
            pivot = pivot_data(datos, indices, columna_unica)

            # if color == "Eficacia":
            #	pivot = pivot.sort_values(by=['Eficacia'], ascending=False)

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
                             lista_agrupadores=[
                                 pregunta]+lista_agrupadores,
                             category_orders=category_orders)
        else:
            fig = scatter_chart(columna_unica=columna_unica,
                                pivot=datos, ejex=ejex, color=color,
                                fila=fila, columna=columna,
                                lista_agrupadores=[
                                    pregunta] + lista_agrupadores,
                                category_orders=category_orders)

        # Evita que los títulos de las subfiguras sean de forma VARIABLE=valor
        fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
        fig.update_yaxes(col=1, title=None)
        fig.update_xaxes(row=1, title=None)

        fig.update_layout(height=height)

        st.plotly_chart(fig, use_container_width=True, config=config_chart)
