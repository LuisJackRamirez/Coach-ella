from coachella.json_ops import create_json
from coachella.nlp import read_query

from collections import deque

from flask import Blueprint
from flask import render_template
from flask import request

import datetime

# Blueprints allow us to organize related views 
# and other code. We register the views in the
# blueprint, and then we register the blueprint
# in the application
#
# Since we only have one view, 
# we only need one Blueprint

# Create Blueprint named 'auth'. We pass "__name__"
# to know where the app object is defined. The URL
# prefix will be prepended to all URLs associated
bp = Blueprint('coachella', __name__, url_prefix='/coachella')

# Here we will hold all requests
q = deque ()

for i in range(10):
    q.append ('')

# When user visits the "coachella/" URL, the
# 'handle_request' view will return HTML with
# the voice requests history.
# 
# For now, it won't require a login
@bp.route ('/', methods=["GET", "POST"])
def handle_request ():
    # Handles voice assistant query
    if request.method == 'POST':
        # Gets body from request
        value = request.form['msg']
        username = request.form['user']
        print (request.form)

        # Obtain query to show on server's website
        q.popleft ()
        now = datetime.datetime.now ()
        q.append ("[" + str(now.year) + "-" + f'{now.month:02}' + "-" + f'{now.day:02}' + " - "
            + f'{now.hour:02}' + ":" + f'{now.minute:02}' + ":" + f'{now.second:02}' + " - " + request.remote_addr + "] -- "
            + str(username) + ": " + value)

        # Query will be analyzed.
        aux = []
        user_request, aux = read_query (value)
        print ("User request: " + str(user_request))

        # Handle query response and create JSON file
        if user_request == -1:
            # Request wasn't identified, we will
            # show an invalid result.
            ret_value = "Invalid request"
        if user_request == 1:
            # Request was identified as 'horario'
            ret_value = create_json (1, username, aux)
            # Request was identified as 'kardex'
        elif user_request == 2:
            ret_value = create_json (2, username, aux)
            # Request was identified as 'credits'
        elif user_request == 3:
            ret_value = create_json (3, username, aux)

        # Return JSON file
        return ret_value

    # Handles website history
    elif request.method == 'GET':
        # print ("Texto obtenido: ", str (cumulative[-1]))
        return render_template ("index.html", msg = reversed(q))
        # return render_template ("index.html", msg = "\n".join (cumulative))