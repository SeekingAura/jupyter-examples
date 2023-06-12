import json
import logging

from _typing import (
    FreshContactCreate,
    FreshContactCreateConflict,
    FreshContactCreateDetailError,
    FreshContactCreateGithub,
    FreshContactResult,
    GithubUserData,
)
from requests_http import RequestHttp


class FreshdeskCmd(RequestHttp):
    def __init__(
        self,
        subdomain: str,
        freshdesk_token: str,
    ):
        self.subdomain = subdomain
        self.freshdesk_token = freshdesk_token
        super().__init__()

    def serialize_contact_from_git(
        self,
        user_data: GithubUserData,
    ) -> tuple[FreshContactCreateGithub, str]:
        contact_keys: dict[str, str] = {
            "name": "name",
            "email": "email",
            "location": "address",
            "bio": "description",
        }
        serialized_contact = dict()
        for git_key, fresh_key in contact_keys.items():
            serialized_contact[fresh_key] = user_data.get(git_key)

        return serialized_contact, user_data.get("avatar_url", "")

    def update_contact(
        self,
        user_id: int,
        contact_data: FreshContactCreate,
    ) -> FreshContactResult:
        url: str = f"https://{self.subdomain}.freshdesk.com/api/v2/contacts/{user_id}"
        headers: dict[str, str] = {
            "Content-Type": "application/json",
        }

        response_obj = self.http_session.put(
            url=url,
            json=contact_data,
            auth=(self.freshdesk_token, "X"),
            headers=headers,
        )

        if response_obj.status_code == 404:
            raise LookupError(
                f"User with email {contact_data.get('email')} already exist but is not a contact"
            )

        return json.loads(response_obj.text)

    def create_contact(
        self,
        contact_data: FreshContactCreate,
    ) -> FreshContactResult:
        url: str = f"https://{self.subdomain}.freshdesk.com/api/v2/contacts"
        headers: dict[str:str] = {
            "Content-Type": "application/json",
        }

        response_obj = self.http_session.post(
            url=url,
            json=contact_data,
            auth=(self.freshdesk_token, "X"),
            headers=headers,
        )

        # Case Duplicate a unique value
        if response_obj.status_code == 409:
            logging.warning(
                f"user with email {contact_data.get('email')} already registered"
            )
            response_conflic: FreshContactCreateConflict = json.loads(
                response_obj.text,
            )
            # Get first error value
            error_detail: FreshContactCreateDetailError = response_conflic.get(
                "errors",
            )[0]
            user_id: int = error_detail.get("additional_info").get("user_id")

            result: FreshContactResult = self.update_contact(
                user_id=user_id,
                contact_data=contact_data,
            )
            logging.info(f"Contact {contact_data.get('email')} updated")
            return result

        logging.info(f"Contact {contact_data.get('email')} created")
        return json.loads(response_obj.text)

    def list_all_contacts(
        self,
    ):
        url: str = f"https://{self.subdomain}.freshdesk.com/api/v2/contacts"
        headers: dict[str:str] = {
            "Content-Type": "application/json",
        }

        response_obj = self.http_session.get(
            url=url,
            auth=(self.freshdesk_token, "X"),
            headers=headers,
        )
        print(response_obj.text)
