import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file")
parser.add_argument("-t", "--bot-token")
parser.add_argument("-i", "--chat-id")
args = parser.parse_args()

with open(args.file) as file:
    park = file.read()
    park = park.splitlines()
    for ip in park:
        result=os.system("ping -c 1 " + ip)
        if result:
                print(ip, "inactive")
                requests.post(send_url, json={'chat_id': args.chat_id, 'text': '{ip} available!'})
        else:
                print(ip, "active")
                requests.post(send_url, json={'chat_id': args.chat_id, 'text': '{ip} active!'})
