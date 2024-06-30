import unittest
from unittest.mock import patch
from get_gitlab_issues import check_access, get_gitlab_issues, get_gitlab_issue


class TestGitLabFunctions(unittest.TestCase):
    def setUp(self):
        self.token = 'fake_token'
        self.url = 'http://fake-url.com'
        self.project_id = '123'
        self.issue_id = '456'
        self.headers = {'Private-Token': self.token}

    @patch('requests.get')
    def test_check_access_valid(self, mock_get):
        mock_get.return_value.status_code = 200
        self.assertTrue(check_access(self.token, self.url))

    @patch('requests.get')
    def test_check_access_invalid(self, mock_get):
        mock_get.return_value.status_code = 401
        self.assertFalse(check_access(self.token, self.url))

    @patch('requests.get')
    def test_get_gitlab_issues(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{'id': 1, 'title': 'Issue 1'}]
        issues = get_gitlab_issues(self.token, self.url, self.project_id)
        self.assertIsInstance(issues, list)
        self.assertEqual(issues[0]['title'], 'Issue 1')

    @patch('requests.get')
    def test_get_gitlab_issue(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'id': self.issue_id, 'title': 'Specific Issue'}
        issue = get_gitlab_issue(self.token, self.url, self.project_id, self.issue_id)
        self.assertIsInstance(issue, dict)
        self.assertEqual(issue['title'], 'Specific Issue')

    @patch('requests.get')
    def test_get_gitlab_issue_not_found(self, mock_get):
        mock_get.return_value.status_code = 404
        issue = get_gitlab_issue(self.token, self.url, self.project_id, self.issue_id)
        self.assertIsNone(issue)


if __name__ == '__main__':
    unittest.main()