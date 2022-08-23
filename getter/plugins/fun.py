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
    kasta_cmd,
    plugins_help,
    parse_pre,
    choice,
    UWUS,
    SHRUGS,
)


@kasta_cmd(
    pattern="(roll|toss|decide)$",
    no_crash=True,
)
async def _(kst):
    cmd = kst.pattern_match.group(1)
    if cmd == "roll":
        chars = range(1, 7)
    elif cmd == "toss":
        chars = ("Heads", "Tails")
    elif cmd == "decide":
        chars = ("Yes.", "No.", "Maybe.")
    text = choice(chars)
    await kst.sod(str(text))


@kasta_cmd(
    pattern="(owo|shg)$",
    no_crash=True,
)
async def _(kst):
    cmd = kst.pattern_match.group(1)
    if cmd == "owo":
        chars = UWUS
    elif cmd == "shg":
        chars = SHRUGS
    text = choice(chars)
    await kst.sod(text)


@kasta_cmd(
    pattern="(bol|bas|bow|dic|dar|slot)$",
    no_crash=True,
)
async def _(kst):
    cmd = kst.pattern_match.group(1)
    if cmd == "bol":
        dice = "⚽"
    elif cmd == "bas":
        dice = "🏀"
    elif cmd == "bow":
        dice = "🎳"
    elif cmd == "dic":
        dice = "🎲"
    elif cmd == "dar":
        dice = "🎯"
    elif cmd == "slot":
        dice = "🎰"
    async with kst.client.action(kst.chat_id, action="game"):
        await kst.try_delete()
        await kst.reply(file=InputMediaDice(dice))


@kasta_cmd(
    pattern="(love|fap|star|moon|think|lul|clock|muah|gym|earth|candy|rain|run|boxs)$",
    no_crash=True,
)
async def _(kst):
    cmd = kst.pattern_match.group(1)
    if cmd == "love":
        emot = "❤️🧡💛💚💙💜🖤"
    elif cmd == "fap":
        emot = "👉👌💦"
    elif cmd == "star":
        emot = "🦋✨🦋✨🦋✨🦋✨"
    elif cmd == "moon":
        emot = "🌗🌘🌑🌒🌓🌔🌕🌖"
    elif cmd == "think":
        emot = "🤔🧐🤔🧐🤔🧐"
    elif cmd == "lul":
        emot = "😂🤣😂🤣😂🤣"
    elif cmd == "clock":
        emot = "🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"
    elif cmd == "muah":
        emot = "😗😙😚😚😘"
    elif cmd == "gym":
        emot = "🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍"
    elif cmd == "earth":
        emot = "🌏🌍🌎🌎🌍🌏🌍🌎"
    elif cmd == "candy":
        emot = "🍦🍧🍩🍪🎂🍰🧁🍫🍬🍭"
    elif cmd == "rain":
        emot = "☀️🌤️⛅🌥️☁️🌩️🌧️⛈️⚡🌩️🌧️🌦️🌥️⛅🌤️☀️"
    elif cmd == "run":
        emot = "🚶🏃🚶🏃🚶🏃🚶🏃"
    elif cmd == "boxs":
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
    chars = (
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
    msg = await kst.eor("🖤")
    for i in range(54):
        await asyncio.sleep(0.5)
        await msg.eor(chars[i % 18])


@kasta_cmd(
    pattern="solars$",
    no_crash=True,
)
async def _(kst):
    chars = (
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️",
        "◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️",
        "◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️",
        "◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️",
        "◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️",
    )
    msg = await kst.eor("`solarsystem`")
    for i in range(80):
        await asyncio.sleep(0.1)
        await msg.eor(chars[i % 8], parse_mode=parse_pre)


@kasta_cmd(
    pattern="(kocok|dino)$",
    no_crash=True,
)
async def _(kst):
    cmd = kst.pattern_match.group(1)
    if cmd == "kocok":
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
    elif cmd == "dino":
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
    cmd = kst.pattern_match.group(1)
    if cmd == "dick":
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
    elif cmd == "doggy":
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
    elif cmd == "dog":
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
    elif cmd == "fucku":
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
    elif cmd == "rose":
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
    elif cmd == "pki":
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
    elif cmd == "pistol":
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
    elif cmd == "ok":
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
    cmd = kst.pattern_match.group(1)
    if cmd == "baa":
        expr = """
┻┳|
┳┻| _
┻┳| •.•)  **baa**
┳┻|⊂ﾉ
┻┳|
"""
    elif cmd == "bgst":
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


@kasta_cmd(
    pattern="thinking$",
    no_crash=True,
)
async def _(kst):
    chars = (
        "THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "THINKING",
        "THI&K#N₹",
        "T+IN@I?G",
        "¿H$NK∆NG",
        "¶H×NK&N*",
        "NGITHKIN",
        "T+I#K@₹G",
        "THINKING...🤔",
    )
    msg = await kst.eor("`Thinking...`")
    for i in range(288):
        await asyncio.sleep(0.05)
        await msg.eor(chars[i % 36])


@kasta_cmd(
    pattern="call$",
    no_crash=True,
)
async def _(kst):
    chars = (
        "Connecting To Telegram Headquarters...",
        "Call Connected.",
        "Telegram: Hello This is Telegram HQ. Who is this?",
        f"Me: Yo this is {kst.client.full_name} , Please Connect me to my lil bro, Pavel Durov",
        "User Authorised.",
        "Calling Pavel Durov At +916969696969",
        "Private Call Connected...",
        "Me: Hello Sir, Please Ban This Telegram Account.",
        "Pavel Durov: May I Know Who is This?",
        f"Me: Yo Brah, I Am {kst.client.full_name}",
        "Pavel Durov: OMG!!! Long time no see, Wassup cat...\nI'll Make Sure That Guy Account Will Get Blocked Within 24Hrs.",
        "Me: Thanks, See You Later Brah.",
        "Pavel Durov: Please Don't Thank Brah, Telegram Is Our's. Just Gimme A Call When You Become Free.",
        "Me: Is There Any Issue/Emergency???",
        "Pavel Durov: Yes Sur, There is A Bug in Telegram v69.6.9.\nI Am Not Able To Fix It. If Possible, Please Help Fix The Bug.",
        "Me: Send Me The App On My Telegram Account, I Will Fix The Bug & Send You.",
        "Pavel Durov: Sure Sur \nTC Bye Bye :)",
        "Private Call Disconnected",
    )
    msg = await kst.eor("`Calling Pavel Durov (ceo of telegram)......`")
    for char in chars:
        await asyncio.sleep(3)
        await msg.eor(char, parse_mode=parse_pre)


@kasta_cmd(
    pattern="deploy$",
    no_crash=True,
)
async def _(kst):
    chars = (
        "Heroku Connecting To Latest Github Build",
        f"Build started by user {kst.client.full_name}",
        f"Deploy 515a69f0 by user {kst.client.full_name}",
        "Restarting Heroku Server...",
        "State changed from up to starting",
        "Stopping all processes with SIGTERM",
        "Process exited with status 143",
        "Starting process with command python3 -m getter",
        "State changed from starting to up",
        "INFO:Userbot:Logged in as 557697062",
        "INFO:Userbot:Successfully loaded all plugins",
        "Build Succeeded",
    )
    msg = await kst.eor("`Deploying...`")
    await asyncio.sleep(3)
    for char in chars:
        await asyncio.sleep(3)
        await msg.eor(char, parse_mode=parse_pre)


plugins_help["fun"] = {
    "{i}roll": "Roll a dice.",
    "{i}toss": "Tosses a coin.",
    "{i}decide": "Randomly answers yes/no/maybe.",
    "{i}owo": "Get a random owo.",
    "{i}shg": "Get a random shrug.",
    "{i}bol": "Send ⚽ emoji.",
    "{i}bas": "Send 🏀 dice emoji.",
    "{i}bow": "Send 🎳 dice emoji.",
    "{i}dic": "Send 🎲 dice emoji.",
    "{i}dar": "Send 🎯 dice emoji.",
    "{i}slot": "Send 🎰 dice emoji.",
    "{i}love|{i}fap|{i}star|{i}moon|{i}think|{i}lul|{i}clock|{i}muah|{i}gym|{i}earth|{i}candy|{i}rain|{i}run|{i}boxs": "Send a random flipping emoji.",
    "{i}heart": "Send a love emoji animation.",
    "{i}solars": "Solarsystem animation.",
    "{i}kocok": "Ngocok simulation.",
    "{i}dino": "Dino animation.",
    "{i}dick|{i}doggy|{i}dog|{i}fucku|{i}rose|{i}pki|{i}pistol|{i}ok": "Show the ascii art text by name.",
    "{i}baa|{i}bgst": "Some funny expressions.",
    "{i}thinking": "Thinking animation.",
    "{i}call": "Call to durov.",
    "{i}deploy": "Deploy simulation.",
}
