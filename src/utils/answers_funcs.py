def graph_answer(datos,pregunta,preguntas):
    if 'respuestas' in preguntas:
        numero = pregunta.split(' ')[0][:-1]
        if numero not in preguntas['respuestas']:
            return datos
        else:
            color = "Eficacia"
            resp = preguntas['respuestas'][numero]    
            datos[color] = (datos[pregunta] == resp)
            datos[color] = datos[color].replace({True: "Correcto", False: "Incorrecto"})
            return datos
            
def has_answer(datos,pregunta,categoria):
    if categoria == None:
        return False
    if 'respuestas' in categoria:  
        numero = pregunta.split(' ')[0][:-1]
        return (numero in categoria['respuestas'])
    else:
        return False