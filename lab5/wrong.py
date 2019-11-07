import time

class Timer():
    def __init__(self, *e):
        self.exeptions = e
        
    def __enter__(self):
        print(k)
        
        
    def __exit__(self, exp_type, exp_val, exp_tb):
        return exp_type in self.exeptions
k = 1
with Timer(IndexError, KeyError, ZeroDivisionError, AttributeError):
    k = k / 0

