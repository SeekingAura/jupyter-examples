import unittest

import requests_mock
from .mock_freshdesk_cmd import (
    MockCreateContact,
    MockSerializeContactFromGit,
    MockUpdateContact,
)

from freshdesk_cmd import FreshdeskCmd


class TestSerializeContactFromGit(unittest.TestCase):
    def setUp(self):
        self.mock = MockSerializeContactFromGit()

    def test_serialize_contact_from_git(self):
        freshdesk_cmd = FreshdeskCmd(
            subdomain=self.mock.fresh_subdomain,
            freshdesk_token=self.mock.fresh_token,
        )
        result_contact, result_avatar_url = freshdesk_cmd.serialize_contact_from_git(
            user_data=self.mock.github_user,
        )

        self.assertIsInstance(result_contact, dict)
        self.assertIsInstance(result_avatar_url, str)

        self.assertEqual(
            set(result_contact.keys()),
            set(self.mock.fresh_git_contact.keys()),
        )

        for key in self.mock.fresh_git_contact:
            self.assertEqual(
                result_contact.get(key),
                self.mock.fresh_git_contact.get(key),
            )
        self.assertEqual(
            result_avatar_url,
            self.mock.github_user.get("avatar_url"),
        )


class TestUpdateContact(unittest.TestCase):
    def setUp(self):
        self.mock = MockUpdateContact()
        self.adapter = requests_mock.Adapter()
        self.adapter.register_uri(
            "PUT",
            f"https://{self.mock.fresh_subdomain}.freshdesk.com/api/v2/contacts/{self.mock.github_user.get('id')}",
            json=self.mock.fresh_contact_result,
        )
        self.adapter.register_uri(
            "GET",
            self.mock.github_user.get("avatar_url"),
            content=self.mock.github_avatar_bytes,
        )

    def test_update_contact(self):
        freshdesk_cmd = FreshdeskCmd(
            subdomain=self.mock.fresh_subdomain,
            freshdesk_token=self.mock.fresh_token,
        )
        freshdesk_cmd.set_http_adapter(http_adapter=self.adapter)

        result = freshdesk_cmd.update_contact(
            self.mock.github_user.get("id"),
            self.mock.fresh_contact,
        )

        self.assertIsInstance(result, dict)

        self.assertEqual(
            set(result.keys()),
            set(self.mock.fresh_contact_result.keys()),
        )

        for key in self.mock.fresh_contact_result:
            self.assertEqual(
                result.get(key),
                self.mock.fresh_contact_result.get(key),
            )


class TestCreateContact(unittest.TestCase):
    def setUp(self):
        self.mock = MockCreateContact()
        self.adapter = requests_mock.Adapter()
        self.adapter.register_uri(
            "POST",
            f"https://{self.mock.fresh_subdomain}.freshdesk.com/api/v2/contacts",
            json=self.mock.fresh_contact_result,
        )
        self.adapter.register_uri(
            "GET",
            self.mock.github_user.get("avatar_url"),
            content=self.mock.github_avatar_bytes,
        )

    def test_create_contact(self):
        freshdesk_cmd = FreshdeskCmd(
            subdomain=self.mock.fresh_subdomain,
            freshdesk_token=self.mock.fresh_token,
        )
        freshdesk_cmd.set_http_adapter(http_adapter=self.adapter)

        result = freshdesk_cmd.create_contact(
            self.mock.fresh_contact,
        )

        self.assertIsInstance(result, dict)

        self.assertEqual(
            set(result.keys()),
            set(self.mock.fresh_contact_result.keys()),
        )

        for key in self.mock.fresh_contact_result:
            self.assertEqual(
                result.get(key),
                self.mock.fresh_contact_result.get(key),
            )
