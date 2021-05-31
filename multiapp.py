"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st


class MultiApp:
    # From  https://github.com/upraneelnihar/streamlit-multiapps
    #       https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4
    """Framework for combining multiple streamlit applications.
    Usage:
        def foo():
            st.title("Hello Foo")
        def bar():
            st.title("Hello Bar")
        app = MultiApp()
        app.add_app("Foo", foo)
        app.add_app("Bar", bar)
        app.run()
    It is also possible keep each application in a separate file.
        import foo
        import bar
        app = MultiApp()
        app.add_app("Foo", foo.app)
        app.add_app("Bar", bar.app)
        app.run()
    """

    def __init__(self, page_title):
        self.apps = []
        self.page_title = page_title
        st.set_page_config(
            page_title=page_title,
            layout="wide",
        )

    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        st.sidebar.write(f'# {self.page_title}')
        app = st.sidebar.radio(
            'Secciones:',
            self.apps,
            format_func=lambda app: app['title'])
        graph_expander = st.sidebar.beta_expander(label='Graficador')
        with graph_expander:
            graph_expander.write("s")
        expander = st.sidebar.beta_expander(label='Changelog')
        with expander:
            expander.write("Changelog test")
        app['function']()
