import os
import asyncio
import random
from time import sleep
from telethon import TelegramClient, events, functions

API_ID = 28384232
API_HASH = "3f3f741f30026039c2faa36f3dfa5d7a"
PHONE_NUMBER = "+96176063942"
SESSION_NAME = "my_session"
#
copyright = lambda:print("script made By N0\nTelegram : @N9km2\nInstagram : @tnr3\nYoutube : https://Youtube.com/Nfrxdra")

copyright()
print("\n" * 5)
print("Script used to auto invite random members to your Telegram group.")
print("Put in Chat username your chat username and in Group username an other group to get members from it.")
group_username = "@BlackXies_group"#يوزر القروب يلي تبي تسحب اعضاء منه
chat_username = "@mhat1"#يوزر قروبك
os.system("clear"); copyright()
print("After login, send /invite in any group.")

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

async def generate_random_usernames_from_group(group_username, num_users):
    usernames = []
    async for user in client.iter_participants(group_username, limit=100):
        if user.username:
            usernames.append(user.username)
    random.shuffle(usernames)
    return usernames[:num_users]

async def invite_users_to_group(chat_username, usernames):
    try:
        await client.connect()

        if not await client.is_user_authorized():
            await client.send_code_request(PHONE_NUMBER)
            await client.sign_in(PHONE_NUMBER, input('Enter the code: '))

        chat = await client.get_entity(chat_username)
        chat_id = chat.id
        xsleep = 0
        for username in usernames:
            if xsleep != 20:
                xsleep += 1
            if xsleep == 20:
                sleep(60)
                x = 0
            try:
                await client(functions.channels.InviteToChannelRequest(chat_id, [username]))
                print(f"\033[1;32mAdded {username} to the group.")
            except Exception as e:
                print(f"\033[1;31mError adding {username} to the group: {str(e)}")
    finally:
        await client.disconnect()

@client.on(events.NewMessage(pattern='/invite'))
async def handle_invite_message(event):
    if event.is_group and event.chat_id:
        num_users = 100
        usernames = await generate_random_usernames_from_group(group_username, num_users)
        await invite_users_to_group(chat_username, usernames)

client.start()
client.run_until_disconnected()
