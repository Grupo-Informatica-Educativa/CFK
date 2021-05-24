from multiapp import MultiApp
from src.pages import ejemplo2020
from src.pages import encuesta_genero_mentores
from src.pages import pretest_inicial
from src.pages import pretest_avanzado
from src.pages import encuesta_caracterizacion

app = MultiApp('CFK 2021')

# Add all your application here
app.add_app("Encuesta Género a Mentores", encuesta_genero_mentores.app)
app.add_app("Pretest Inicial", pretest_inicial.app)
app.add_app("Pretest Avanzado", pretest_avanzado.app)
app.add_app("Encuesta Caracterización", encuesta_caracterizacion.app)


# The main app
app.run()
