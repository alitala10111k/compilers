from ntpath import join
from pyrogram import (
    Client,
    filters,
    idle
)
import asyncio

from youtubesearchpython import VideosSearch

from pyrogram.errors.exceptions.bad_request_400 import MessageEmpty, MessageTooLong, UserNotParticipant,ChatAdminRequired, ChannelInvalid, MediaEmpty
from pyrogram.types.bots_and_keyboards.callback_query import CallbackQuery
from pyrogram.types.bots_and_keyboards.reply_keyboard_markup import ReplyKeyboardMarkup
from pyrogram.raw.functions.phone import CreateGroupCall,DiscardGroupCall
from pyrogram.raw.types import GroupCall
from pyrogram.raw.types import InputGroupCall
# from pyrogram.raw.base import InputGroupCall
from pyrogram.enums import ChatMemberStatus
from pyrogram import enums

from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ChatPrivileges,
)

from pyromod import listen

import time, sqlite3, random, aiocron, requests, json, os, re, sys

from pytgcalls import StreamType
from pytgcalls.types.input_stream.quality import HighQualityAudio
from pytgcalls.types.input_stream.quality import HighQualityVideo
from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.input_stream.video_parameters import VideoParameters
