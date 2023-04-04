import requests


if __name__ == '__main__':

    owner = 'FarharSakibaev'
    repo = 'protein-analysis-toolkit'

    response = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits/master')
    latest_commit = response.json()

    print(latest_commit['sha'])