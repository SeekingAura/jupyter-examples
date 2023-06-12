import json

from _typing import GithubUserData
from requests_http import RequestHttp


class GithubCmd(RequestHttp):
    def __init__(
        self,
        github_token: str,
    ):
        self.github_token = github_token
        super().__init__()

    def get_github_user_data(
        self,
    ) -> GithubUserData:
        url: str = "https://api.github.com/user"
        headers: dict[str, str] = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {self.github_token}",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        data = self.http_session.get(
            url=url,
            headers=headers,
        )

        return json.loads(data.text)
