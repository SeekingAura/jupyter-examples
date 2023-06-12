import unittest

import requests_mock

from github_cmd import GithubCmd

from .mock_github_cmd import MockGetGithubUserData


class TestGetGithubUserData(unittest.TestCase):
    # Set up the mock adapter
    def setUp(self):
        self.mock = MockGetGithubUserData()
        self.adapter = requests_mock.Adapter()
        self.adapter.register_uri(
            "GET", "https://api.github.com/user", json=self.mock.github_user
        )

    def test_get_github_user_data(self):
        github_cmd = GithubCmd(github_token=self.mock.github_token)
        github_cmd.set_http_adapter(http_adapter=self.adapter)

        result = github_cmd.get_github_user_data()

        self.assertIsInstance(result, dict)

        self.assertEqual(set(result.keys()), set(self.mock.github_user.keys()))

        for key in self.mock.github_user:
            self.assertEqual(result.get(key), self.mock.github_user.get(key))
