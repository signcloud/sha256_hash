from hash.celery import app
from hash.settings import BASE_DIR
from .models import HashesModel
import subprocess as sp
import os
import time


def save_to_file(input_data):
    file_path = os.path.join(
        BASE_DIR, f'hash/hashes/{time.strftime("%Y-%m-%d-%H:%M")}.txt')
    print(file_path)
    with open(file_path, 'w') as file:
        file.write(input_data)


def get_or_none(model, **kwargs):
    try:
        model.objects.filter(**kwargs)
    except Exeption as e:
        return None


def log(error):
    os.path.join(BASE_DIR, f'hash/log.txt')
    with open('log.txt', 'a') as log_file:
        log_file.write(error + '\n')


@app.task
def hash_func(path):
    hash_db = HashesModel
    main = os.path.join(BASE_DIR, 'hash/main.py')
    output = sp.getoutput(f"python3 {main} {path}")
    save_to_file(output)
    if output:
        output_list = output.split('\n')
        log(output_list[0] + '\n')
        for line in output_list:
            file_hash = line.split(" ")
            log(line)
            if file_hash[1]:
                log(file_hash[1])
            log(f'File hash = {file_hash[1]}')

            if get_or_none(hash_db, file=file_hash[1]):
                # print(query.values('file'))
                return "Exists"
            else:
                hash_db.objects.create(file=file_hash[1], hash=file_hash[0])

    return 'Done! Check your hashes.'
