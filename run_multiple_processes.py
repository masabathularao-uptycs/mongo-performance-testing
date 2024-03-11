# import multiprocessing
# import os

# def run_process():
#     # Replace 'your_script.py' with the name of your Python file
#     os.system("/usr/local/bin/python3 load.py")

# if __name__ == '__main__':
#     num_processes = 82
#     processes = []

#     for _ in range(num_processes):
#         p = multiprocessing.Process(target=run_process)
#         p.start()
#         processes.append(p)

#     for p in processes:
#         p.join()

#for i in {1..82}; do nohup /usr/local/bin/python3 load.py & done