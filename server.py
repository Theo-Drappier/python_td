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
    cnx = Connection('metrics')
    allHost = cnx.selectAllHost()
    lastMetrics = cnx.selectByHost('ubuntu')[0]
    memories = lastMetrics[1]
    memoryFree = memories[1] / (1024.0**3)
    memoryUsed = memories[3] / (1024.0**3)
    return render_template('index.html', name=name, memoryFree=memoryFree, memoryUsed=memoryUsed)


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
