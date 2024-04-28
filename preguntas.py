"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

# python -m venv .venv
# .venv\Scripts\activate
# python.exe -m pip install --upgrade pip

def open_data():
    with open("data.csv", "r") as file:
        lines = file.readlines()
        return lines

# Limpiamos la data, la cual está separada por \t
def clean_data():
    lines = open_data()
    return [line.split("\t") for line in lines]

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    return sum([int(row[1]) for row in clean_data()])

#print(pregunta_01())

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    
    # Retorne la cantidad de registros por cada letra de la primera columna como la lista de tuplas (letra, cantidad), ordendas alfabéticamente.
    
    data = clean_data()
    dic = {}
    
    # Itera sobre las filas del archivo
    for row in data:
        # Si la letra ya está en el diccionario, suma 1 al valor
        if row[0] in dic:
            dic[row[0]] += 1
        # Si no está, crea la llave con valor 1
        else:
            dic[row[0]] = 1
            
    # Retorna una lista de tuplas (clave, valor) ordenada alfabéticamente
    return sorted(dic.items())

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    
    data = clean_data()
    dic = {}
    
    for row in data:
        # Si la letra ya está en el diccionario, suma 1 al valor
        if row[0] in dic:
            dic[row[0]] += int(row[1])
        # Si no está, crea la llave con valor 1
        else:
            dic[row[0]] = int(row[1])
            
    # Retorna una lista de tuplas (clave, valor) ordenada alfabéticamente
    return sorted(dic.items())


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    
    data = clean_data()
    dic = {}
    
    dates = [z[2] for z in data]
    # separa Date en sus partes
    dates = [z.split("-") for z in dates]
    
    # Itera sobre las filas del archivo
    for row in dates:
        # Si el mes ya está en el diccionario, suma 1 al valor
        if row[1] in dic:
            dic[row[1]] += 1
        # Si no está, crea la llave con valor 1
        else:
            dic[row[1]] = 1
            
    # Retorna una lista de tuplas (clave, valor) ordenada
    return sorted(dic.items())

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    
    data = clean_data()

    dic = {} # Diccionario para almacenar los valores máximos y mínimos

    # Iteramos sobre las filas del archivo
    for row in data:

        # Si la letra ya está en el diccionario, comparamos el valor actual con el valor máximo y mínimo
        if row[0] in dic:
            dic[row[0]] = (max(dic[row[0]][0], int(row[1])), min(dic[row[0]][1], int(row[1])))
        # Si no está, creamos la llave con el valor actual
        else:
            dic[row[0]] = (int(row[1]), int(row[1]))

    # Retornamos una lista de tuplas (clave, valor máximo, valor mínimo) ordenada alfabéticamente
    return sorted([(key, value[0], value[1]) for key, value in dic.items()])


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    
    data = clean_data()
    dic = {}
    
    new_data = [z[4] for z in data]
    new_data = [z.strip().split(",") for z in new_data]
    
    for x in new_data:
        for y in x:
            key, value = y.split(":")
            if key in dic:
                dic[key]= (max(dic[key][0], int(value)), min(dic[key][1], int(value)))
            else:
                dic[key] = (int(value), int(value))
    
    return sorted([(key, value[1], value[0]) for key, value in dic.items()])


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    data = clean_data()
    dic = {}
    
    # Iteramos sobre las filas del archivo
    for row in data:
        if row[1] in dic:
            dic[row[1]].append(row[0])
        else:
            dic[row[1]] = [row[0]]

    return sorted([(int(key), value) for key, value in dic.items()])

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    
    data = clean_data()
    dic = {}
    
    # Iteramos sobre las filas del archivo
    for row in data:
        if row[1] in dic:
            dic[row[1]].add(row[0])
        else:
            dic[row[1]] = {row[0]}
    
    return sorted([(int(key), sorted(list(value))) for key, value in dic.items()])


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    
    data = clean_data()
    dic = {}
    
    new_data = [z[4] for z in data]
    new_data = [z.strip().split(",") for z in new_data]
    
    for x in new_data:
        for y in x:
            key,_ = y.split(":")
            if key in dic:
                dic[key] += 1
            else:
                dic[key] = 1

    return dict(sorted(dic.items()))


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    data = clean_data()
    
    return [(row[0], len(row[3].split(",")), len(row[4].split(","))) for row in data]


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    data = clean_data()
    dic = {}
    
    for row in data:
        for letter in row[3].split(","):
            if letter in dic:
                dic[letter] += int(row[1])
            else:
                dic[letter] = int(row[1])
    
    return dict(sorted(dic.items()))



def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    data = clean_data()
    dic = {}
    
    for row in data:
        for letter in row[4].split(","):
            _, value = letter.split(":")
            if row[0] in dic:
                dic[row[0]] += int(value)
            else:
                dic[row[0]] = int(value)
    
    return dict(sorted(dic.items()))
