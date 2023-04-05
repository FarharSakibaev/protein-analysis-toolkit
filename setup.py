import os

from config import PROJECT_PATH, FETCH_UPDATES
from update import update


def setup():

    if FETCH_UPDATES:
        update()

    dirs_to_create = ['input', 'output']

    for dir_path in dirs_to_create:
        dir_path = f'{PROJECT_PATH}/{dir_path}'
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)


if __name__ == '__main__':
    setup()
