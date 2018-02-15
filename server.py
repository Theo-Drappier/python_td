# -*- encoding: utf-8 -*-
from flask import Flask
from flask import request
import json
from flask import render_template

from models.Connection import Connection

app = Flask(__name__)


@app.route('/')
def index():
    cnx = Connection('metrics')
    allHost = cnx.selectAllHost()
    return render_template('index.html', allHost=allHost)


@app.route('/chartHost', methods=['POST'])
def hello():
    name = request.form['hostname']
    cnx = Connection('metrics')
    allMetrics = cnx.selectByHost(name)
    lastMetrics = allMetrics[-1]
    cpuUsed = lastMetrics[0]
    cpuFree = 100.0 - cpuUsed
    memories = lastMetrics[1]
    memoryFree = memories[1] / (1024.0**3)
    memoryFree = "%.2f" % memoryFree
    memoryUsed = memories[3] / (1024.0**3)
    memoryUsed = "%.2f" % memoryUsed
    return render_template('chartHost.html', name=name, memoryFree=memoryFree, memoryUsed=memoryUsed, cpuUsed=cpuUsed, cpuFree=cpuFree, allMetrics=allMetrics)


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
