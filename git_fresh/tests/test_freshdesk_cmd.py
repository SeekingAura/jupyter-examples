import unittest
import requests_mock
from datetime import datetime
from uuid import uuid4

from freshdesk_cmd import FreshdeskCmd

mock_github_user = {
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
    "email": "test@example.com",
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
}

mock_github_avatar_bytes = b"\xff\xd8\xff\xdb\x00\x84\x00\x08\x06\x06\x07\x06\x05\x08\x07\x07\x07\t\t\x08\n\x0c\x14\r\x0c\x0b\x0b\x0c\x19\x12\x13\x0f\x14\x1d\x1a\x1f\x1e\x1d\x1a\x1c\x1c"

mock_fresh_git_contact = {
    "name": "Test User",
    "email": "test@example.com",
    "address": "",
    "avatar": "https://avatars.githubusercontent.com/u/123456?v=4",
    "description": "",
}

mock_fresh_contact = {
    "name": "Test User",
    "email": "test@example.com",
    "phone": None,
    "mobile": None,
    "twitter_id": None,
    "unique_external_id": None,
    "other_emails": None,
    "company_id": None,
    "view_all_tickets": None,
    "other_companies": None,
    "address": "",
    "avatar": "https://avatars.githubusercontent.com/u/123456?v=4",
    "custom_fields": None,
    "description": "",
    "job_title": None,
    "language": None,
    "tags": None,
    "time_zone": None,
}

mock_fresh_contact_result = {
    "active": True,
    "address": None,
    "avatar": {
        "attachment_type": "Attachment",
        "content_type": "image/png",
        "created_at": datetime(2022, 1, 3, 0, 0, 0).strftime(
            "%Y-%m-%dT%H:%M:%S:Z",
        ),
        "deleted": False,
        "file_name": "avatar.png",
        "id": 1234567890,
        "size": 10000,
        "updated_at": datetime(2022, 1, 3, 0, 0, 0).strftime(
            "%Y-%m-%dT%H:%M:%S:Z",
        ),
        "url": "/contacts/1234567890/avatar",
    },
    "company_id": None,
    "csat_rating": None,
    "custom_fields": {},
    "deleted": False,
    "description": "",
    "email": "",
    "facebook_id": None,
    "first_name": "",
    "followers_count": 0,
    "following_count": 0,
    "id": 1234567890,
    "job_title": "",
    "language": "",
    "last_name": "",
    "mobile": None,
    "name": "",
    "other_companies_count": 0,
    "other_emails_count": 0,
    "other_emails_unverified_count": 0,
    "other_phones_count": 0,
    "phone": None,
    "preferred_source": None,
    "tags": [],
    "time_zone": "",
    "twitter_id": None,
    "unique_external_id": None,
    "updated_at": datetime(2022, 1, 3, 0, 0, 0).strftime(
        "%Y-%m-%dT%H:%M:%S:Z",
    ),
    "verified": True,
    "view_all_tickets": False,
    "visitor_id": str(uuid4()),
}

mock_subdomain = "test"
mock_token = "abcdefg"


class TestSerializeContactFromGit(unittest.TestCase):
    def test_serialize_contact_from_git(self):
        freshdesk_cmd = FreshdeskCmd(
            subdomain=mock_subdomain,
            freshdesk_token=mock_token,
        )
        result = freshdesk_cmd.serialize_contact_from_git(mock_github_user)

        self.assertIsInstance(result, dict)

        self.assertEqual(set(result.keys()), set(mock_fresh_git_contact.keys()))

        for key in mock_fresh_git_contact:
            self.assertEqual(result[key], mock_fresh_git_contact[key])


class TestUpdateContact(unittest.TestCase):
    def setUp(self):
        self.adapter = requests_mock.Adapter()
        self.adapter.register_uri(
            "PUT",
            f"https://{mock_subdomain}.freshdesk.com/api/v2/contacts/{mock_github_user.get('id')}",
            json=mock_fresh_contact_result,
        )
        self.adapter.register_uri(
            "GET",
            mock_github_user.get("avatar_url"),
            content=mock_github_avatar_bytes,
        )

    def test_update_contact(self):
        freshdesk_cmd = FreshdeskCmd(
            subdomain=mock_subdomain,
            freshdesk_token=mock_token,
        )
        freshdesk_cmd.set_http_adapter(http_adapter=self.adapter)

        result = freshdesk_cmd.update_contact(
            mock_github_user.get("id"),
            mock_fresh_contact,
        )

        self.assertIsInstance(result, dict)

        self.assertEqual(set(result.keys()), set(mock_fresh_contact_result.keys()))

        for key in mock_fresh_contact_result:
            self.assertEqual(result[key], mock_fresh_contact_result[key])
