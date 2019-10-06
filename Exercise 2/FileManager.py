import os

def file_exists(name):
    if os.path.exists(name):
        open('Plithos.txt', 'w').close()
