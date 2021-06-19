"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st
from src.pages import ejemplo2020


class MultiApp:

    def __init__(self, page_title):
        
        self.preguntas = []
        self.inicial = []
        self.avanzado = []
        self.mentores = []
        self.greentic = []
        self.page_title = page_title
        st.set_page_config(
            page_title=page_title,
            layout="wide",
        )

    def add_app(self, title, func,_type):
        if  _type == "Inicial":
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

    def run(self):
        st.sidebar.write(f'# {self.page_title}')

        categorias = st.sidebar.radio("Secciones",["Herramientas","Cuestionario Inicial","Cuestionario Avanzado","Greentic","Mentores"])
 
        if categorias == "Herramientas":
            pages = [{
                    'title': 'Graficador',
                    'function': ejemplo2020.app
                }]
            app = st.sidebar.radio("Seleccione herramienta: ", pages, format_func=lambda app: app['title'])
        elif categorias == "Cuestionario Inicial":
            app = st.sidebar.radio("Seleccione cuestionario: ", self.inicial, format_func=lambda app: app['title'])
        elif categorias == "Cuestionario Avanzado":
            app = st.sidebar.radio("Seleccione cuestionario: ", self.avanzado, format_func=lambda app: app['title'])
        elif categorias == "Greentic":
            app = st.sidebar.radio("Seleccione: ", self.greentic, format_func=lambda app: app['title'])
        elif categorias == "Mentores":
            app = st.sidebar.radio("Seleccione: ", self.mentores, format_func=lambda app: app['title'])
        
        app['function']()