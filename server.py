# -*- encoding: utf-8 -*-
from flask import Flask
from flask import request

from myvirtualenv.models.Connection import Connection

app = Flask(__name__)


@app.route('/')
def hello():
    return "<h1><small>Hello World !</small></h1>"


@app.route('/post', methods=['POST'])
def firstPost():
    if request.method == 'POST':
        data = request.data
        cnx = Connection('metrics')
        cnx.selectAll()


if __name__ == '__main__':
    app.run(debug=True)
