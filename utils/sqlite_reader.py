from opentele.td import TDesktop
from opentele.api import API, UseCurrentSession
import asyncio


async def main():
    tdataFolder = r"tdata"
    tdesk = TDesktop(tdataFolder)

    assert tdesk.isLoaded()

    # flag=UseCurrentSession
    #
    # Convert TDesktop to Telethon using the current session.
    client = await tdesk.ToTelethon(session="telethon.session", flag=UseCurrentSession)

    # Connect and print all logged-in sessions of this client.
    # Telethon will save the session to telethon.session on creation.
    await client.connect()
    await client.PrintSessions()


asyncio.run(main())
