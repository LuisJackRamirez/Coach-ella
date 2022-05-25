# Kardex operations
# eval: [ord | ext | ets]

from coachella.db import get_db

import pymysql

def asked_grades (lemma):
    keywords = [
        'kardex',
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

def get_kardex (username):
    # Returns kardex values
    conn = get_db ()
    conn.select_db ('saes')

    query = "SELECT materia_id,nombre,materia_cursada.grupo,calif,eval,periodo FROM materia_cursada JOIN materia ON (alumno_id = " + username + " AND id=materia_id) ORDER BY periodo;"
    cursor = conn.cursor (pymysql.cursors.DictCursor)
    cursor.execute (query)
    result = cursor.fetchall ()

    kardex = {
        "json_id": 2,
        "materias": []
    }

    for x in result:
        kardex["materias"].append (
            {
                "id": x["materia_id"],
                "nombre": x["nombre"],
                "grupo": x["grupo"],
                "calif": x["calif"],
                "eval": x["eval"],
                "periodo": x["periodo"]
            }
        )
        print (kardex["materias"][-1])

    return kardex
