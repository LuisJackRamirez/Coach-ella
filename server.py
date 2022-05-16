""" Main server """

from flask import Flask
from flask import render_template
from flask import request
from json_ops import create_json
from nlp import read_query

app = Flask (__name__)
app.config ['SECRET_KEY'] = 'oh_so_secret'

# Aquí se colocan las consultas
cumulative = ['Historial']

@app.route ('/', methods=["GET", "POST"])
def handle_request ():
    # Handles request
    if request.method == 'POST':
        # Obtiene el cuerpo del mensaje
        value = request.form['msg']
        print (request.form)

        # Capturar valor para mostrarlo en página web del servidor.
        cumulative.append (str (value))

        # Envío de la solicitud para su análisis
        user_request = read_query (value)
        print ("User request: " + str(user_request))

        # Manejo de la respuesta
        if user_request == -1:
            # La solicitud no fue reconocida,
            # se muestra un resultado inválido
            ret_value = "Invalid request"
        if user_request == 1:
            # La solicitud fue clasificada como
            # una consulta de horario
            ret_value = create_json (1)
            # La solicitud fue clasificada como
            # una consulta de calificaciones
        elif user_request == 2:
            ret_value = create_json (2)
            # La solicitud fue clasificada como
            # una consulta de créditos
        elif user_request == 3:
            ret_value = create_json (3)

        return ret_value
    elif request.method == 'GET':
        # print ("Texto obtenido: ", str (cumulative[-1]))
        return render_template ("index.html", msg = str(cumulative[0]))
        # return render_template ("index.html", msg = "\n".join (cumulative))

if __name__ == '__main__':
    app.run (host="0.0.0.0", debug=True)