### Multi processing real world example with factorial calculations

import multiprocessing
import math
import sys
import time

sys.set_int_max_str_digits(100000)

def calculate_factorial(num):
    print(f"Calculating factorial for number {num}")
    result = math.factorial(num)
    print(f"Factorial of {num} is {result}")
    return result

numbers = [1200, 4000, 5200, 6800]

if __name__ == "__main__":
    start_time = time.time()

    with multiprocessing.Pool() as pool:
        results = pool.map(calculate_factorial, numbers)

    print(f"Results are {results}")
    print(f"Total time of execution in seconds {time.time() - start_time}")