import time
import pandas as pd
import numpy as np
from diccionario import municipio_parser

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

ISEMPTY = object()

a, b = 'áéíóúü', 'aeiouu'
trans = str.maketrans(a, b)


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.2f ms' %
                  (method.__name__, (te - ts) * 1000))
        return result
    return timed

def limpiar_municipio(data, column):
    data[column] = data[column].str.translate(trans).str.lower().str.strip()
    data[column] = data[column].map(lambda municipio: municipio_parser[municipio] if municipio in municipio_parser else municipio).str.capitalize()
    print("limpiar_municipio!")

def limpiar_dob(data,column):
    data[column] = pd.to_datetime(data[column], format="%Y-%m-%d", errors='coerce')
    mediana = data[column].median()
    data[column] = data[column].fillna(mediana)
    data.loc[(data[column] > '2011-01-01') | (data[column] < '1930-01-01'), column] = mediana
    print("done limpiar_dob!")

def limpiar_profesion(data,column):
    profesion_titulo = {
        r'(.*)\bing(.*)': 'Ingenieria',
        r'(.*)\blic(.*)': 'Licenciatura',
        r'(.*)\bdoce(.*)': 'Docencia',
        r'(.*)\bprof(.*)': 'Docencia',
        r'(.*)\bmentor(.*)': 'Mentoria',
        r'(.*)\becon(.*)': 'Economia',
        r'(.*)\badmin(.*)': 'Administracion',
        r'(.*)\bfisic(.*)': 'Fisica',
    }
    
    profesion_campo= {
        r'(.*)\bcompu(.*)': 'Sistemas',
        r'(.*)\belectr(.*)': 'Electronica',
        r'(.*)\belectri(.*)': 'Electrica',
        r'(.*)\bfis(.*)': 'Fisica',
        r'(.*)\bindus(.*)': 'Industrial',
        r'(.*)\binform(.*)': 'Informatica',
        r'(.*)\blengua(.*)': 'Literatura',
        r'(.*)\bletra(.*)': 'Literatura',
        r'(.*)\blite(.*)': 'Literatura',
        r'(.*)\bmeca(.*)': 'Mecanica',
        r'(.*)\bpedag(.*)': 'Pedagogia',
        r'(.*)\bqu(.*)': 'Quimica',
        r'(.*)\bsistem(.*)': 'Sistemas',
        r'(.*)\btecno(.*)': 'Tecnologia',
        r'(.*)\bteleco(.*)' : 'Telecomunicaciones',
    }

    data[column] = data[column].str.translate(trans).str.lower().str.strip()


    data['Profesion Titulo'] = data[column].str.split().str[0].replace(regex=profesion_titulo).str.capitalize()   
    data.loc[~(data['Profesion Titulo'].isin(profesion_titulo.values())),'Profesion Titulo'] = data['Profesion Titulo'].mode()[0]
    data['Profesion Campo'] = data[column].str.split().str[-1].replace(regex=profesion_campo).str.capitalize()
    data.loc[~(data['Profesion Campo'].isin(profesion_campo.values())),'Profesion Campo'] = data['Profesion Campo'].mode()[0]
    print("done limpiar_profesion!")

def clean_database(data, options=ISEMPTY):
    '''
    `opciones` : dict
    Debe tener la siguiente estructura:
    {
        'columna1': 'id_funcion1',
        'columna2': 'id_funcion2'
    }

    '''
    if options is None or options is ISEMPTY:
        return None
    else:
        for column in options:
            eval(f"limpiar_{options[column]}(data, column)")
        return data
    
        
        

