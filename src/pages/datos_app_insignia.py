import streamlit as st
import numpy as np
from src.utils.chart_funcs import *
from src.utils.helper_funcs import *


def app():
    st.write("""# GreentTIC: Datos App insignias""")

    # Nombre del archivo con los datos
    file = "data/limpios/datos_greentic_app.xlsx"
    # Nombre de la columna cuyos datos son únicos para cada respuesta
    columna_unica = 'usuario_id'
    # A partir de esta columna comienzan las preguntas (columnas de interés)
    col_preguntas = 6
    files = {
        "respuestas": {}
    }

    # poner eficacia en el metodo Filtro
    # ver como acomarem al metodo graph_answer

    if file:
        datos = pd.read_excel(file, sheet_name='insignias')

        # initialize list of lists
        columnas = list(datos.columns)

        arreglo_multi_respuesta = ['1. insignia(ruta)']

        arreglo_prengutas = ['1. insignia(ruta)']

        indices_preguntas = [columnas.index(arreglo_prengutas[0])]

        # Esta arreglo de preguntas es necesario debido a que la idea es que el usuario no vea las columnas las cuales
        # segmentamos por respuestas y las convertimos en columnas
        preguntas = list([columnas[col_preguntas]])

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

        contador = 0
        for i in indices:
            if i in arreglo_multi_respuesta:
                repeticiones = 30
                respuestas = np.array(
                    columnas[indices_preguntas[0] + 1:indices_preguntas[0] + repeticiones])
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
