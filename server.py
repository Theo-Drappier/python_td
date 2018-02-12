# -*- encoding: utf-8 -*-
from flask import Flask
from flask import request
import json

from models.Connection import Connection

app = Flask(__name__)


@app.route('/')
def hello():
    return "<h1><small>Hello World !</small></h1>"


@app.route('/post', methods=['POST'])
def firstPost():
    if request.method == 'POST':
        data = request.data
        dataJson = json.loads(data)
        cnx = Connection('metrics')
        cnx.insertRow(dataJson)
        cnx.closeConnect()


if __name__ == '__main__':
    app.run(debug=True)
