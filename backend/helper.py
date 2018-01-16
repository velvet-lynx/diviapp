import multiprocessing
import multiprocessing.pool

class NoDaemonProcess(multiprocessing.Process):
    """ Modified version of multiprocessing process
        with daemon parameter set to false"""
    def _get_daemon(self):
        return False
    def _set_daemon(self, value):
        pass
    daemon = property(_get_daemon, _set_daemon)

class Pool(multiprocessing.pool.Pool):
    """ Modified version of multiprocessing Pool allowing
        the creation of children pools of workers """
    Process = NoDaemonProcess

def to_dict_list(lines):
    return [
        dict(zip(line.keys(), line.first()))
        for line in lines
    ]

def to_dict(keys, datas):
    return dict(zip(keys, datas))