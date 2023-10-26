import os
import argparse
import requests

parser = argparse.ArgumentParser()
parser.description = "Simple Python script for monitoring IP available and send it to Telegram Bot"
parser.add_argument("-f", "--file", required=True)
parser.add_argument("-t", "--bot-token", required=True)
parser.add_argument("-i", "--chat-id", required=True)
args = parser.parse_args()

send_url = 'https://api.telegram.org/bot{token}/sendMessage'.format(token=args.bot_token)
not_available_ip_list = "\U0001F525 FIRING \n"
not_available_ip_counter = 0

if not os.path.exists(args.file):
    print('{file} must be exist. Please fix it and try again'.format(file=args.file))
    quit()

with open(args.file) as file:
    park = file.read()
    park = park.splitlines()
    for ip in park:
        result=os.system("ping -c 1 " + ip)
        if result:
            print(ip, "inactive")
            not_available_ip_list += "{ip} not available!\n".format(ip=ip)
            not_available_ip_counter += 1
        else:
            print(ip, "active")
#           requests.post(send_url, json={'chat_id': args.chat_id, 'text': '\U00002705 {ip} is available!'.format(ip=ip)})

not_available_ip_list += "\nNot available ip count: {not_available_ip_counter}".format(not_available_ip_counter=not_available_ip_counter)

status = requests.post(send_url, json={'chat_id': args.chat_id, 'text': not_available_ip_list})

print("request to telegram status: {status}".format(status=status))

print(not_available_ip_list)
