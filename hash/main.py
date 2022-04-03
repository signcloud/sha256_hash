import hashlib
import multiprocessing
import os
import time
import sys


def get_hash_sha256(filename):
    # filesize = os.path.getsize(filename)
    # print(
    #     'Counting hash for file: ' + filename + f' with process {multiprocessing.current_process().name} on'
    #                                             f' {time.ctime()}')
    with open(filename, 'rb') as f:
        m = hashlib.sha256()
        while True:
            data = f.read(8192)
            if not data:
                break
            m.update(data)
        return f'{m.hexdigest()} {filename}'


def find_all_files(root_path):
    files_list = []
    for root, dirs, files in os.walk(root_path, topdown=True):
        for name in files:
            filepath = os.path.join(root, name)
            if os.path.exists(filepath):
                files_list.append(filepath)
    return files_list


def print_func(response):
    for line in response:
        print(line)


path = sys.argv[1] if len(sys.argv) > 1 else './'
processes = int(sys.argv[2]) if len(sys.argv) > 2 else 5

if __name__ == '__main__':
    # print('Counting hashes in ' + path)
    st_time = time.time()
    with multiprocessing.Pool(multiprocessing.cpu_count() * processes) as p:
        p.map_async(get_hash_sha256, find_all_files(path), callback=print_func)
        p.close()
        p.join()  #
    end_time = time.time()
    diff_time = end_time - st_time

    # print(diff_time, 'Processes/CPU core:', processes, 'CPU cores:', multiprocessing.cpu_count())