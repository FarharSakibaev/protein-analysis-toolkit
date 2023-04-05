import subprocess
from datetime import datetime, timedelta

import requests


def git_is_installed() -> bool:
    try:
        result = subprocess.run(['git', '--version'], capture_output=True, text=True)
        print(result.stdout)
        return True
    except FileNotFoundError:
        print('Please install Git on your PC if you want to fetch updates')
        return False


def get_last_commit() -> dict:
    try:
        output = subprocess.check_output(['git', 'log', '-1'], stderr=subprocess.STDOUT)
        output = output.decode('utf-8').split('\n')

        last_version = output[0].replace('commit', '').strip()
        date = output[2].replace('Date:', '').strip()

        return {
            'local_version': last_version,
            'date': datetime.strptime(date[:-6], "%a %b %d %H:%M:%S %Y")
        }
    except subprocess.CalledProcessError as e:
        print("Error:", e.output)


def update() -> None:
    if not git_is_installed():
        return

    local_version_data = get_last_commit()
    delta = datetime.now() - local_version_data['date']
    version = local_version_data['local_version']

    owner = 'FarharSakibaev'
    repo = 'protein-analysis-toolkit'

    response = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits/master')
    latest_commit = response.json()

    latest_version = latest_commit['sha']

    if delta < timedelta(days=1) and version != latest_version or latest_version not in version:
        subprocess.run(["git", "checkout", "master"])
        subprocess.run(["git", "pull"])
        exit('Project updated, please run the application again')
    else:
        print('Nothing to update')


if __name__ == '__main__':
    update()
