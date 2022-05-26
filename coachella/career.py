# Career operations

from coachella.db import get_db

import pymysql

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

def get_career (username):
    # Returns career values
    query = "SELECT reprobadas,creditos_total,creditos_pend,creditos_repr,periodos_cursados,periodos_disponibles,carga_auth FROM carrera WHERE alumno_id = " + username + ";"

    conn = get_db ()
    conn.select_db ('saes')

    cursor = conn.cursor (pymysql.cursors.DictCursor)
    cursor.execute (query)
    result = cursor.fetchone ()

    carrera = {
        "json_id": 3
    }

    carrera["reprobadas"] = result["reprobadas"]
    carrera["creditos_total"] = result["creditos_total"]
    carrera["creditos_pend"] = result["creditos_pend"]
    carrera["creditos_repr"] = result["creditos_repr"]
    carrera["periodos_cursados"] = result["periodos_cursados"]
    carrera["periodos_disponibles"] = result["periodos_disponibles"]
    carrera["carga_auth"] = result["carga_auth"]

    return carrera
