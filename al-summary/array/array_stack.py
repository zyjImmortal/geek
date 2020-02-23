

class ArrayStack:
    
    def __init__(self):
        self._stack = []
        
    def push(self, item):
        self._stack.append(item)
    
    def pop(self):
        self._stack.pop()