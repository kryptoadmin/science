### Multi threading using thread pool executor

from concurrent.futures import ThreadPoolExecutor
import time


def print_names(name):
    time.sleep(1)
    return name


names = ["Dilip", "Sandhya", "Anusha", "Reddamma", "Swathi"]

current_time = time.time()
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_names, names)

for result in results:
    print(result)

print(f"Time taken to execute: {time.time() - current_time}")