import gitlab


def check_access(token, gitlab_url):
    gl = gitlab.Gitlab(url=gitlab_url, private_token=token)
    try:
        user = gl.user
        return True
    except gitlab.exceptions.GitlabAuthenticationError:
        return False


def get_gitlab_issues(token, gitlab_url, group_id, labels=None, iteration_id=None):
    gl = gitlab.Gitlab(url=gitlab_url, private_token=token)
    group = gl.groups.get(id=group_id)
    issues = group.issues.list(labels=labels, iteration_id=iteration_id, get_all=True)
    return issues


def get_gitlab_issue(token, gitlab_url, project_id, issue_id):
    gl = gitlab.Gitlab(url=gitlab_url, private_token=token)
    project = gl.projects.get(project_id)
    issue = project.issues.get(issue_id)
    return issue.attributes
