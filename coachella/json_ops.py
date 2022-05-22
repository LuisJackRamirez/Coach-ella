""" JSON Operations """
import json
from horario import get_horario
from kardex import get_kardex
from career import get_career

def create_json (query):
    """ Creates JSON file """
    if query == 1:
        # Horario
        horario_json = json.dumps (get_horario ())

        return horario_json
    elif query == 2:
        # Kardex
        kardex_json = json.dumps (get_kardex ())

        return kardex_json
    elif query == 3:
        # Créditos
        creditos_json = json.dumps (get_career ())

        return creditos_json

    return -1
    