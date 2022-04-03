from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import PathForm
from .tasks import hash_func
from .models import HashesModel
import os

BASE_DIR = settings.BASE_DIR


def show_parsed(request, filename):
    hash_db = HashesModel
    file_to_read = os.path.join(BASE_DIR, f'hash/hashes/{filename}')
    with open(file_to_read) as file:
        file_content = file.read()
        content = file_content.split('\n')
        for line in content:
            file_hash = line.split()
            query = hash_db.objects.filter(hash=file_hash[0])
            if query:
                return HttpResponse(query.values())
                continue
            else:
                hash_db.objects.create(file=file_hash[1], hash=file_hash[0])
    return HttpResponse(content)


def show(request, filename=0):
    file_to_read = os.path.join(BASE_DIR, f'hash/hashes/{filename}')
    if os.path.exists(file_to_read):
        with open(file_to_read, 'r') as f:
            content = f.readlines()
        hashes_list = '<br>'.join(content)
        return HttpResponse(f'{hashes_list}')  # temp.replace('\n', '<br>')
    else:
        return redirect('hashes')


def write(request):
    file_to_read = os.path.join(BASE_DIR, 'hash/hashes/file.txt')
    try:
        with open(file_to_read, 'w') as f:
            temp = f.write("Hello")
    except IOError as e:
        print(e)
        return HttpResponse(e)

    print('Hello')
    return HttpResponse("Wrote...")


def read(request):
    file_to_read = os.path.join(BASE_DIR, 'hash/hashes/file.txt')
    with open(file_to_read, 'r') as f:
        temp = f.read()
    return HttpResponse(temp)


def hashes(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dir_path = os.path.join(BASE_DIR, 'hash/hashes/')
    files_list = os.listdir(dir_path)
    file_path = os.path.join(BASE_DIR, './out.txt')
    with open(file_path, 'w') as file:
        file.write('Hello')
    # files_list_string = ' '.join(files_list)
    return render(request, 'hash/list.html', {'files_list': files_list})


def test(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PathForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            hash_func.delay(request.POST['path'])
            return redirect('hashes/')
    else:
        form = PathForm()

    return render(request, 'hash/path.html', {'form': form})
