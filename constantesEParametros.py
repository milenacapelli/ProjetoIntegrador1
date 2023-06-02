from enum import Enum

class Constantes(Enum):
    MP10 = "mp10"
    MP25 = "mp25"
    O3 = "o3"
    CO = "co"
    NO2 = "no2"
    SO2 = "so2"
    BOA = "Boa"
    MODERADA = "Moderada"
    RUIM = "Ruim"
    MUITO_RUIM = "Muito Ruim"
    PESSIMA = "Pessima"

valorDaQualidade = {
    "Boa": 0, 
    "Moderada": 1,
    "Ruim": 2,
    "Muito Ruim": 3,
    "Pessima": 4
}

intervalosConcentracao = {
    "mp10":[
        [0, 50],
        [51 , 100],
        [101, 150],
        [151, 250],
        [251]
    ],
    "mp25": [
        [0, 25],
        [26, 50],
        [51, 75],
        [76, 125],
        [126]
    ],
    "o3": [
        [0, 100],
        [101, 130],
        [131, 160],
        [161, 200],
        [201]
    ],
    "co": [
        [0, 9],
        [10, 11],
        [12, 13],
        [14, 15],
        [16]
    ],
    "no2": [
        [0, 200],
        [201, 240],
        [241, 320],
        [321, 1130],
        [1131]
    ],
    "so2": [
        [0, 20],
        [21, 40],
        [41, 365],
        [366, 800],
        [801]
    ]
}

tabelaQualidadeAr = {
    "mp10": {
        "Boa": {
            "indiceInicial": 0,
            "indiceFinal": 40,
            "concentracaoInicial": 0,
            "concentracaoFinal": 50
        },
        "Moderada": {
            "indiceInicial": 41,
            "indiceFinal": 80,
            "concentracaoInicial": 51,
            "concentracaoFinal": 100
        },
        "Ruim": {
            "indiceInicial": 81,
            "indiceFinal": 120,
            "concentracaoInicial": 101,
            "concentracaoFinal": 150
        },
        "Muito Ruim": {
            "indiceInicial": 121,
            "indiceFinal": 200,
            "concentracaoInicial": 151,
            "concentracaoFinal": 250
        },
        "Pessima": {
            "indiceInicial": 201,
            "indiceFinal": False,
            "concentracaoInicial": 251,
            "concentracaoFinal": False
        },
    },
    "mp25": {
        "Boa": {
            "indiceInicial": 0,
            "indiceFinal": 40,
            "concentracaoInicial": 0,
            "concentracaoFinal": 25
        },
        "Moderada": {
            "indiceInicial": 41,
            "indiceFinal": 80,
            "concentracaoInicial": 26,
            "concentracaoFinal": 50
        },
        "Ruim": {
            "indiceInicial": 81,
            "indiceFinal": 120,
            "concentracaoInicial": 51,
            "concentracaoFinal": 75
        },
        "Muito Ruim": {
            "indiceInicial": 121,
            "indiceFinal": 200,
            "concentracaoInicial": 76,
            "concentracaoFinal": 125
        },
        "Pessima": {
            "indiceInicial": 200,
            "indiceFinal": False,
            "concentracaoInicial": 126,
            "concentracaoFinal": False
        },
    },
    "o3": {
        "Boa": {
            "indiceInicial": 0,
            "indiceFinal": 40,
            "concentracaoInicial": 0,
            "concentracaoFinal": 100
        },
        "Moderada": {
            "indiceInicial": 41,
            "indiceFinal": 80,
            "concentracaoInicial": 101,
            "concentracaoFinal": 130
        },
        "Ruim": {
            "indiceInicial": 81,
            "indiceFinal": 120,
            "concentracaoInicial": 131,
            "concentracaoFinal": 160
        },
        "Muito Ruim": {
            "indiceInicial": 121,
            "indiceFinal": 200,
            "concentracaoInicial": 161,
            "concentracaoFinal": 200
        },
        "Pessima": {
            "indiceInicial": 201,
            "indiceFinal": False,
            "concentracaoInicial": 201,
            "concentracaoFinal": False
        },
    },
    "co": {
        "Boa": {
            "indiceInicial": 0,
            "indiceFinal": 40,
            "concentracaoInicial": 0,
            "concentracaoFinal": 9
        },
        "Moderada": {
            "indiceInicial": 41,
            "indiceFinal": 80,
            "concentracaoInicial": 10,
            "concentracaoFinal": 11
        },
        "Ruim": {
            "indiceInicial": 81,
            "indiceFinal": 120,
            "concentracaoInicial": 12,
            "concentracaoFinal": 13
        },
        "Muito Ruim": {
            "indiceInicial": 121,
            "indiceFinal": 200,
            "concentracaoInicial": 13,
            "concentracaoFinal": 15
        },
        "Pessima": {
            "indiceInicial": 200,
            "indiceFinal": False,
            "concentracaoInicial": 16,
            "concentracaoFinal": False
        },
    },
    "no2": {
        "Boa": {
            "indiceInicial": 0,
            "indiceFinal": 40,
            "concentracaoInicial": 0,
            "concentracaoFinal": 200
        },
        "Moderada": {
            "indiceInicial": 41,
            "indiceFinal": 80,
            "concentracaoInicial": 201,
            "concentracaoFinal": 240
        },
        "Ruim": {
            "indiceInicial": 81,
            "indiceFinal": 120,
            "concentracaoInicial": 241,
            "concentracaoFinal": 320
        },
        "Muito Ruim": {
            "indiceInicial": 121,
            "indiceFinal": 200,
            "concentracaoInicial": 321,
            "concentracaoFinal": 1130
        },
        "Pessima": {
            "indiceInicial": 200,
            "indiceFinal": False,
            "concentracaoInicial": 1131,
            "concentracaoFinal": False
        },
    },
    "so2": {
        "Boa": {
            "indiceInicial": 0,
            "indiceFinal": 40,
            "concentracaoInicial": 0,
            "concentracaoFinal": 20
        },
        "Moderada": {
            "indiceInicial": 41,
            "indiceFinal": 80,
            "concentracaoInicial": 21,
            "concentracaoFinal": 40
        },
        "Ruim": {
            "indiceInicial": 81,
            "indiceFinal": 120,
            "concentracaoInicial": 41,
            "concentracaoFinal": 365
        },
        "Muito Ruim": {
            "indiceInicial": 121,
            "indiceFinal": 200,
            "concentracaoInicial": 366,
            "concentracaoFinal": 800
        },
        "Pessima": {
            "indiceInicial": 200,
            "indiceFinal": False,
            "concentracaoInicial": 801,
            "concentracaoFinal": False
        },
    }
}

opcoesDicionario = {
    "1": "mp10",
    "2": "mp25",
    "3": "o3",
    "4": "co",
    "5": "no2",
    "6": "so2"
}