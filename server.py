# -*- encoding: utf-8 -*-
from flask import Flask
from flask import request
import json
from flask import render_template

from models.Connection import Connection

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('index.html', name=name)


@app.route('/post', methods=['POST'])
def firstPost():
    if request.method == 'POST':
        data = request.data
        dataJson = json.loads(data)
        cnx = Connection('metrics')
        cnx.insertRow(dataJson)
        cnx.closeConnect()
        return True


if __name__ == '__main__':
    app.run(debug=True)
