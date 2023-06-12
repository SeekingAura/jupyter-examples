from datetime import datetime
from typing import TypedDict


class Plan:
    name: str
    space: int
    collaborators: int
    private_repos: int

    def __init__(
        self, name: str, space: int, collaborators: int, private_repos: int
    ) -> None:
        self.name = name
        self.space = space
        self.collaborators = collaborators
        self.private_repos = private_repos


class GithubUserData(TypedDict):
    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: str
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    site_admin: bool
    name: str
    company: None
    blog: str
    location: str
    email: str
    hireable: None
    bio: str
    twitter_username: None
    public_repos: int
    public_gists: int
    followers: int
    following: int
    created_at: datetime
    updated_at: datetime
    private_gists: int
    total_private_repos: int
    owned_private_repos: int
    disk_usage: int
    collaborators: int
    two_factor_authentication: bool
    plan: Plan

