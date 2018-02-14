# -*- encoding: utf-8 -*-
import psutil
import requests
import os
import socket
import json


class HostInfo:

    version = "0.1"
    _cpu = ()
    _os = ()
    _memory = ()
    _disks = ()
    _hostname = ()

    def __init__(self):
        """
        Init object HostInfo
        """
        print "New instance"

    # def _get_process_rf(self):

    def get_info(self):
        self._cpu = psutil.cpu_percent()
        self._memory = json.dumps(psutil.virtual_memory())
        self._disks = json.dumps(psutil.disk_io_counters(perdisk=True))
        self._os = os.name
        self._hostname = socket.gethostname()

    def publish(self):
        requests.post('http://127.0.0.1:5000/post', json={
            'cpu': self._cpu, 'disks': self._disks, 'memory': self._memory, 'os': self._os, 'hostname': self._hostname
        })



