#!/usr/bin/env python3

import os
from flask import Flask, jsonify
from fundamentus import get_data
from datetime import datetime

app = Flask(__name__)

# First update
lista, dia = dict(get_data()), datetime.strftime(datetime.today(), '%d')

@app.route("/")
def json_api():
    global lista, dia
    
    # Then only update once a day
    if dia == datetime.strftime(datetime.today(), '%d'):
        return jsonify(lista)
    else:
        lista, dia = dict(get_data()), datetime.strftime(datetime.today(), '%d')
        return jsonify(lista)

port = int(os.environ.get('PORT', 5000))

app.run(debug=True, host='0.0.0.0', port=port)