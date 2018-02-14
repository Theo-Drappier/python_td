# -*- encoding: utf-8 -*-
from mysql import connector
import json
import datetime

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
        insertQuery = "INSERT INTO " + self._table + " (cpu, memory, disks, name, os, daTime) VALUES (%(cpu)s, %(memory)s, %(disks)s, %(hostname)s, %(os)s, NOW())"
        cursor = self._cnx.cursor()
        cursor.execute(insertQuery, newRow)
        self._cnx.commit()
        cursor.close()

    def closeConnect(self):
        self._cnx.close()

    def selectAllHost(self):
        query = "SELECT DISTINCT name FROM metrics;"
        cursor = self._cnx.cursor()
        cursor.execute(query)
        arrayHost = []
        for c in cursor:
            arrayHost.append(c)
        cursor.close()
        return arrayHost

    def selectByHost(self, host):
        query = "SELECT cpu, memory, disks, os, name, daTime FROM metrics WHERE name = '" + host + "' ORDER BY daTime ASC LIMIT 5;"
        cursor = self._cnx.cursor()
        cursor.execute(query)
        arrayMetrics = []
        i = 0
        for row in cursor:
            arrayMetrics.append([])
            for c in row:
                try:
                    jsonC = json.loads(c)
                except ValueError as e:
                    jsonC = c
                    print e
                except TypeError as e:
                    jsonC = c
                    print e
                finally:
                    arrayMetrics[i].append(jsonC)
            i+=1
        cursor.close()
        return arrayMetrics



