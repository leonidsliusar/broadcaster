import asyncio
import io
import json
from asyncio import Semaphore
from typing import Union, Optional, AsyncGenerator
from telethon.errors import ChannelInvalidError, ChannelPrivateError, InputConstructorInvalidError, \
    ChatAdminRequiredError, MsgIdInvalidError
from telethon.sync import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest, UpdateUsernameRequest
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetRepliesRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.tl.types import User, Channel, Chat, PeerUser, PeerChannel, InputPhoto
from telethon.tl.functions.contacts import SearchRequest
from core.settings import settings
from core.models import FetchedChannel, FetchedUser
from utils.exceptions import NoUserFound

API_ID = 23128967
API_HASH = '1768893f3990862c7ec4571227f32743'
PHONE = '233541517457'


class LoginPassword:
    __slots__ = (
        '_api_id', '_api_hash', '_phone', '_password', '_bot_token', '_client', '_client_name', '_device', '_proxy')

    def __init__(self, api_id: int, api_hash: str, phone: str, proxy: dict) -> None:
        self._api_id: int = api_id
        self._api_hash: str = api_hash
        self._phone: str = phone
        self._password: str = None
        self._client: Optional[TelegramClient] = None
        self._device: str = 'iPhone 13 Pro Max'
        self._proxy: dict = proxy

    @property
    def client(self) -> TelegramClient:
        return self._client

    @client.setter
    def client(self, *args) -> None:
        if self._client is None:
            self._client = TelegramClient(
                session=self._phone,
                api_id=self._api_id,
                api_hash=self._api_hash,
                proxy=self._proxy
            )
        else:
            print("Client is already set")


class LoginSession:
    __slots__ = ('_api_id', '_api_hash', '_phone', '_bot_token', '_client', '_client_name', '_device')

    def __init__(self, api_id: int, api_hash: str, phone: str, bot_token: str) -> None:
        self._api_id: int = api_id
        self._api_hash: str = api_hash
        self._phone: str = phone
        self._bot_token: str = bot_token
        self._client: Optional[TelegramClient] = None
        self._client_name: str = phone
        self._device: str = 'iPhone 13 Pro Max'

    @property
    def client(self) -> TelegramClient:
        return self._client

    @client.setter
    def client(self, *args):
        if self._client is None:
            self._client = TelegramClient(self._client_name, self._api_id, self._api_hash)
        else:
            print("Client is already set")


class ChannelParser(LoginPassword):

    async def start(self) -> None:
        self.client = ...
        await self.client.start(phone=self._phone, code_callback=self.verify_code)

    async def verify_code(self):
        code = None
        while not code:
            with open('code_proxy.json', 'r') as file:
                code_map = json.load(file)
                code = code_map.get(self._phone)
        return code

    async def stop(self) -> None:
        await self.client.disconnect()

    async def about_me(self) -> User:
        return await self.client.get_me()

    async def update_me(self, **kwargs) -> None:
        if 'username' in kwargs:
            username = kwargs.pop('username')
            await self.client(UpdateUsernameRequest(username))
        if 'photo' in kwargs:
            photo = kwargs.pop('photo')
            await self.client(UploadProfilePhotoRequest(
                file=await self.client.upload_file(photo)
            ))
        if 'remove_photo_id' in kwargs:
            kwargs.pop('remove_photo_id')
            p = await self.client.get_profile_photos('me')
            p = p[0]
            await self.client(DeletePhotosRequest(
                id=[InputPhoto(
                    id=p.id,
                    access_hash=p.access_hash,
                    file_reference=p.file_reference
                )]
            ))
        await self.client(UpdateProfileRequest(**kwargs))


# proxy = {
#     'proxy_type': 'socks5',
#     'addr': '185.155.233.153',
#     'port': 50101,
#     'username': 'loslyusar',
#     'password': 'uKFgqacpvp',
# }


async def main(phone: str, proxy: dict):
    proxy = dict(zip(['proxy_type', 'addr', 'port', 'username', 'password'], list(proxy.values())))
    bot = ChannelParser(settings.API_ID, settings.API_HASH, phone, proxy=proxy)
    await bot.start()
    return await bot.about_me()
