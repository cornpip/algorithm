import time

start_t = 0
end_t = 0
def start():
    global start_t
    start_t = time.time()

def finish():
    global end_t
    end_t = time.time()
    print("ing time ==>", end_t - start_t)

def sleep(t):
    time.sleep(t)