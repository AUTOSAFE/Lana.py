#!/usr/bin/env python3
# Created By Project - evolution
import pyfiglet
import requests
import os
from time import sleep
from datetime import datetime
from pytz import timezone
from colorama import Fore, init

# Config
red = Fore.LIGHTRED_EX
green = Fore.LIGHTGREEN_EX
yellow = Fore.LIGHTYELLOW_EX
white = Fore.WHITE

init(autoreset=True)

def logTime():
    now_utc = datetime.now(timezone('UTC'))
    now_pacific = now_utc.astimezone(timezone("Asia/Jakarta"))
    return now_pacific.strftime("%H:%M:%S")

def banner(str):
    os.system("cls||clear")
    __banner__ = pyfiglet.figlet_format(str, font="slant", justify="center")
    print(red + __banner__)
    print(f"\t\t\t{yellow}[ {yellow}Created By : PROJECT EVOLUTION ! {red}]")
    print(f"\t\t{yellow}[ {yellow}This tools for Auto Crown and Trophy games Stumble{red} ]\n")

def start():
    banner("EVOLUTION")
    input_auth = input(f"{green}[{white}?{green}] {white}put in you Authorized : ")
    round_input = input(f"{green}[{white}?{green}] {white}put in you elimited (1, 2, 3) : ")
    delay_input = input(f"{green}[{white}?{green}] {white}Enter How fast is Crown (ex: 1 = 1sec) : ")

    while True:
        try:
            sleep(int(delay_input))
            req_game = requests.get(f"http://kitkabackend.eastus.cloudapp.azure.com:5010/round/finishv2/{round_input}", headers={
                "authorization": input_auth
            })
            if "BANNED" in str(req_game.text) or req_game.status_code == 403:
                print(f"{red}[{yellow}*{red}] {green}Account Give Banned")
                break
            elif "SERVER_ERROR" in str(req_game.text):
                continue
            elif "User" in str(req_game.text):
                print(f"{white}[{red}{logTime()}{white}] {yan}Nickname: {white}{req_game.json()['User']['Username']} {yellow}| Country: {white}{req_game.json()['User']['Country']} {white}| Trophy: {yellow}{req_game.json()['User']['SkillRating']} {white}| Crown: {yellow}{req_game.json()['User']['Crowns']}")
        except:
            continue

if __name__=="__main__":
    start()
