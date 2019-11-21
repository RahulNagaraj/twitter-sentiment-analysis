# Server

import os
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tweets')
def tweets():
    # Do some operation


port = int(os.environ.get('PORT', 5000))
app.run(host="0.0.0.0", port=port, debug=True)
