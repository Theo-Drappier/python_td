# -*- encoding: utf-8 -*-
from mysql import connector


class Connection:
    _cnx = ()
    _config = {
        'user': 'lpdip',
        'password': 'lpdip:17',
        'host': '127.0.0.1',
        'database': 'prog_agent_v0'
    }
    _table = ()

    def __init__(self, table):
        self._cnx = connector.connect(**self._config)
        self._table = table

    def selectAll(self):
        cursor = self._cnx.cursor()
        query = "SELECT * FROM " + self._table
        cursor.execute(query)

        for c in cursor:
            print c.id, c.cpu, c.memory

        cursor.close()

    def closeConnect(self):
        self._cnx.close()