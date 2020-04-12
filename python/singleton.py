import time
import threading

def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper


class Singleton(object):
    _instance = None
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kw):
        with cls._instance_lock:
            if cls._instance is None:
                cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, x, y):
        self.x = x
        self.y = y


s = Singleton(1, 2)
print(s.x)