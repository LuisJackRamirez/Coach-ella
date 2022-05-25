""" Kardex operations """

# eval: [ord | ext | ets] """

def asked_grades (lemma):
    keywords = [
        'calificación',
        'sacar',
        'ordinario',
        'extraordinario',
        'suficiencia',
        'ets'
    ]

    if lemma in keywords:
        return True
    
    return False

def get_kardex ():
    """ Returns horario values """
    kardex = {
        "json_id": 2,
        "materias": [
            {   "id": 1,            \
                "nombre":"POO",     \
                "grupo":"3",        \
                "calif":10,         \
                "eval":"ord",       \
                "periodo":"20-1"    \
            },
            {
                "id": 466,          \
                "nombre":"IES",     \
                "grupo":"3",        \
                "calif":6,          \
                "eval":"ext",       \
                "periodo":"20-1"    \
            }
        ]
    }

    return kardex
