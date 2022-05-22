""" Horario operations """

def asked_schedule (lemma):
    keywords = [
        'horario',
        'hora',
        'calendario',
        'cuándo',
        'día',
        'clase'
    ]

    if lemma in keywords:
        return True
    
    return False

def get_horario ():
    """ Returns horario values """
    horario = {
        "json_id": 1,
        "materias": [{"id": 1, "nombre":"POO", "grupo":"3", "dia":"Lun", "hora":"0830"}]
    }

    return horario
