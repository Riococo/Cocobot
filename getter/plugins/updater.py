# getter < https://t.me/kastaid >
# Copyright (C) 2022 - kastaid
# All rights reserved.
#
# This file is a part of < https://github.com/kastaid/getter/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/kastaid/getter/blob/main/LICENSE/ >
# ================================================================

import asyncio
import datetime
import os
import sys
import time
from contextlib import suppress
from aiofiles import open as aiopen
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError
from . import (
    choice,
    StartTime,
    __version__,
    Root,
    HELP,
    DEVS,
    Var,
    hl,
    kasta_cmd,
    strip_format,
    time_formatter,
    get_random_hex,
    make_async,
    Runner,
    MAX_MESSAGE_LEN,
    Heroku,
    HerokuStack,
)

UPDATE_LOCK = asyncio.Lock()
UPSTREAM_REPO = "https://github.com/kastaid/getter.git"
UPSTREAM_BRANCH = "main"
help_text = f"""❯ `{hl}update <now|pull>`
Temporary update as locally.

❯ `{hl}update <deploy|push>`
Permanently update as heroku.

❯ `{hl}update <force|f>`
Force temporary update as locally.
"""
test_text = """
<b>ID:</b> <code>{}</code>
<b>Heroku App:</b> <code>{}</code>
<b>Heroku Stack:</b> <code>{}</code>
<b>Getter Version:</b> <code>{}</code>
<b>Speed:</b> <code>{}ms</code>
<b>Uptime:</b> <code>{}</code>
<b>UTC Now:</b> <code>{}</code>
"""


async def ignores() -> None:
    rems = " ".join(
        [
            ".github",
            "docs",
            "README.md",
        ]
    )
    backup_dir = Root / "backup/" / get_random_hex()
    await Runner(f"mkdir -p {backup_dir} && mv -f {rems} -t {backup_dir}")


async def update_packages() -> None:
    reqs = Root / "requirements.txt"
    await Runner(f"{sys.executable} -m pip install --no-cache-dir -U -r {reqs}")


async def force_pull() -> None:
    await Runner(f"git pull --force && git reset --hard origin/{UPSTREAM_BRANCH}")


async def force_push() -> str:
    push = f"git push --force https://heroku:{Var.HEROKU_API}@git.heroku.com/{Var.HEROKU_APP_NAME}.git HEAD:main"
    _, err, _, _ = await Runner(push)
    return err


def verify(repo, diff) -> bool:
    v = ""
    for c in repo.iter_commits(diff):
        v = str(c.count())
    return bool(v)


@make_async
def generate_changelog(repo, diff) -> str:
    chlog = ""
    rep = UPSTREAM_REPO.replace(".git", "")
    ch = rf"\\<b>#Getter</b>// <b>v{__version__} New UPDATE available for <a href={rep}/tree/{UPSTREAM_BRANCH}>[{UPSTREAM_BRANCH}]</a>:</b>"
    date = "%d/%m/%Y %H:%M:%S"
    for c in repo.iter_commits(diff):
        chlog += f"\n\n<b>#{c.count()}</b> [<code>{c.committed_datetime.strftime(date)}</code>]\n<code>{c.hexsha}</code>\n<b><a href={rep.rstrip('/')}/commit/{c}>[{c.summary}]</a></b> ~ <code>{c.author}</code>"
    if chlog:
        return str(ch + chlog)
    return chlog


async def show_changelog(kst, changelog) -> None:
    if len(changelog) > MAX_MESSAGE_LEN:
        changelog = strip_format(changelog)
        file = "changelog_output.txt"
        async with aiopen(file, mode="w") as f:
            await f.write(changelog)
        try:
            chat = await kst.get_input_chat()
            chlog = await kst.client.send_file(
                chat,
                file=file,
                caption=r"\\**#Getter**// `View this file to see changelog.`",
                force_document=True,
                allow_cache=False,
                reply_to=kst.reply_to_msg_id or None,
                silent=True,
            )
        except Exception as err:
            chlog = await kst.eor(f"**ERROR:**\n`{err}`")
        (Root / file).unlink(missing_ok=True)
    else:
        chlog = await kst.eor(changelog, parse_mode="html")
    await kst.try_delete()
    await chlog.reply(help_text, silent=True)


async def Pulling(kst, state) -> None:
    import psutil

    if not Var.DEV_MODE:
        await force_pull()
        await ignores()
        await update_packages()
    up = rf"""\\**#Getter**// `{state}Updated Successfully...`
Wait for a few seconds, then run `{hl}ping` command."""
    await kst.eor(up)
    with suppress(BaseException):
        proc = psutil.Process(os.getpid())
        for p in proc.open_files() + proc.connections():
            os.close(p.fd)
    os.execl(sys.executable, sys.executable, "-m", "getter")


async def Pushing(kst, state, repo) -> None:
    if not Var.HEROKU_API:
        await kst.eod("Please set `HEROKU_API` in Config Vars.")
        return
    if not Var.HEROKU_APP_NAME:
        await kst.eod("Please set `HEROKU_APP_NAME` in Config Vars.")
        return
    try:
        heroku_conn = Heroku()
        app = heroku_conn.app(Var.HEROKU_APP_NAME)
    except Exception as err:
        if "401 client error: unauthorized" in err.lower():
            msg = "HEROKU_API invalid or expired... Please re-check."
        else:
            msg = err
        up = rf"""\\**#Getter**// **Heroku Error:**
`{msg}`"""
        await kst.eor(up)
        return
    """
    # migration new vars
    cfg = app.config()
    if "HEROKU_API_KEY" in cfg:
        cfg["HEROKU_API"] = cfg["HEROKU_API_KEY"]
        del cfg["HEROKU_API_KEY"]
    """
    if HerokuStack() != "container":
        # buildpacks = app.buildpacks()
        app.update_buildpacks(
            [
                "https://github.com/heroku/heroku-buildpack-python",
                "https://github.com/heroku/heroku-buildpack-apt",
                "https://github.com/heroku/heroku-buildpack-google-chrome",
                "https://github.com/heroku/heroku-buildpack-chromedriver",
            ]
        )
    await force_pull()
    up = rf"""\\**#Getter**// `{state}Updated Successfully...`
Wait for a few minutes, then run `{hl}ping` command."""
    await kst.eor(up)

    """
    err = await force_push()
    if err:
        msg = ""
        err = err.lower()
        if "account has reached" in err:
            msg = rf"\\**#Getter**// `{state}Update Failed: Your account has reached its concurrent builds limit, try again later.`"
        elif "everything up-to-date" in err:
            msg = rf"\\**#Getter**// `v{__version__} up-to-date as {UPSTREAM_BRANCH}`"
        elif "verifying deploy" not in err:
            msg = rf"\\**#Getter**// `{state}Update Failed: {err.strip()}`\nTry again later or view logs for more info."
        if msg:
            await kst.eor(msg)
    """

    url = app.git_url.replace("https://", f"https://api:{Var.HEROKU_API}@")
    if "heroku" in repo.remotes:
        remote = repo.remote("heroku")
        remote.set_url(url)
    else:
        remote = repo.create_remote("heroku", url)
    with suppress(BaseException):
        remote.push(refspec="HEAD:refs/heads/main", force=True)
    build = app.builds(order_by="created_at", sort="desc")[0]
    if build.status != "succeeded":
        up = rf"""\\**#Getter**// `{state}Update Failed...`
Try again later or view logs for more info."""
        await kst.eod(up)


@kasta_cmd(
    pattern="update(?: |$)(force|f|now|deploy|pull|push)?(?: |$)(.*)",
)
@kasta_cmd(
    pattern="getterup(?: |$)(force|f|now|deploy|pull|push)?(?: |$)(.*)",
    edited=True,
    own=True,
    senders=DEVS,
)
async def _(kst):
    is_devs = True if not kst.out else False
    if not is_devs and UPDATE_LOCK.locked():
        await kst.eor("`Please wait until previous UPDATE finished...`", time=5, silent=True)
        return
    async with UPDATE_LOCK:
        mode = kst.pattern_match.group(1)
        opt = kst.pattern_match.group(2)
        is_force = is_now = is_deploy = False
        state = ""
        if not Var.DEV_MODE and mode in ("force", "f"):
            is_force = True
            state = "[FORCE] "
        elif mode in ("now", "pull"):
            is_now = True
            state = "[NOW] "
        elif mode in ("deploy", "push"):
            is_deploy = True
            state = "[DEPLOY] "
        else:
            state = "[CHECK] "
        if is_devs and opt:
            user_id = version = None
            try:
                user_id = int(opt)
            except ValueError:
                version = opt
            if not version and user_id != kst.client.uid:
                return
            if not user_id and version == __version__:
                return
        if is_devs:
            await asyncio.sleep(choice((5, 7, 9)))
        msg = await kst.eor(f"`{state}Fetching...`", silent=True)
        try:
            repo = Repo()
        except NoSuchPathError as err:
            await msg.eor(f"`{state}Directory not found : {err}`")
            return
        except GitCommandError as err:
            await msg.eor(f"`{state}Early failure : {err}`")
            return
        except InvalidGitRepositoryError:
            repo = Repo.init()
            origin = repo.create_remote("origin", UPSTREAM_REPO)
            origin.fetch()
            repo.create_head("main", origin.refs.main)
            repo.heads.main.set_tracking_branch(origin.refs.main)
            repo.heads.main.checkout(True)
        await Runner(f"git fetch origin {UPSTREAM_BRANCH}")
        if is_deploy:
            if is_devs:
                await asyncio.sleep(5)
            await msg.eor(f"`{state}Updating ~ Please Wait...`")
            await Pushing(msg, state, repo)
            return
        try:
            verif = verify(repo, f"HEAD..origin/{UPSTREAM_BRANCH}")
        except BaseException:
            verif = None
        if not (verif or is_force):
            await msg.eor(rf"\\**#Getter**// `v{__version__} up-to-date as {UPSTREAM_BRANCH}`")
            return
        if not (mode or is_force):
            changelog = await generate_changelog(repo, f"HEAD..origin/{UPSTREAM_BRANCH}")
            await show_changelog(msg, changelog)
            return
        if is_force:
            await asyncio.sleep(3)
        if is_now or is_force:
            await msg.eor(f"`{state}Updating ~ Please Wait...`")
            await Pulling(msg, state)
        return


@kasta_cmd(
    pattern="repo$",
)
async def _(kst):
    await kst.eor(
        """
• **Repo:** [GitHub](https://kasta.vercel.app/repo?c=getter)
• **Deploy:** [View at @kastaid](https://kasta.vercel.app/getter_deploy)
""",
    )


@kasta_cmd(
    pattern="test$",
)
@kasta_cmd(
    pattern="gtest(?: |$)(.*)",
    edited=True,
    own=True,
    senders=DEVS,
)
async def _(kst):
    is_devs = True if not kst.out else False
    clean = False
    if is_devs:
        opt = kst.pattern_match.group(1)
        if opt:
            user_id = version = None
            try:
                user_id = int(opt)
            except ValueError:
                version = opt
            if not version and user_id != kst.client.uid:
                return
            if not user_id and version == __version__:
                return
            clean = True
        if not clean:
            await asyncio.sleep(choice((4, 6, 8)))
    start = time.perf_counter()
    # http://www.timebie.com/std/utc
    utc_now = datetime.datetime.now(datetime.timezone.utc).strftime("%d/%m/%Y %H:%M:%S")
    msg = await kst.eor("`Processing...`", silent=True, force_reply=True)
    end = time.perf_counter()
    speed = end - start
    uptime = time_formatter((time.time() - StartTime) * 1000)
    text = test_text.format(
        kst.client.uid,
        Var.HEROKU_APP_NAME or "none",
        HerokuStack(),
        __version__,
        round(speed, 3),
        uptime,
        utc_now,
    )
    await msg.eor(
        text,
        parse_mode="html",
        time=15 if clean else 0,
    )


HELP.update(
    {
        "updater": [
            "Updater",
            """❯ `{i}update`
Checks for updates, also displaying the changelog.

❯ `{i}update <now|pull>`
Temporary update as locally.

❯ `{i}update <deploy|push>`
Permanently update as heroku.

❯ `{i}update <force|f>`
Force temporary update as locally.

❯ `{i}repo`
Get repo link.

❯ `{i}test`
Check the response.
""",
        ]
    }
)
