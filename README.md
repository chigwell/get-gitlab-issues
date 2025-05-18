[![PyPI version](https://badge.fury.io/py/get-gitlab-issues.svg)](https://badge.fury.io/py/get-gitlab-issues)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/get-gitlab-issues)](https://pepy.tech/project/get-gitlab-issues)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue)](https://www.linkedin.com/in/eugene-evstafev-716669181/)

# Get GitLab Issues

`Get GitLab Issues` is a Python package designed to facilitate the extraction and management of issues from GitLab repositories. This tool is essential for developers looking to streamline their issue tracking processes directly through Python scripts.

## Installation

To install `Get GitLab Issues`, you can use pip:

```bash
pip install get-gitlab-issues
```

## Usage

`Get GitLab Issues` provides a straightforward API to interact with GitLab issues. Below is an example of how to use the package to retrieve issues and check user access:

### Example

```python
from get_gitlab_issues import check_access, get_gitlab_issues, get_gitlab_issue

# Check user access
if check_access('YOUR_PRIVATE_TOKEN', 'https://gitlab.example.com'):
    print("Access verified")

# Fetch issues for a specific group
issues = get_gitlab_issues('YOUR_PRIVATE_TOKEN', 'https://gitlab.example.com', '123456')
for issue in issues:
    print(issue.title, issue.description)

# Fetch a specific issue
issue_detail = get_gitlab_issue('YOUR_PRIVATE_TOKEN', 'https://gitlab.example.com', '123456', '1')
print(issue_detail.title, issue_detail.description)
```

## Functions

- `check_access(token, url)`: Checks if the provided token has access to the GitLab API.
- `get_gitlab_issues(token, url, group_id, labels=None, iteration_id=None)`: Retrieves a list of issues from a specified group.
- `get_gitlab_issue(token, url, project_id, issue_id)`: Retrieves details for a specific issue.

## Features

- Simple installation and easy usage.
- Efficient access to GitLab issues through the API.
- Ability to check user access and retrieve specific issues or lists of issues.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/chigwell/get-gitlab-issues/issues).

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
