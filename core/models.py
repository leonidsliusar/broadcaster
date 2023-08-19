from typing import Optional
from pydantic import BaseModel
from core.settings import settings


class FetchedChannel(BaseModel):
    channel_id: Optional[int] = None
    title: Optional[str] = None
    user_counts: Optional[int] = None
    user_set: Optional[list[dict]] = []


class FetchedUser(BaseModel):  # detail about user comment
    user_id: int
    user_name: str
    first_name: str
    last_name: str
    phone: str
    message: str
    channel_id: int
    channel_title: str


class FetchedUserFromGroup(BaseModel):
    user_id: int
    message: str
    channel_id: int
    channel_title: str


class Task(BaseModel):
    id: Optional[int]
    message: str
    users: set[int]


class Group(BaseModel):
    id: int
    title: str
    description: Optional[str]
    user_count: int
    users: set[int]


class User(BaseModel):
    id: int
    username: str
    first_name: str


class InputBroadcast(BaseModel):
    phone: str
    password: str
    group_id: str
    text: str
