import os
import argparse
import requests

parser = argparse.ArgumentParser()
parser.description = "Simple Python script for monitoring IP available and send it to Telegram Bot"
parser.add_argument("-f", "--file")
parser.add_argument("-t", "--bot-token")
parser.add_argument("-i", "--chat-id")
args = parser.parse_args()

send_url = 'https://api.telegram.org/bot{token}/sendMessage'.format(token=args.bot_token)
not_available_ip_list = ""

with open(args.file) as file:
    park = file.read()
    park = park.splitlines()
    for ip in park:
        result=os.system("ping -c 1 " + ip)
        if result:
                print(ip, "inactive")
                not_available_ip_list += "\U0000274C {ip} not available!\n".format(ip=ip)
        else:
                print(ip, "active")
#                requests.post(send_url, json={'chat_id': args.chat_id, 'text': '\U00002705 {ip} is available!'.format(ip=ip)})

status = requests.post(send_url, json={'chat_id': args.chat_id, 'text': not_available_ip_list})

print("request to telegram status: {status}".format(status=status))

print(not_available_ip_list)
