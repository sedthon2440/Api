from time import sleep
import logging
import asyncio
import time
import datetime
import os
import requests
import re
import random
import telethon
from telethon import events, TelegramClient, functions
from telethon.tl import functions, types
from telethon.tl.types import InputPeerUser
from telethon.errors import FloodWaitError
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
    YouBlockedUserError,
    UserNotParticipantError
)
from telethon.sessions import StringSession
from telethon.utils import get_display_name
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import (
    ImportChatInviteRequest as Get,
    GetHistoryRequest,
    ImportChatInviteRequest,
    GetMessagesViewsRequest
)
from telethon.tl.functions.channels import (
    LeaveChannelRequest,
    JoinChannelRequest,
    InviteToChannelRequest,
    GetParticipantRequest
)
from telethon.tl.functions.contacts import UnblockRequest
from telethon.tl.functions.messages import (
    SendVoteRequest,
    SendReactionRequest
)


from telethon import TelegramClient, events


api_id = 26478228
api_hash = '7bd0b1761bebea880a084631044ea2bf'
bot_token = '6563637329:AAGMoZlngSyYkVvvYfCO8luQ1H7gFYACCy4'  


client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(content_types=['photo']))
async def handle_new_photo(event):
    
    photo_id = event.message.photo.id
    
    photo_url = f'https://api.thetellus.io/v1/images/{photo_id}'

    await event.reply(f'رابط الصورة: {photo_url}')


client.start(bot_token=bot_token)  
client.run_until_disconnected()


