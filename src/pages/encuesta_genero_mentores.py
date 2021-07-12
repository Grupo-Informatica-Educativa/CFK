import streamlit as st
from src.utils.chart_funcs import *
from src.utils.helper_funcs import *


def app():
    st.write("""# Encuesta Género a Mentores""")

    # Nombre del archivo con los datos
    file = "data/limpios/Encuesta_genero_mentores.xlsx"
    # Nombre de la columna cuyos datos son únicos para cada respuesta
    columna_unica = 'Registro'
    # A partir de esta columna comienzan las preguntas (columnas de interés)
    col_preguntas = 15

    if file:
        datos = load_data(file)
        chart_type = st.radio("Tipo de visualización ",
                              ("Barras", "Dispersión", "Cajas", "Tendencia"))

        pregunta, filtros_def, indices, lista_agrupadores, lista_cursos = filtros(
            datos, col_preguntas, chart_type)
        ejex, color, columna, fila = filtros_def
        height = st.slider(
            "Ajuste el tamaño vertical de la gráfica", 500, 1000)

        category_orders = categories_order(set(datos[pregunta]), pregunta)
        if lista_cursos != []:
            datos = datos.loc[datos.Curso.isin(lista_cursos)]

        # Selecciona tipo de gráfica
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
                                lista_agrupadores=[pregunta]+lista_agrupadores,
                                category_orders=category_orders)

        # Evita que los títulos de las subfiguras sean de forma VARIABLE=valor
        fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
        fig.update_yaxes(col=1, title=None)
        fig.update_xaxes(row=1, title=None)

        fig.update_layout(height=height)

        st.plotly_chart(fig, use_container_width=True, config=config_chart)
