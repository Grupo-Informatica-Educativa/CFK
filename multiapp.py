"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st


class MultiApp:

    def __init__(self, page_title):
        self.preguntas = []
        self.inicial = []
        self.avanzado = []
        self.mentores = []
        self.greentic = []
        self.herramientas = []
        self.page_title = page_title
        st.set_page_config(
            page_title=page_title,
            layout="wide",
        )

    def add_app(self, title, func, _type):
        if _type == "Inicial":
            self.inicial.append({
                "title": title,
                "function": func
            })
        elif _type == "Avanzado":
            self.avanzado.append({
                "title": title,
                "function": func
            })
        elif _type == "Greentic":
            self.greentic.append({
                "title": title,
                "function": func
            })
        elif _type == "Pregunta":
            self.preguntas.append({
                "title": title,
                "function": func
            })
        elif _type == "Mentores":
            self.mentores.append({
                "title": title,
                "function": func
            })
        elif _type == "Herramientas":
            self.herramientas.append({
                "title": title,
                "function": func
            })

    def run(self):
        st.sidebar.write(f'# {self.page_title}')

        categoria = st.sidebar.radio("Secciones",
                                     ["Curso Inicial", "Curso Avanzado", "GreenTIC", "Mentores", "Herramientas"])  # , "Preguntas"])

        if categoria == "Herramientas":
            app = st.sidebar.radio(
                "Seleccione herramienta: ", self.herramientas, format_func=lambda app: app['title'])
        elif categoria == "Curso Inicial":
            app = st.sidebar.radio(
                "Seleccione instrumento:", self.inicial, format_func=lambda app: app['title'])
        elif categoria == "Curso Avanzado":
            app = st.sidebar.radio(
                "Seleccione instrumento:", self.avanzado, format_func=lambda app: app['title'])
        elif categoria == "GreenTIC":
            app = st.sidebar.radio(
                "Seleccione instrumento:", self.greentic, format_func=lambda app: app['title'])
        elif categoria == "Mentores":
            app = st.sidebar.radio(
                "Seleccione instrumento:", self.mentores, format_func=lambda app: app['title'])
        elif categoria == "Preguntas":
            app = st.sidebar.radio(
                "Seleccione pregunta:", self.preguntas, format_func=lambda app: app['title'])

        app['function']()
