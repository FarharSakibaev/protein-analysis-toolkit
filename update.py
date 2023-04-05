import subprocess

import requests

from config import PROJECT_PATH


def git_is_installed() -> bool:
    try:
        result = subprocess.run(['git', '--version'], capture_output=True, text=True)
        print(result.stdout)
        return True
    except FileNotFoundError:
        print('Please install Git on your PC if you want to fetch updates')
        return False


def update() -> None:
    if not git_is_installed():
        return

    file_path = f'{PROJECT_PATH}/version.txt'

    with open(file_path, 'r') as version_file:
        version = version_file.read().strip().replace('\n', '')

    owner = 'FarharSakibaev'
    repo = 'protein-analysis-toolkit'

    response = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits/master')
    latest_commit = response.json()

    latest_version = latest_commit['sha']

    if version != latest_version or latest_version not in version:
        subprocess.run(["git", "checkout", "master"])
        subprocess.run(["git", "pull"])

        with open(file_path, 'w') as version_file:
            version_file.write(latest_version)
        exit('Project updated, please run the application again')
    else:
        print('Nothing to update')


if __name__ == '__main__':
    update()
