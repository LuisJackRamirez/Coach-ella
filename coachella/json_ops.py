# JSON operations
import simplejson as json

# Uncomment following lines if testing from server.py
# from horario import get_horario
# from kardex import get_kardex
# from career import get_career

from coachella.horario import get_horario
from coachella.kardex import get_kardex
from coachella.career import get_career

def create_json (query, username):
    # Creates JSON file
    if query == 1:
        # Horario
        horario_json = json.dumps (get_horario (username))

        return horario_json
    elif query == 2:
        # Kardex
        kardex_json = json.dumps (get_kardex (username))

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
    