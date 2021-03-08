from pytchat import LiveChatAsync
from concurrent.futures import CancelledError
import asyncio
import time
import pydirectinput
import os
import requests


liveID = ""


async def main():
    
    print("Doki Doki Youtube live chat controller! by NateTH")
    print("\n")
    liveID = input("ID live : ")
    os.system("cls")
    print(f"---------Starting live {liveID}---------")
    print("\n")
    livechat = LiveChatAsync(liveID, callback = func)
    while livechat.is_alive():
        await asyncio.sleep(3)

async def func(chatdata):
    
    for c in chatdata.items:
        message = c.message.lower()
        if message in "up down enter h left right space".split():
            print(f"{c.author.name} had pressd {message.upper()}!")
            pydirectinput.keyDown(message)
            pydirectinput.keyUp(message)
        await chatdata.tick_async()


def checkVersion():
    os.system("color 0")
    print("Starting : checking version...")

    thisVersion = "1.0"
    version = requests.get("https://pastebin.com/raw/74nyUZfr")
    os.system("cls")
    try:
        if(version.text != thisVersion):
            os.system("color 4")
            raise Exception("We'are have new version on github. Check it out! : https://github.com/kidJaNateTH/DokiDokiYT")
        else:
            os.system("color 3")
            try:
                loop = asyncio.get_event_loop()
                loop.run_until_complete(main())
            except CancelledError:
                pass
    except Exception as err:
        print(err)
        os.system("pause")


if __name__ == '__main__':
    checkVersion()
