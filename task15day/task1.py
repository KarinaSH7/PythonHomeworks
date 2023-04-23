'Напишите функиию, которая считает время выполнение этой функци'
import time
def func_to_decor():
    for i in range(1000):
        print(i)

def measure_time(func):
    start_time = time.time()
    func()
    end_time = time.time()
    print("Time taken: ", end_time - start_time, "seconds")

measure_time(func_to_decor)