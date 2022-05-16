""" Career operations """

def asked_credits (lemma):
    keywords = [
        'carrera',
        'crédito',
        'reprobado','reprobada',
        'periodo',
        'carga',
        'académico',
        'trayectoria'
    ]

    if lemma in keywords:
        return True
    
    return False

def get_career ():
    """ Returns career values """
    carrera = {
        "json_id": 3,
        "reprobadas": 0,
        "creditos_total":196.03,
        "creditos_pend":33.57,
        "creditos_repr":61.00,
        "periodos_cursados":7,
        "periodos_disponibles":7,
        "carga_auth":"max"
    }

    return carrera
