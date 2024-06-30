[![GitHub release (latest by date)](https://img.shields.io/github/v/release/chigwell/get-gitlab-issues)](https://github.com/chigwell/get-gitlab-issues/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/get-gitlab-issues)](https://pepy.tech/project/get-gitlab-issues)

# Get GitLab Issues

`Get GitLab Issues` is a Python package designed to automate the extraction and management of issues from GitLab repositories. This tool is essential for developers looking to streamline their issue tracking processes directly through Python scripts.

## Installation

To install `Get GitLab Issues`, you can use pip:

```bash
pip install get-gitlab-issues
```

## Usage

`Get GitLab Issues` provides a straightforward API to interact with GitLab issues. Here is a basic example of how to use the package to retrieve issues:

### Example

```python
from get_gitlab_issues import GitLabIssueFetcher

# Initialize the issue fetcher for a specific repository
fetcher = GitLabIssueFetcher(repo_id='123456', private_token='YOUR_PRIVATE_TOKEN')

# Fetch issues
issues = fetcher.fetch_all_issues()
for issue in issues:
    print(issue.title, issue.description)
```

## Input Parameters

The main function `fetch_all_issues` in `GitLabIssueFetcher` class accepts several parameters:

- **repo_id** (`str`): The unique identifier for the GitLab repository.
- **private_token** (`str`): Your GitLab personal access token for authentication.

## Features

- Easy to install and use.
- Efficiently fetches issues from GitLab repositories.
- Suitable for developers and teams looking to automate their development workflows.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/chigwell/get-gitlab-issues/issues).

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).