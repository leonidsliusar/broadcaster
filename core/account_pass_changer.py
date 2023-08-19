import asyncio
from getpass import getpass
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.account import UpdatePasswordSettingsRequest

API_ID = 23128967
API_HASH = '1768893f3990862c7ec4571227f32743'
BOT_TOKEN = '6342844716:AAFLHrm6JivKEe9bbq4qpyyKTJBMdV_epPs'
PHONE = '6285600296652'



async def change_pass():
    new_password = 'Jdhakdfjuekld45dfv99VRGdc6'
    async with TelegramClient('telethon', API_ID, API_HASH) as client:
        client.start(PHONE)
        client(UpdatePasswordSettingsRequest(
            new_settings=client(UpdatePasswordSettingsRequest(
                new_password=new_password
            ))
        ))


async def main():
    client = TelegramClient('telethon', API_ID, API_HASH)
    await client.start()
    print(await client.get_me())


# asyncio.run(main())
