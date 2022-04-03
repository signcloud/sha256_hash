import subprocess as sp
import os
# from .services import save_to_file

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
main = os.path.join(BASE_DIR, 'hash/main.py')
output = sp.getoutput(f"python3 {main} ./")


def save_to_file(input_data):
    file_path = os.path.join('hashes/', 'file.txt')
    with open('hashes/file.txt', 'w') as file:
        file.write(input_data)

print(output)
files_list = []
save_to_file(output)

for root, dirs, files in os.walk('./hashes'):
    for name in files:
        filepath = os.path.join(root, name)
        if os.path.exists(filepath):
            files_list.append(filepath)
    print(files_list)
