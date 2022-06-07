# JSON operations
import simplejson as json

# Uncomment following lines if testing from server.py
# from horario import get_horario
# from kardex import get_kardex
# from career import get_career

from coachella.horario import get_horario
from coachella.kardex import get_kardex
from coachella.career import get_career

def create_json (query, username, aux):
    # Creates JSON file
    if query == 1:
        # Horario
        horario = get_horario (username, aux)

        if horario == -1:
            horario_json = "Invalid request"
        else:
            horario_json = json.dumps (horario)

        return horario_json
    elif query == 2:
        # Kardex
        kardex = get_kardex (username)

        if kardex == -1:
            kardex_json = "Invalid request"
        else:
            kardex_json = json.dumps (kardex)

        return kardex_json
    elif query == 3:
        # Creditos
        career = get_career (username)

        if career == -1:
            creditos_json = "Invalid request"
        else:
            creditos_json = json.dumps (career)

        return creditos_json

    return -1
    