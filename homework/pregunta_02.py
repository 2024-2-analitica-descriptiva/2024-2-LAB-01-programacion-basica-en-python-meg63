"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
def pregunta_02():
    with open('files/input/data.csv', 'r') as file:
        archivo = csv.reader(file, delimiter='\t')
        diccionario = {}
        for row in archivo:
            if row[0] in diccionario.keys():
                diccionario[row[0]] += 1
            else:
                diccionario[row[0]] = 1
        return sorted(diccionario.items())

    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
pregunta_02()