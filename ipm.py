import os
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file")
args = parser.parse_args()

with open(args.file) as file:
    park = file.read()
    park = park.splitlines()
    for ip in park:
        result=subprocess.Popen(["ping", ip], stdout=file, stderr=file).wait()
        if result:
                print(ip, "inactive")
        else:
                print(ip, "active")
