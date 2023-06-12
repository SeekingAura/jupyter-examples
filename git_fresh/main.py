import argparse

import settings
from _typing import (
    FreshContactCreateGithub,
    FreshContactResult,
    GithubUserData,
)
from freshdesk_cmd import FreshdeskCmd
from github_cmd import GithubCmd

parser: argparse.ArgumentParser = argparse.ArgumentParser(
    description="Create contacts on freshdesk, check env file",
)
args: argparse.Namespace = parser.parse_args()

if __name__ == "__main__":
    if (
        not settings.GITHUB_TOKEN
        or not settings.FRESHDESK_SUBDOMAIN
        or not settings.FRESHDESK_TOKEN
    ):
        raise ValueError(
            "Some required vars not configured, check env-base file",
        )
    github_cmd = GithubCmd(github_token=settings.GITHUB_TOKEN)
    freshdesk_cmd = FreshdeskCmd(
        subdomain=settings.FRESHDESK_SUBDOMAIN,
        freshdesk_token=settings.FRESHDESK_TOKEN,
    )

    user_data: GithubUserData = github_cmd.get_github_user_data()
    contact_data: FreshContactCreateGithub = freshdesk_cmd.serialize_contact_from_git(
        user_data=user_data,
    )
    _: FreshContactResult = freshdesk_cmd.create_contact(
        contact_data=contact_data,
    )
