from random import randint

from instagrapi import Client as IClient
from instagrapi.exceptions import ChallengeRequired, TwoFactorRequired
from pyrogram import Client as PClient
from telethon.sessions import StringSession
from telethon.sync import TelegramClient


def main():
    print("T E A M    H E L L B O T   ! !")
    print("Hello!! Welcome to HellBot Session Generator\n")
    print("Human Verification Required !!")
    while True:
        verify = int(randint(1, 50))
        okvai = int(input(f"Enter {verify} to continue: "))
        if okvai == verify:
            print("\nChoose the string session type: \n1. HellBot (Telethon) \n2. Music Bot (Pyrogram) \n3. Instagram Session")
            while True:
                library = input("\nYour Choice: ")
                if library == "1":
                    generate_telethon_session()
                    break
                elif library == "2":
                    generate_pyro_session()
                    break
                elif library == "3":
                    generate_insta_session()
                    break
                else:
                    print("Please enter integer values (1/2/3 only).")
            break
        else:
            print("Verification Failed! Try Again:")


def generate_pyro_session():
    print("Pyrogram Session for Music Bot!", "BQCzJaWASNDqHgUm_LREE0SGfspc_Ftxy349R6yQej5BFygK_NuyDnzXRCTcE7QXpXbqoFNRQHLR0edrN-yLmGWG0CPJrxl82YqnjgO5xpn4siJKoDMhWcGiSy0r51n-OxnY9RBIcq0UlkxPVReD97bPgKsGys9TXQ-MwoHKNkfR-krQyfL-gm-IaNgKmbMDT_1hxVsAEYFPGkGiE4PSNrFvoKwo59ehraR4NsUTs2ELl5h2b9OjWJ2p6eL60nhttiaHjEawSSfI-3JhLra4wAsjhMMeNetOUonCLDIAg98ShUpiHBD3YdRRwwVonT_0QKzjNUuOgR4X9BaEYVdkCt3jAAAAAUgLerAA")
    APP_ID = int(input("\nEnter APP ID here:", "13976276"))
    API_HASH = input("\nEnter API HASH here:", "7f024cbc744a2f44569c3641b5ccecb7")
    with PClient(':memory:', api_id=APP_ID, api_hash=API_HASH) as hellbot:
        print("\nYour HellBot Session Is sent in your Telegram Saved Messages.")
        hellbot.send_message(
            "me",
            f"#HELLBOT_MUSIC #HELLBOT_SESSION #PYROGRAM\n\n`{hellbot.export_session_string()}`",
        )


def generate_telethon_session():
    print("\nTelethon Session For HellBot!", "1BVtsOKkBuxicIsKS-ayOnpp5KXFR8uKIgynmYRxz4G_mDo4cQjTSZuMBCy8pdynPHVMLnMMzZq0sCH1ffGFDe98eIycnXP_LB7pZNIKY7BZVRq-BAIuF76xDCE9s6GzgeFYRDQ7tpEXYkYEgUDEtr9OH4u3BB05-MXtrATkX72_QSUTNheSmtruS_HGiQeEdkadOf7D-cF_p96XJccpLA2ri4FPTWuJk2mZ3kZ16-lHYJS4xq2aN81myboD-SsAfAu0zjJmoDjm_WeZD6lzNA_BuvAyMo-_YJqBT8hAMIsqKhtBxEwi0KUpG8yYRPndALQBxMVbEAMPJE1IQxdLSIxn2F4w5ZjU=")
    APP_ID = int(input("\nEnter APP ID here:", "13976276"))
    API_HASH = input("\nEnter API HASH here:", "7f024cbc744a2f44569c3641b5ccecb7")
    with TelegramClient(StringSession(), APP_ID, API_HASH) as hellbot:
        print("\nYour HellBot Session Is sent in your Telegram Saved Messages.")
        hellbot.send_message(
            "me",
            f"#HELLBOT #HELLBOT_SESSION #TELETHON \n\n`{hellbot.session.save()}`",
        )


def generate_insta_session():
    print("Instagram Session For HellBot!", "47580232066%3A22j7PG1L5XIvxG%3A21%3AAY cOyPID5qFr2QQ9w9c7MB6vuuJCpzukI3tMDVSAOA")
    cl = IClient()
    username = input("Enter your Instagram Username:", "official_sumit806")
    password = input("Enter your Instagram Password:", "skcc112566")
    try:
        cl.login(username, password)
        xyz =  cl.get_settings()
        sessionid = xyz['authorization_data']['sessionid']
        print(f"Your Instagram Session is: \n>>> {sessionid}")
        print("\nCopy it from here and remember not to share it with anyone!")
    except (ChallengeRequired, TwoFactorRequired, Exception) as e:
        print(e)


def challenge_code(username, choice):
    while True:
        otp = input("Enter the OTP sent to your Email: ")
        if otp.isdigit():
            break
        else:
            print("Enter digits only!")
    return otp


main()

