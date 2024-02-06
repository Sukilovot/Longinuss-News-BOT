import os

import praw
from dotenv import load_dotenv
from os import environ,listdir
load_dotenv("./.env")

bot_client = praw.Reddit(client_id=environ["BOT_ID"], client_secret=environ["BOT_SECRET"],
                         username=environ["ACC_USERNAME"], password=environ["ACC_PASSWORD"],
                         redirect_uri=environ["REDIRECT_URL"], user_agent=environ["USER_AGENT"]) # mf praw.. WHY urI???!
bot_client.auth.url(scopes=["identity"], state="...", duration="permanent")
bot_client.read_only = False
print(f"BOT: Logged as {bot_client.user.me()}")

subreddit = bot_client.subreddit("LonginussNews")
print("BOT: Entered into LonginussNews")
print("---")
for notice in os.listdir("./news"):
    notice_name = notice.replace(".txt", "")
    print(f"NOTICE: {notice_name}")
    print("BOT: Trying to POST the notice...")
    archive = open(f"./news/{notice}", "rb").read().decode()

    subreddit.submit(title=notice_name, selftext=archive)
    print(f"BOT: NOTICE {notice_name} POSTED!")