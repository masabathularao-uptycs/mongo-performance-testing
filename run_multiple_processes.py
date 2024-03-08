import multiprocessing
import os

def run_process():
    # Replace 'your_script.py' with the name of your Python file
    os.system("python load.py")

if __name__ == '__main__':
    num_processes = 18
    processes = []

    for _ in range(num_processes):
        p = multiprocessing.Process(target=run_process)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
