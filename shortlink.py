import os
import asyncio
import aiohttp
from os import getenv, environ
from asyncio import TimeoutError
from shortzy import Shortzy
from config import *

SHORTENER_APII = SHORTENER_API
SHORTENER_URL = SHORTENER_WEBSITE


shortzy = Shortzy(SHORTENER_APII, SHORTENER_URL)

async def get_shortlink(link):
    if not SHORTENER_APII or not SHORTENER_URL:
        return link

    try:
        x = await shortzy.convert(link, silently_fail=True)
    except Exception:
        x = await get_shortlink_sub(link)
    return x


async def get_shortlink_sub(link):
    if SHORTENER_URL == "api.shareus.io":
        url = f'https://{SHORTENER_URL}/easy_api'
        params = {
            "key": SHORTENER_APII,
            "link": link,
        }
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, params=params, raise_for_status=True, ssl=False) as response:
                    data = await response.text()
                    return data
        except Exception:
            x = await get_shortlink_sub(link)
            return x



