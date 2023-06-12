from datetime import datetime
from typing import Any, List, TypedDict, Optional
from uuid import UUID


class CustomFields:
    pass

    def __init__(
        self,
    ) -> None:
        pass


class FreshContactResult(TypedDict):
    active: bool
    address: None
    deleted: bool
    description: None
    email: str
    id: int
    job_title: None
    language: str
    mobile: None
    name: str
    phone: None
    time_zone: str
    twitter_id: None
    custom_fields: CustomFields
    tags: List[Any]
    other_emails: List[Any]
    facebook_id: None
    created_at: datetime
    updated_at: datetime
    csat_rating: None
    preferred_source: None
    company_id: None
    view_all_tickets: None
    other_companies: List[Any]
    unique_external_id: None
    avatar: None
    first_name: str
    last_name: str
    visitor_id: UUID
    org_contact_id: float
    other_phone_numbers: List[Any]


class FreshContactCreateGithub(TypedDict):
    name: str
    email: str
    address: Optional[str]
    avatar: Optional[str]
    description: Optional[str]


class FreshContactCreate(TypedDict):
    name: str
    email: str
    phone: Optional[str]
    mobile: Optional[str]
    twitter_id: Optional[str]
    unique_external_id: Optional[str]
    other_emails: Optional[List[str]]
    company_id: Optional[int]
    view_all_tickets: Optional[bool]
    other_companies: Optional[List[str]]
    address: Optional[str]
    avatar: Optional[str]
    custom_fields: Optional[CustomFields]
    description: Optional[str]
    job_title: Optional[str]
    language: Optional[str]
    tags: Optional[List[str]]
    time_zone: Optional[str]
    lookup_parameter: Optional[str]


class AdditionalInfo(TypedDict):
    user_id: int


class FreshContactCreateDetailError(TypedDict):
    field: str
    additional_info: AdditionalInfo
    message: str
    code: str


class FreshContactCreateConflict(TypedDict):
    description: str
    errors: List[FreshContactCreateDetailError]
