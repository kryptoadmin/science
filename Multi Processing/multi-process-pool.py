### Multi processing with process pool executor

from concurrent.futures import ProcessPoolExecutor
import time

def print_name(name):
    time.sleep(2)
    return f"Name is {name}"


names = ["Dilip", "Sandhya", "Lavanya", "Anusha", "Swetha", "Swathi"]

if __name__ == "__main__":
    current_time = time.time()
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(print_name, names)

    for result in results:
        print(result)
    
    print(f"Total time of execution {time.time() - current_time}")
