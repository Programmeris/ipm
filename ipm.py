import os
import subprocess

with open("ip.txt") as file:
    park = file.read()
    park = park.splitlines()
    for ip in park:
        result=subprocess.Popen(["ping", ip], stdout=file, stderr=file).wait()
        if result:
                print(ip, "inactive")
        else:
                print(ip, "active")
