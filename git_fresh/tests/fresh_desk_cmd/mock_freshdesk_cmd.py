import sys

from uuid import uuid4

from tests import fake


class MockSerializeContactFromGit:
    def __init__(self):
        self.fake = fake
        self.create_mock()

    def create_mock(self):
        self.fresh_subdomain = self.fake.hostname(0)
        self.fresh_token = self.fake.pystr_format(
            string_format=f'{"?"*18}',
            letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        )

        username = self.fake.user_name()
        account_id: int = self.fake.unique.random_int()
        created_at = self.fake.date_time_between()
        updated_at = self.fake.date_time_between(start_date=created_at)
        self.github_user = {
            "login": username,
            "id": account_id,
            "node_id": fake.pystr_format(
                string_format=f'{"?"*18}==',
                letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
            ),
            "avatar_url": f"https://avatars.githubusercontent.com/u/{account_id}?v=4",
            "gravatar_id": "",
            "url": f"https://api.github.com/users/{username}",
            "html_url": f"https://github.com/{username}",
            "followers_url": f"https://api.github.com/users/{username}/followers",
            "following_url": f"https://api.github.com/users/{username}/following{{/other_user}}",
            "gists_url": f"https://api.github.com/users/{username}/gists{{/gist_id}}",
            "starred_url": f"https://api.github.com/users/{username}/starred{{/owner}}{{/repo}}",
            "subscriptions_url": f"https://api.github.com/users/{username}/subscriptions",
            "organizations_url": f"https://api.github.com/users/{username}/orgs",
            "repos_url": f"https://api.github.com/users/{username}/repos",
            "events_url": f"https://api.github.com/users/{username}/events/{{/privacy}}",
            "received_events_url": f"https://api.github.com/users/{username}/received_events",
            "type": "User",
            "site_admin": False,
            "name": self.fake.name(),
            "company": None,
            "blog": "",
            "location": f"{self.fake.country()}, {self.fake.city()}",
            "email": self.fake.ascii_email(),
            "hireable": None,
            "bio": self.fake.text(max_nb_chars=50),
            "twitter_username": None,
            "public_repos": self.fake.random_int(min=0, max=100),
            "public_gists": self.fake.random_int(min=0, max=100),
            "followers": self.fake.random_int(min=0, max=100),
            "following": self.fake.random_int(min=0, max=100),
            "created_at": created_at.strftime(
                "%Y-%m-%dT%H:%M:%S:Z",
            ),
            "updated_at": updated_at.strftime(
                "%Y-%m-%dT%H:%M:%S:Z",
            ),
        }

        self.fresh_git_contact = {
            "name": self.github_user.get("name"),
            "email": self.github_user.get("email"),
            "address": self.github_user.get("location"),
            "description": self.github_user.get("bio"),
        }


class MockUpdateContact:
    def __init__(self):
        self.fake = fake
        self.create_mock()

    def create_mock(self):
        self.fresh_subdomain = self.fake.hostname(0)
        self.fresh_token = self.fake.pystr_format(
            string_format=f'{"?"*18}',
            letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        )

        username = self.fake.user_name()
        account_id: int = self.fake.unique.random_int()
        github_created_at = self.fake.date_time_between()
        github_updated_at = self.fake.date_time_between(start_date=github_created_at)
        self.github_user = {
            "login": username,
            "id": account_id,
            "node_id": fake.pystr_format(
                string_format=f'{"?"*18}==',
                letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
            ),
            "avatar_url": f"https://avatars.githubusercontent.com/u/{account_id}?v=4",
            "gravatar_id": "",
            "url": f"https://api.github.com/users/{username}",
            "html_url": f"https://github.com/{username}",
            "followers_url": f"https://api.github.com/users/{username}/followers",
            "following_url": f"https://api.github.com/users/{username}/following{{/other_user}}",
            "gists_url": f"https://api.github.com/users/{username}/gists{{/gist_id}}",
            "starred_url": f"https://api.github.com/users/{username}/starred{{/owner}}{{/repo}}",
            "subscriptions_url": f"https://api.github.com/users/{username}/subscriptions",
            "organizations_url": f"https://api.github.com/users/{username}/orgs",
            "repos_url": f"https://api.github.com/users/{username}/repos",
            "events_url": f"https://api.github.com/users/{username}/events/{{/privacy}}",
            "received_events_url": f"https://api.github.com/users/{username}/received_events",
            "type": "User",
            "site_admin": False,
            "name": self.fake.name(),
            "company": None,
            "blog": "",
            "location": f"{self.fake.country()}, {self.fake.city()}",
            "email": self.fake.ascii_email(),
            "hireable": None,
            "bio": self.fake.text(max_nb_chars=50),
            "twitter_username": None,
            "public_repos": self.fake.random_int(min=0, max=100),
            "public_gists": self.fake.random_int(min=0, max=100),
            "followers": self.fake.random_int(min=0, max=100),
            "following": self.fake.random_int(min=0, max=100),
            "created_at": github_created_at.strftime(
                "%Y-%m-%dT%H:%M:%S:Z",
            ),
            "updated_at": github_updated_at.strftime(
                "%Y-%m-%dT%H:%M:%S:Z",
            ),
        }

        self.github_avatar_bytes = self.fake.binary(length=64)
        self.fresh_contact = {
            "name": self.github_user.get("name"),
            "email": self.github_user.get("email"),
            "phone": None,
            "mobile": None,
            "twitter_id": None,
            "unique_external_id": None,
            "other_emails": None,
            "company_id": None,
            "view_all_tickets": None,
            "other_companies": None,
            "address": self.github_user.get("location"),
            "avatar": self.github_user.get("avatar_url"),
            "custom_fields": None,
            "description": self.github_user.get("bio"),
            "job_title": None,
            "language": None,
            "tags": None,
            "time_zone": None,
        }

        fresh_avatar_created_at = self.fake.date_time_between()
        fresh_avatar_updated_at = self.fake.date_time_between(
            start_date=fresh_avatar_created_at,
        )
        fresh_updated_at = self.fake.date_time_between(
            start_date=github_created_at,
        )
        self.fresh_contact_result = {
            "active": True,
            "address": self.github_user.get("location"),
            "avatar": {
                "attachment_type": "Attachment",
                "content_type": "image/png",
                "created_at": fresh_avatar_created_at.strftime(
                    "%Y-%m-%dT%H:%M:%S:Z",
                ),
                "deleted": False,
                "file_name": "avatar.png",
                "id": self.fake.random_int(),
                "size": sys.getsizeof(self.github_avatar_bytes),
                "updated_at": fresh_avatar_updated_at.strftime(
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
            "id": self.fake.random_int(),
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
            "updated_at": fresh_updated_at.strftime(
                "%Y-%m-%dT%H:%M:%S:Z",
            ),
            "verified": True,
            "view_all_tickets": False,
            "visitor_id": str(uuid4()),
        }


class MockCreateContact:
    def __init__(self):
        self.fake = fake
        self.create_mock()

    def create_mock(self):
        self.fresh_subdomain = self.fake.hostname(0)
        self.fresh_token = self.fake.pystr_format(
            string_format=f'{"?"*18}',
            letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        )

        username = self.fake.user_name()
        account_id: int = self.fake.unique.random_int()
        github_created_at = self.fake.date_time_between()
        github_updated_at = self.fake.date_time_between(start_date=github_created_at)
        self.github_user = {
            "login": username,
            "id": account_id,
            "node_id": fake.pystr_format(
                string_format=f'{"?"*18}==',
                letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
            ),
            "avatar_url": f"https://avatars.githubusercontent.com/u/{account_id}?v=4",
            "gravatar_id": "",
            "url": f"https://api.github.com/users/{username}",
            "html_url": f"https://github.com/{username}",
            "followers_url": f"https://api.github.com/users/{username}/followers",
            "following_url": f"https://api.github.com/users/{username}/following{{/other_user}}",
            "gists_url": f"https://api.github.com/users/{username}/gists{{/gist_id}}",
            "starred_url": f"https://api.github.com/users/{username}/starred{{/owner}}{{/repo}}",
            "subscriptions_url": f"https://api.github.com/users/{username}/subscriptions",
            "organizations_url": f"https://api.github.com/users/{username}/orgs",
            "repos_url": f"https://api.github.com/users/{username}/repos",
            "events_url": f"https://api.github.com/users/{username}/events/{{/privacy}}",
            "received_events_url": f"https://api.github.com/users/{username}/received_events",
            "type": "User",
            "site_admin": False,
            "name": self.fake.name(),
            "company": None,
            "blog": "",
            "location": f"{self.fake.country()}, {self.fake.city()}",
            "email": self.fake.ascii_email(),
            "hireable": None,
            "bio": self.fake.text(max_nb_chars=50),
            "twitter_username": None,
            "public_repos": self.fake.random_int(min=0, max=100),
            "public_gists": self.fake.random_int(min=0, max=100),
            "followers": self.fake.random_int(min=0, max=100),
            "following": self.fake.random_int(min=0, max=100),
            "created_at": github_created_at.strftime(
                "%Y-%m-%dT%H:%M:%S:Z",
            ),
            "updated_at": github_updated_at.strftime(
                "%Y-%m-%dT%H:%M:%S:Z",
            ),
        }

        self.github_avatar_bytes = self.fake.binary(length=64)
        self.fresh_contact = {
            "name": self.github_user.get("name"),
            "email": self.github_user.get("email"),
            "phone": None,
            "mobile": None,
            "twitter_id": None,
            "unique_external_id": None,
            "other_emails": None,
            "company_id": None,
            "view_all_tickets": None,
            "other_companies": None,
            "address": self.github_user.get("location"),
            "avatar": self.github_user.get("avatar_url"),
            "custom_fields": None,
            "description": self.github_user.get("bio"),
            "job_title": None,
            "language": None,
            "tags": None,
            "time_zone": None,
        }

        fresh_avatar_created_at = self.fake.date_time_between()
        fresh_avatar_updated_at = self.fake.date_time_between(
            start_date=fresh_avatar_created_at,
        )
        fresh_updated_at = self.fake.date_time_between(
            start_date=github_created_at,
        )
        self.fresh_contact_result = {
            "active": True,
            "address": self.github_user.get("location"),
            "avatar": {
                "attachment_type": "Attachment",
                "content_type": "image/png",
                "created_at": fresh_avatar_created_at.strftime(
                    "%Y-%m-%dT%H:%M:%S:Z",
                ),
                "deleted": False,
                "file_name": "avatar.png",
                "id": self.fake.random_int(),
                "size": sys.getsizeof(self.github_avatar_bytes),
                "updated_at": fresh_avatar_updated_at.strftime(
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
            "id": self.fake.random_int(),
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
            "updated_at": fresh_updated_at.strftime(
                "%Y-%m-%dT%H:%M:%S:Z",
            ),
            "verified": True,
            "view_all_tickets": False,
            "visitor_id": str(uuid4()),
        }
