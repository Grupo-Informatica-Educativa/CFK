import streamlit as st
from src.utils.chart_funcs import *
from src.utils.helper_funcs import *
from src.utils.answers_funcs import *
import pandas as pd


@st.cache
def load_dataset(file):
    return pd.read_excel(file)


def app():
    st.write("""# Graficador de datos en formato vertical""")

    file = "data/limpios/greentic_insignias.xlsx"

    col_preguntas = st.number_input(
        "Cuántas columnas tiene de datos sociodemográficos", 1, 40)

    if file:
        datos = load_dataset(file)

        # Nombre de la columna cuyos datos son únicos para cada respuesta
        columna_unica = st.selectbox('Columna única', datos.columns)

        tipo_grafica = st.radio("Tipo de visualización ",
                            ("Barras", "Dispersión", "Cajas"))

        columnas_filtros = st.multiselect("Seleccione columnas para filtrar:", datos.columns)

        datos, pregunta, filtros_def, indices, lista_agrupadores = filtros_multiselect_vertical(
            datos, col_preguntas, tipo_grafica, columnas_filtros=columnas_filtros)
        # return pregunta, filtros_def, indices, lista_agrupadores
        ################
        ejex, color, columna, fila = filtros_def

        # ---
        height = st.slider(
            "Ajuste el tamaño vertical de la gráfica", 500, 1000)


        answer_orders = st.multiselect(
            'Seleccione el orden en el que se debe presentar el eje x', datos[ejex].unique())
        category_orders = {ejex: answer_orders}
        if color != None:
            color_orders = st.multiselect(
                'Seleccione el orden en el que se deben presentar las categorías de color', datos[color].unique())
            category_orders[color] = color_orders
        if columna != None:
            column_orders = st.multiselect(
                'Seleccione el orden en el que se deben presentar las categorías por columnas', datos[columna].unique())
            category_orders[columna] = column_orders
        if fila != None:
            row_orders = st.multiselect(
                'Seleccione el orden en el que se deben presentar las categorías por fila', datos[fila].unique())
            category_orders[fila] = row_orders

        if len(datos) == 0:
            st.warning("El / los grupos seleccionados no tienen datos para mostrar")
        elif (fila == "Grupo" or columna == "Grupo") and (len(datos.Grupo.unique()) > 10):
            st.warning("Por favor use los filtros para seleccionar menos grupos")
        else:
            # Selecciona tipo de gráfica
            if tipo_grafica == "Barras":
                # Los diagramas de barra exigen agrupar la información antes de graficar
                pivot = pivot_data(datos, indices, columna_unica)
                fig = bar_chart(columna_unica=columna_unica,
                                pivot=pivot, ejex=ejex, color=color,
                                fila=fila, columna=columna, indices=indices,
                                category_orders=category_orders)
            elif tipo_grafica == "Cajas":

                fig = box_chart(columna_unica=pregunta,
                                pivot=datos, ejex=ejex, color=color,
                                fila=fila, columna=columna, indices=indices, category_orders=category_orders)
                fig.update_yaxes(col=1, title=None)
            else:
                fig = scatter_chart(columna_unica=columna_unica,
                                    pivot=datos, ejex=ejex, color=color,
                                    fila=fila, columna=columna,
                                    lista_agrupadores=[
                                        pregunta]+lista_agrupadores,
                                    category_orders=category_orders)

            # Evita que los títulos de las subfiguras sean de forma VARIABLE=valor
            fig.for_each_annotation(
                lambda a: a.update(text=a.text.split("=")[-1]))
            # Quita los nombres de los ejes (se ven feos cuando se divide por columnas)
            fig.update_yaxes(col=1, title=None)
            fig.update_xaxes(row=1, title=None)

            fig.update_layout(height=height)

            st.plotly_chart(fig, use_container_width=True, config=config_chart)
