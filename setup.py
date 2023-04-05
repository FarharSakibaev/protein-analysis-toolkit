import os

from config import PROJECT_PATH


def setup():
    dirs_to_create = ['input', 'output']
    files_to_create = ['version.txt']

    for dir_path in dirs_to_create:
        dir_path = f'{PROJECT_PATH}/{dir_path}'
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

    for file_path in files_to_create:
        file_path = f'{PROJECT_PATH}/{file_path}'
        with open(file_path, 'w') as file:
            file.write('')


if __name__ == '__main__':
    setup()
