import numpy as np
from pathlib import Path

class A:
    abc = 1
    def __init__(self, num, *args) -> None:
        self.num = num
        self._a = 1

    @property
    def a(self):
        return self._a
    
    @a.setter
    def a(self, value):
        self._a = value

class B(A):
    def __init__(self, b) -> None:
        self.b = b
    
    @property
    def a(self):
        return self._a