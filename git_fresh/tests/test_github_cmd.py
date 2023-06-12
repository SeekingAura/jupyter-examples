import unittest
from datetime import datetime

import requests_mock

from github_cmd import GithubCmd

# Mock response for the github api
mock_response = {
    "login": "testuser",
    "id": 123456,
    "node_id": "MDQ6VXNlcjEyMzQ1Ng==",
    "avatar_url": "https://avatars.githubusercontent.com/u/123456?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/testuser",
    "html_url": "https://github.com/testuser",
    "followers_url": "https://api.github.com/users/testuser/followers",
    "following_url": "https://api.github.com/users/testuser/following{/other_user}",
    "gists_url": "https://api.github.com/users/testuser/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/testuser/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/testuser/subscriptions",
    "organizations_url": "https://api.github.com/users/testuser/orgs",
    "repos_url": "https://api.github.com/users/testuser/repos",
    "events_url": "https://api.github.com/users/testuser/events{/privacy}",
    "received_events_url": "https://api.github.com/users/testuser/received_events",
    "type": "User",
    "site_admin": False,
    "name": "Test User",
    "company": None,
    "blog": "",
    "location": "",
    "email": "",
    "hireable": None,
    "bio": "",
    "twitter_username": None,
    "public_repos": 10,
    "public_gists": 0,
    "followers": 0,
    "following": 0,
    "created_at": datetime(2022, 1, 1, 0, 0, 0).strftime(
        "%Y-%m-%dT%H:%M:%S:Z",
    ),
    "updated_at": datetime(2022, 1, 2, 0, 0, 0).strftime(
        "%Y-%m-%dT%H:%M:%S:Z",
    ),
    "private_gists": 0,
    "total_private_repos": 1,
    "owned_private_repos": 1,
    "disk_usage": 100,
    "collaborators": 0,
    "two_factor_authentication": False,
    "plan": {
        "name": "free",
        "space": 976562499,
        "collaborators": 0,
        "private_repos": 10000,
    },
}

mock_token = "abcdefg"


class TestGetGithubUserData(unittest.TestCase):
    # Set up the mock adapter
    def setUp(self):
        self.adapter = requests_mock.Adapter()
        self.adapter.register_uri(
            "GET", "https://api.github.com/user", json=mock_response
        )

    def test_get_github_user_data(self):
        github_cmd = GithubCmd(github_token=mock_token)
        github_cmd.set_http_adapter(http_adapter=self.adapter)

        result = github_cmd.get_github_user_data()

        self.assertIsInstance(result, dict)

        self.assertEqual(set(result.keys()), set(mock_response.keys()))

        for key in mock_response:
            self.assertEqual(result.get(key), mock_response.get(key))
