from multiapp import MultiApp
from src.pages import ejemplo2020
from src.pages import encuesta_genero_mentores
from src.pages import pretest_inicial
from src.pages import pretest_avanzado
from src.pages import encuesta_caracterizacion
from src.pages import caracterizacion_piloto_beta
from src.pages import pretest_piloto_beta
from src.pages import pretest_mentores

from src.preguntas.p1 import pregunta1

app = MultiApp('CFK 2021')

# Add all your application here
app.add_app("Pretest Inicial", pretest_inicial.app)
app.add_app("Pretest Avanzado", pretest_avanzado.app)
app.add_app("Encuesta Género a Mentores", encuesta_genero_mentores.app)
app.add_app("Pretest Mentores", pretest_mentores.app)
app.add_app("Encuesta Caracterización", encuesta_caracterizacion.app)

app.add_app("GreenTIC: Caracterización piloto beta",
            caracterizacion_piloto_beta.app)
app.add_app("GreenTIC: Pretest piloto beta", pretest_piloto_beta.app)

# The main app
app.run()
