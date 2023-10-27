"""Used modules"""
import os
import sys
import argparse
import requests

def main():
    """Simple script for check ip avaliable and send result to Telegram Bot."""
    parser = argparse.ArgumentParser()
    parser.description = "Simple Python script for" \
                         "monitoring IP available and send it to Telegram Bot"
    parser.add_argument("-f", "--file", required=True)
    parser.add_argument("-t", "--bot-token", required=True)
    parser.add_argument("-i", "--chat-id", required=True)
    args = parser.parse_args()

    send_url = f'https://api.telegram.org/bot{args.bot_token}/sendMessage'
    not_available_ip_list = "\U0001F525 FIRING \n"
    not_available_ip_counter = 0

    if not os.path.exists(args.file):
        print(f'{args.file} must be exist. Please fix it and try again')
        sys.exit()

    if os.stat(args.file).st_size == 0:
        print(f'{args.file} is empty!')
        sys.exit()

    with open(args.file, encoding='UTF-8') as file:
        ip_list = file.read()
        ip_list = ip_list.splitlines()
        for verifiable_ip in ip_list:
            result=os.system("ping -c 1 " + verifiable_ip)
            if result:
                print(verifiable_ip, "inactive")
                not_available_ip_list += f"{verifiable_ip} not available!\n"
                not_available_ip_counter += 1

    not_available_ip_list += f"\nNot available ip count: {not_available_ip_counter}"
    status = requests.post(send_url, json={'chat_id': args.chat_id, 'text': not_available_ip_list}, timeout=10)
    print(f"request to telegram status: {status}")
    print(not_available_ip_list)

if __name__ == '__main__':
    main()
