import streamlit as st
from src.utils.chart_funcs import *
from src.utils.helper_funcs import *
from src.utils.answers_funcs import *
import pandas as pd


@st.cache
def load_dataset(file):
    return pd.read_excel(file)


def app():
    st.write("""# Quiz Avanzado""")

    tipo_grafica = st.radio("Tipo de visualización ",
                            ("Barras", "Dispersión", "Cajas"))

    # Nombre del archivo con los datos
    file = "data/limpios/Quiz_avanzado_v1.xlsx"
    # Nombre de la columna cuyos datos son únicos para cada respuesta
    columna_unica = 'Identificación'
    # A partir de esta columna comienzan las preguntas (columnas de interés)
    col_preguntas = 21

    if file:
        datos = load_dataset(file)

        # ---
        cuestionarios = st.multiselect(
            "Seleccione cuestionario(s):", datos.Cuestionario.unique())
        datos = datos.loc[datos.Cuestionario.isin(cuestionarios)]

        intentos = st.multiselect(
            "Seleccione intento(s):", datos.Intento.unique())
        datos = datos.loc[datos.Intento.isin(intentos)]

        numpregs = st.multiselect(
            "Seleccione número de pregunta(s):", datos['Núm.Pregunta'].unique())
        datos = datos.loc[datos['Núm.Pregunta'].isin(numpregs)]

        preguntas = st.multiselect(
            "Seleccione pregunta(s):", datos.Pregunta.unique())
        datos = datos.loc[datos.Pregunta.isin(preguntas)]

        datos.Eficacia = datos.Eficacia.astype(str)
        # de filtros() - helper_functs
        lista_filtros = []

        lista_agrupadores = list(datos.iloc[:, 1:col_preguntas].columns)  # yes

        try:
            cursos = datos.Grupo.unique()
            cursos.sort()
            lista_grupo = st.multiselect(
                'Seleccione los cursos que desea visualizar', cursos)  # yes
        except:
            lista_grupo = []

        if tipo_grafica == 'Cajas':
            lista_filtros.append(st.selectbox(
                "Seleccione el eje x", [' '] + lista_agrupadores))
        elif tipo_grafica == 'Dispersión':
            lista_filtros.append(st.selectbox(
                "Seleccione el eje x", lista_agrupadores))
        else:
            lista_filtros.append(st.selectbox("Seleccione el eje x", [
                "Pregunta", "Cuestionario"] + lista_agrupadores))
        # yes hasta aqui
        cols = st.beta_columns(3)

        for index, col in enumerate(cols):
            with col:
                if index == 0:
                    lista_filtros.append(st.selectbox(
                        "Dividir por color", [" ", "Pregunta", "Cuestionario", "Intento"] + lista_agrupadores))
                elif index == 1:
                    lista_filtros.append(st.selectbox(
                        "Dividir por columna", [" ", "Pregunta", "Cuestionario", "Intento"] + lista_agrupadores))
                elif index == 2:
                    lista_filtros.append(st.selectbox(
                        "Dividir por fila", [" ", "Pregunta", "Cuestionario", "Intento"] + lista_agrupadores))

        filtros_def = [None if x == ' ' else x for x in lista_filtros]
        indices = list(set(filtros_def).difference([None]))

        # return pregunta, filtros_def, indices, lista_agrupadores, lista_grupo

        ################
        pregunta = 'Respuesta'
        pregunta, filtros_def, indices, lista_agrupadores, lista_grupo

        ejex, color, columna, fila = filtros_def

        # ---
        height = st.slider(
            "Ajuste el tamaño vertical de la gráfica", 500, 1000)

        orden_grupos = ["I"+str(x) for x in range(87)]

        category_orders = categories_order(
            set(datos[pregunta]), pregunta, orden_grupos)
        if lista_grupo != []:
            datos = datos.loc[datos.Grupo.isin(lista_grupo)]

        if len(datos) == 0:
            st.warning(
                "El / los grupos seleccionados no tienen datos para mostrar")
        elif (fila == "Grupo" or columna == "Grupo") and (len(datos.Grupo.unique()) > 10):
            st.warning(
                "Por favor use los filtros para seleccionar menos grupos")
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
