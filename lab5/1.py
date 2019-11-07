import time

class Timer():
    def __init__(self):
        self.time_in = 0
        self.time_out = 0
        
    def __enter__(self):
        self.time_in = time.time()
        
    def __exit__(self, exp_type, exp_val, exp_tb):
        self.time_out = time.time()
        print(self.time_out - self.time_in)

with Timer():
    timesleep(0.2)
