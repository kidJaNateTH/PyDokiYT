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
        if(c.message.lower() == "up"):
            print(f"{c.author.name} had pressd UP!")
            pydirectinput.keyDown("up")
            pydirectinput.keyUp("up")
        if(c.message.lower() == "down"):
            print(f"{c.author.name} had pressd DOWN!")
            pydirectinput.keyDown("down")
            pydirectinput.keyUp("down")
        if(c.message.lower() == "enter"):
            print(f"{c.author.name} had pressd ENTER!")
            pydirectinput.keyDown("enter")
            pydirectinput.keyUp("enter")
        if(c.message.lower() == "h"):
            print(f"{c.author.name} had pressd H!")
            pydirectinput.keyDown("h")
            pydirectinput.keyUp("h")
        if(c.message.lower() == "left"):
            print(f"{c.author.name} had pressd LEFT!")
            pydirectinput.keyDown("left")
            pydirectinput.keyUp("left")
        if(c.message.lower() == "right"):
            print(f"{c.author.name} had pressd RIGHT!")
            pydirectinput.keyDown("right")
            pydirectinput.keyUp("right")
        if(c.message.lower() == "space"):
            print(f"{c.author.name} had pressd SPACE!")
            pydirectinput.keyDown("space")
            pydirectinput.keyUp("space")
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
    

