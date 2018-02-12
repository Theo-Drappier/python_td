# -*- encoding: utf-8 -*-
import psutil
import requests


class HostInfo:

    version = "0.1"
    _cpu = ()
    _memory = ()
    _disks = ()

    def __init__(self):
        """
        Init object HostInfo
        """
        print "New instance"

    # def _get_process_rf(self):

    def get_info(self):
        self._cpu = psutil.cpu_percent()
        self._memory = psutil.virtual_memory()
        self._disks = psutil.disk_io_counters(perdisk=True)

    def publish(self):
        requests.post('http://127.0.0.1:5000/post', json={
            'cpu': self._cpu, 'disks': self._disks, 'memory': self._memory
        })



