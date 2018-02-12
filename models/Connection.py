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
            print c[0], c[1], c[2]

        cursor.close()

    def insertRow(self, newRow):
        memory = newRow['memory'][0] / 1024
        cpu = newRow['cpu']
        insertQuery = "INSERT INTO " + self._table + " (cpu, memory) VALUES (" + str(cpu) + ", " + str(memory) + ")"
        cursor = self._cnx.cursor()
        cursor.execute(insertQuery)
        self._cnx.commit()
        cursor.close()

    def closeConnect(self):
        self._cnx.close()
