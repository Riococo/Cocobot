# getter < https://t.me/kastaid >
# Copyright (C) 2022 kastaid
#
# This file is a part of < https://github.com/kastaid/getter/ >
# PLease read the GNU Affero General Public License in
# < https://github.com/kastaid/getter/blob/main/LICENSE/ >.

import asyncio
from collections import deque
from telethon.tl.types import InputMediaDice
from . import (
    HELP,
    kasta_cmd,
    parse_pre,
    choice,
    UWUS,
    SHRUGS,
)


@kasta_cmd(
    pattern="(owo|shg)$",
    no_crash=True,
)
async def _(kst):
    match = kst.pattern_match.group(1)
    if match == "owo":
        chars = UWUS
    elif match == "shg":
        chars = SHRUGS
    text = choice(chars)
    await kst.eor(text)


@kasta_cmd(
    pattern="(bol|bas|bow|dic|dar|slot)$",
    no_crash=True,
)
async def _(kst):
    match = kst.pattern_match.group(1)
    if match == "bol":
        dice = "⚽"
    elif match == "bas":
        dice = "🏀"
    elif match == "bow":
        dice = "🎳"
    elif match == "dic":
        dice = "🎲"
    elif match == "dar":
        dice = "🎯"
    elif match == "slot":
        dice = "🎰"
    await kst.try_delete()
    await kst.reply(file=InputMediaDice(dice))


@kasta_cmd(
    pattern="(love|fap|star|moon|lul|clock|muah|gym|earth|candy|rain|run|boxs)$",
    no_crash=True,
)
async def _(kst):
    match = kst.pattern_match.group(1)
    if match == "love":
        emot = "❤️🧡💛💚💙💜🖤"
    elif match == "fap":
        emot = "👉👌💦"
    elif match == "star":
        emot = "🦋✨🦋✨🦋✨🦋✨"
    elif match == "moon":
        emot = "🌗🌘🌑🌒🌓🌔🌕🌖"
    elif match == "lul":
        emot = "😂🤣😂🤣😂🤣"
    elif match == "clock":
        emot = "🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"
    elif match == "muah":
        emot = "😗😙😚😚😘"
    elif match == "gym":
        emot = "🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍"
    elif match == "earth":
        emot = "🌏🌍🌎🌎🌍🌏🌍🌎"
    elif match == "candy":
        emot = "🍦🍧🍩🍪🎂🍰🧁🍫🍬🍭"
    elif match == "rain":
        emot = "☀️🌤️⛅🌥️☁️🌩️🌧️⛈️⚡🌩️🌧️🌦️🌥️⛅🌤️☀️"
    elif match == "run":
        emot = "🚶🏃🚶🏃🚶🏃🚶🏃"
    elif match == "boxs":
        emot = "🟥🟧🟨🟩🟦🟪🟫⬛⬜"
    deq = deque(list(emot))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await kst.eor("".join(deq))
        deq.rotate(1)


@kasta_cmd(
    pattern="heart$",
    no_crash=True,
)
async def _(kst):
    anim_interv = 0.5
    anim_ttl = range(54)
    msg = await kst.eor("🖤")
    anim_chars = (
        "❤️",
        "🧡",
        "💛",
        "💚",
        "💙",
        "💜",
        "🖤",
        "💘",
        "💝",
        "❤️",
        "🧡",
        "💛",
        "💚",
        "💙",
        "💜",
        "🖤",
        "💘",
        "💝",
    )
    for i in anim_ttl:
        await asyncio.sleep(anim_interv)
        await msg.eor(anim_chars[i % 18])


@kasta_cmd(
    pattern="solars$",
    no_crash=True,
)
async def _(kst):
    anim_interv = 0.1
    anim_ttl = range(0, 80)
    msg = await kst.eor("`solarsystem...`")
    anim_chars = (
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️",
        "◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️",
        "◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️",
        "◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️",
        "◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️",
    )
    for i in anim_ttl:
        await asyncio.sleep(anim_interv)
        await msg.eor(anim_chars[i % 8], parse_mode=parse_pre)


@kasta_cmd(
    pattern="kocok$",
    no_crash=True,
)
async def _(kst):
    chars = (
        "8✊️===D",
        "8=✊️==D",
        "8==✊️=D",
        "8===✊️D",
        "8==✊️=D",
        "8=✊️==D",
        "8✊️===D",
        "8=✊️==D",
        "8==✊️=D",
        "8===✊️D",
        "8==✊️=D",
        "8=✊️==D",
        "8✊️===D",
        "8=✊️==D",
        "8==✊️=D",
        "8===✊️D",
        "8==✊️=D",
        "8=✊️==D",
        "8✊️===D",
        "8=✊️==D",
        "8==✊️=D",
        "8===✊️D",
        "8==✊️=D",
        "8=✊️==D",
        "8===✊D💦",
        "8==✊=D💦💦",
        "8=✊==D💦💦💦",
        "8✊===D💦💦💦💦",
        "8===✊D💦💦💦💦💦",
        "8==✊=D💦💦💦💦💦💦",
        "8=✊==D💦💦💦💦💦💦💦",
        "8✊===D💦💦💦💦💦💦💦💦",
        "8===✊D💦💦💦💦💦💦💦💦💦",
        "8==✊=D💦💦💦💦💦💦💦💦💦💦",
        "8=✊==D ?",
        "8==✊=D ??",
        "8===✊D ???",
        "😭😭😭",
    )
    for char in chars:
        await asyncio.sleep(0.3)
        await kst.eor(char)


@kasta_cmd(
    pattern="dino$",
    no_crash=True,
)
async def _(kst):
    chars = (
        "🏃                        🦖",
        "🏃                       🦖",
        "🏃                      🦖",
        "🏃                     🦖",
        "🏃                    🦖",
        "🏃                   🦖",
        "🏃                  🦖",
        "🏃                 🦖",
        "🏃                🦖",
        "🏃               🦖",
        "🏃              🦖",
        "🏃             🦖",
        "🏃            🦖",
        "🏃           🦖",
        "🏃          🦖",
        "🏃           🦖",
        "🏃            🦖",
        "🏃             🦖",
        "🏃              🦖",
        "🏃               🦖",
        "🏃                🦖",
        "🏃                 🦖",
        "🏃                  🦖",
        "🏃                   🦖",
        "🏃                    🦖",
        "🏃                     🦖",
        "🏃                    🦖",
        "🏃                   🦖",
        "🏃                  🦖",
        "🏃                 🦖",
        "🏃                🦖",
        "🏃               🦖",
        "🏃              🦖",
        "🏃             🦖",
        "🏃            🦖",
        "🏃           🦖",
        "🏃          🦖",
        "🏃         🦖",
        "🏃        🦖",
        "🏃       🦖",
        "🏃      🦖",
        "🏃     🦖",
        "🏃    🦖",
        "🏃   🦖",
        "🏃  🦖",
        "🏃 🦖",
        "🧎🦖",
    )
    for char in chars:
        await asyncio.sleep(0.3)
        await kst.eor(char, parse_mode=parse_pre)


@kasta_cmd(
    pattern="(dick|doggy|dog|fucku|rose|pki|pistol|ok)$",
    no_crash=True,
)
async def _(kst):
    match = kst.pattern_match.group(1)
    if match == "dick":
        art = """
ㅤ
⣠⡶⠚⠛⠲⢄⡀
⣼⠁ ⠀⠀⠀ ⠳⢤⣄
⢿⠀⢧⡀⠀⠀⠀⠀⠀⢈⡇
⠈⠳⣼⡙⠒⠶⠶⠖⠚⠉⠳⣄
⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄
⠀⠀⠀⠘⣆ ⠀⠀⠀⠀ ⠀⠈⠓⢦⣀
⠀⠀⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⢤
⠀⠀⠀⠀⠀⠀⠙⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧
⠀⠀⠀⠀⠀⠀⠀⡴⠋⠓⠦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠈⣇
⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄
⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⢹⡄⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃
⠀⠀⠀⠀⠀⠀⠀⠙⢦⣀⣳⡀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⢦⣀⣀⣀⣀⣠⡴⠚⠉
ㅤ
"""
    elif match == "doggy":
        art = """
ㅤ
⠀⠀⠀⠀⠀⠀⣠⣤⣄
⠀⠀⠀⠀⠀⢰⣿⣿⣿⡷
⠀⠀⠀⠀⠀⢀⣙⡛⠛⠁
⠀⠀⠀⠀⢀⣿⣿⣿⡆
⠀⠀⠀⠀⣾⣿⣿⣿⣧
⠀⠀⠀⢰⣿⣿⣿⠙⣿⣧⠀⣤⣶⣄⣾⣿⣿⣷
⠀⠀⠀⢻⣿⣿⣇⣴⣮⡿⣿⡟⠛⠁⣙⠿⠿⠋
⠀⠀⠀⠘⣿⣿⡏⣿⣿⣿⣾⣾⣿⣿⣿⣷
⢀⣀⣀⣀⣿⣿⡇⢿⣿⡇⠈⠉⠻⡿⣿⡏
⠘⠿⠿⠿⠿⠿⠧⠿⠿⠇⠀⠀⠀⠀⠿⠿⠿⠿⠗
ㅤ
"""
    elif match == "dog":
        art = r"""
ㅤ
┈┈┈┈╱▏┈┈┈┈┈╱▔▔▔▔╲┈┈┈┈
┈┈┈┈▏▏┈┈┈┈┈▏╲▕▋▕▋▏┈┈┈
┈┈┈┈╲╲┈┈┈┈┈▏┈▏┈▔▔▔▆┈┈
┈┈┈┈┈╲▔▔▔▔▔╲╱┈╰┳┳┳╯┈┈
┈┈╱╲╱╲▏┈┈┈┈┈┈▕▔╰━╯┈┈┈
┈┈▔╲╲╱╱▔╱▔▔╲╲╲╲┈┈┈┈┈┈
┈┈┈┈╲╱╲╱┈┈┈┈╲╲▂╲▂┈┈┈┈
┈┈┈┈┈┈┈┈┈┈┈┈┈╲╱╲╱┈┈┈┈
ㅤ
"""
    elif match == "fucku":
        art = """
ㅤ
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠏⠁⠙⢿⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠀⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⠀⠀⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⠀⣾⠏⣿⠀⠀⠀⠀⢸⣷⣦⣄⡀
⠀⠀⠀⠀⠀⠀⣼⡿⠀⣿⠀⠀⠀⠀⢸⠇⠀⠉⢷⡀
⠀⠀⠀⠀⣠⡾⢿⠇⠀⣿⠀⠀⠀⠀⢸⡇⠀⠀⠸⡷⠤⣄⡀
⠀⠀⢠⡾⠋⣾⠀⠀⠀⣿⠀⠀⠀⠀⢸⡇⠀⠀⠀⣧⠀⠀⠹⡄
⠀⣰⠏⠀⠀⣿⠀⠀⠀⠉⠀⠀⠀⠀⠈⠁⠀⠀⠀⢹⡄⠀⠀⢹⡄
⢰⡏⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠇⠀⠀⠀⢻⡄
⠘⣿⡀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣷
⠀⠙⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿
⠀⠀⠀⠹⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡟
⠀⠀⠀⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠟
⠀⠀⠀⠀⠀⠀⠈⠻⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡿⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠏
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏
ㅤ
"""
    elif match == "rose":
        art = """
ㅤ
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀
⠀⠀⠀⠀⠀⠀⠀⡠⠖⠋⠉⠉⠳⡴⠒⠒⠒⠲⠤⢤⣀
⠀⠀⠀⠀⠀⣠⠊⠀⠀⡴⠚⡩⠟⠓⠒⡖⠲⡄⠀⠀⠈⡆
⠀⠀⠀⢀⡞⠁⢠⠒⠾⢥⣀⣇⣚⣹⡤⡟⠀⡇⢠⠀⢠⠇
⠀⠀⠀⢸⣄⣀⠀⡇⠀⠀⠀⠀⠀⢀⡜⠁⣸⢠⠎⣰⣃
⠀⠀⠸⡍⠀⠉⠉⠛⠦⣄⠀⢀⡴⣫⠴⠋⢹⡏⡼⠁⠈⠙⢦⡀
⠀⠀⣀⡽⣄⠀⠀⠀⠀⠈⠙⠻⣎⡁⠀⠀⣸⡾⠀⠀⠀⠀⣀⡹⠂
⢀⡞⠁⠀⠈⢣⡀⠀⠀⠀⠀⠀⠀⠉⠓⠶⢟⠀⢀⡤⠖⠋⠁
⠀⠉⠙⠒⠦⡀⠙⠦⣀⠀⠀⠀⠀⠀⠀⢀⣴⡷⠋
⠀⠀⠀⠀⠀⠘⢦⣀⠈⠓⣦⣤⣤⣤⢶⡟⠁
⢤⣤⣤⡤⠤⠤⠤⠤⣌⡉⠉⠁⠀⢸⢸⠁⡠⠖⠒⠒⢒⣒⡶⣶⠤
⠉⠲⣍⠓⠦⣄⠀⠀⠙⣆⠀⠀⠀⡞⡼⡼⢀⣠⠴⠊⢉⡤⠚⠁
⠀⠀⠈⠳⣄⠈⠙⢦⡀⢸⡀⠀⢰⢣⡧⠷⣯⣤⠤⠚⠉
⠀⠀⠀⠀⠈⠑⣲⠤⠬⠿⠧⣠⢏⡞
⠀⠀⢀⡴⠚⠉⠉⢉⣳⣄⣠⠏⡞
⣠⣴⣟⣒⣋⣉⣉⡭⠟⢡⠏⡼
⠉⠀⠀⠀⠀⠀⠀⠀⢀⠏⣸⠁
⠀⠀⠀⠀⠀⠀⠀⠀⡞⢠⠇
⠀⠀⠀⠀⠀⠀⠀⠘⠓⠚
ㅤ
"""
    elif match == "pki":
        art = """
ㅤ
⠀⠀⠀⠀⠀⠀⢀⣤⣀⣀⣀⠀⠻⣷⣄
⠀⠀⠀⠀⢀⣴⣿⣿⣿⡿⠋⠀⠀⠀⠹⣿⣦⡀
⠀⠀⢀⣴⣿⣿⣿⣿⣏⠀⠀⠀⠀⠀⠀⢹⣿⣧
⠀⠀⠙⢿⣿⡿⠋⠻⣿⣿⣦⡀⠀⠀⠀⢸⣿⣿⡆
⠀⠀⠀⠀⠉⠀⠀⠀⠈⠻⣿⣿⣦⡀⠀⢸⣿⣿⡇
⠀⠀⠀⠀⢀⣀⣄⡀⠀⠀⠈⠻⣿⣿⣶⣿⣿⣿⠁
⠀⠀⠀⣠⣿⣿⢿⣿⣶⣶⣶⣶⣾⣿⣿⣿⣿⡁
⢠⣶⣿⣿⠋⠀⠀⠉⠛⠿⠿⠿⠿⠿⠛⠻⣿⣿⣦⡀
⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⡿
ㅤ
"""
    elif match == "pistol":
        art = """
ㅤ
⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣤⣤
⠀⢶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿
⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠛⠛⠛⠛⠋⠉
⠀⠀⢹⣿⣿⣿⣿⣿⠏⢠⣿⡀⠀⠀⢹⡟
⠀⢠⣿⣿⣿⣿⣿⣿⣦⣀⣀⣙⣂⣠⠼⠃
⠀⣾⣿⣿⣿⣿⣿⠁
⢠⣿⣿⣿⣿⣿⡟
⢸⣿⣿⣿⣿⣿⡅
⠀⠛⠛⠛⠛⠛⠃
ㅤ
"""
    elif match == "ok":
        art = """
ㅤ
⠀⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀
⠀⠀⠀⣴⠿⠏⠀⠀⠀⠀⠀⠀⢳⡀⠀⡏⠀⠀⠀⠀⠀⢷
⠀⠀⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀⠀⠀ ⡇
⠀⠀⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿⠀⣸⠀⠀OK⠀ ⡇
⠀⠀⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀⣿⠀⢹⠀⠀⠀⠀⠀ ⡇
⠀⠀⠙⢿⣯⠄⠀⠀⠀⢀⡀⠀⠀⡿⠀⠀⡇⠀⠀⠀⠀⡼
⠀⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀⠀⠘⠤⣄⣠⠞
⠀⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁
⠀⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀
⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿
⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀⠀⣄⢸
⣿⣿⣧⣀⣿.........⣀⣰⣏⣘⣆⣀
ㅤ
"""
    await kst.sod(art, parse_mode=parse_pre)


@kasta_cmd(
    pattern="(baa|bgst)$",
    no_crash=True,
)
async def _(kst):
    match = kst.pattern_match.group(1)
    if match == "baa":
        expr = """
┻┳|
┳┻| _
┻┳| •.•)  **baa**
┳┻|⊂ﾉ
┻┳|
"""
    elif match == "bgst":
        expr = """
○
く|)へ
    〉
 ￣￣┗┓             __bgst bgst__
 　 　   ┗┓　     ヾ○ｼ
  　　        ┗┓   ヘ/
 　                 ┗┓ノ
　 　 　 　 　   ┗┓
"""
    await kst.sod(expr)


HELP.update(
    {
        "fun": [
            "Funny",
            """❯ `{i}owo`
Get a random owo.

❯ `{i}shg`
Get a random shrug.

❯ `{i}bol|{i}bas|{i}bow|{i}dic|{i}dar|{i}slot`
Send the dice emoji.

❯ `{i}love|{i}fap|{i}star|{i}moon|{i}lul|{i}clock|{i}muah|{i}gym|{i}earth|{i}candy|{i}rain|{i}run|{i}boxs`
Send a random flipping emoji.

❯ `{i}heart`
Send a love emoji animation.

❯ `{i}solars`
Show the solarsystem animation.

❯ `{i}kocok`
Ngocok simulation.

❯ `{i}dino`
Show the dino animation.

❯ `{i}dick|{i}doggy|{i}dog|{i}fucku|{i}rose|{i}pki|{i}pistol|{i}ok`
Show the ascii art text by name.

❯ `{i}baa|{i}bgst`
Some funny expressions.
""",
        ]
    }
)
