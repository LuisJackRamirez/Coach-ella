# Horario operations

# import pymysql
import psycopg2.extras

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

def get_horario (username, asked_materias):
    # Returns horario values
    conn = get_db ()
    # conn.select_db ('saes')

    #query = "SELECT id,nombre,materia.grupo,dia,hora FROM materia_actual INNER JOIN materia ON materia_id = id AND alumno_id = " + username + " ORDER BY id;"
    query = "SELECT id,nombre,materia.grupo,dia,hora FROM materia_actual INNER JOIN materia ON materia_id = id AND alumno_id = '" + username + "' ORDER BY id;"
    # cursor = conn.cursor (pymysql.cursors.DictCursor)
    cursor = conn.cursor (
        cursor_factory = psycopg2.extras.RealDictCursor)

    cursor.execute (query)
    result = cursor.fetchall ()

    if len(result) == 0:
        return -1

    horario = {
        "json_id": 1,
        "materias": []
    }

    if len (asked_materias) != 0:
        for x in result:
            for materia in asked_materias:
                if (x["nombre"].lower ()).find (materia) != -1:
                    horario["materias"].append (
                        make_dict (x)
                    )
    else:
        for x in result:
            horario["materias"].append (
                make_dict (x)
            )

    return horario

def make_dict (x):
    return {
        "id": x["id"],              \
        "nombre": x["nombre"],      \
        "grupo": x["grupo"],        \
        "dia": x["dia"],            \
        "hora": x["hora"]  
    }