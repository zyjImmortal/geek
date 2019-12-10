class File:
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()


from contextlib import contextmanager


@contextmanager
def file(file_name, method):
    f = open(file_name, method)
    yield f
    f.close()


with File('demo.txt', 'w') as f:
    f.write("hahaha")
