from tests import fake


class MockGetGithubUserData:
    def __init__(self):
        self.fake = fake
        self.create_mock()

    def create_mock(self):
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
        self.github_token = self.fake.pystr_format(
            string_format=f'{"?"*18}',
            letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        )
