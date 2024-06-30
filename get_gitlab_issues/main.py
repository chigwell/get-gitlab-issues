import requests


def check_access(token, url):
    headers = {'Private-Token': token}
    response = requests.get(f"{url}/user", headers=headers)
    return response.status_code == 200


def get_gitlab_issues(token, url, labels=None, iteration_id=None):
    headers = {'Private-Token': token}
    response = requests.get(f"{url}/issues?labels={labels}&iteration_id={iteration_id}", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_gitlab_issue(token, url, issue_id):
    headers = {'Private-Token': token}
    response = requests.get(f"{url}/issues/{issue_id}", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

