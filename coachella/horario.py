# Horario operations

import pymysql

from coachella.db import get_db

def asked_schedule (lemma):
    keywords = [
        'horario',
        'hora',
        'calendario',
        'cuándo',
        'cuando',
        'día',
        'clase'
    ]

    if lemma in keywords:
        return True
    
    return False

def get_horario (username):
    # Returns horario values
    conn = get_db ()
    conn.select_db ('saes')

    query = "SELECT id,nombre,materia.grupo,dia,hora FROM materia_actual INNER JOIN materia ON materia_id = id AND alumno_id = " + username + " ORDER BY id;"
    cursor = conn.cursor (pymysql.cursors.DictCursor)
    cursor.execute (query)
    result = cursor.fetchall ()

    horario = {
        "json_id": 1,
        "materias": []
    }

    for x in result:
        horario["materias"].append (
            {
                "id": x["id"],              \
                "nombre": x["nombre"],      \
                "grupo": x["grupo"],        \
                "dia": x["dia"],            \
                "hora": x["hora"]  
            }
        )

    return horario
