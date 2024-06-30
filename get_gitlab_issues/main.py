import requests
from urllib.parse import urlencode


def check_access(token, url):
    headers = {'Private-Token': token}
    response = requests.get(f"{url}/user", headers=headers)
    return response.status_code == 200


def get_gitlab_issues(token, url, project_id, labels=None, iteration_id=None):
    headers = {'Private-Token': token}
    url = f"{url}/projects/{project_id}/issues?labels={labels}&iteration_id={iteration_id}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_gitlab_issue(token, url, project_id, issue_id):
    headers = {'Private-Token': token}
    response = requests.get(f"{url}/projects/{project_id}/issues/{issue_id}", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

