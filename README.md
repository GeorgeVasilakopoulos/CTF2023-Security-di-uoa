## 2023 Project 2

Your goal is to attack the server `project-2.csec.chatzi.org`.
You have the information that a pico server runs in http://project-2.csec.chatzi.org:8000,
the code of which can be found in the [following repository](https://github.com/chatziko/pico).
Also, you have stolen:
- The admin's username: `admin`
- The password: `8c6e2f34df08e2f879e61eeb9e8ba96f8d9e96d8033870f80127567d270d7d96`  
  (It must be given in an encrypted format)

Tasks:

1. Find the MD5 digest of the plaintext password
2. Find the plaintext password
3. Find the contents of `/etc/secret`
4. Find the output of `lspci` when executed in the server




## Answers:
1. ```ef281a07091268a0d779cf489d00380c```

2. ```aCEDIsRateRe```

3.

```⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⢀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣦⣴⣶⣶⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣤⣤⣤⣤⣤⣀⣀⣀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⠿⠟⠛⠛⠋⠉⠉⠉⠉⠉⠉⠛⠛⠛⠿⢷⣦⣤⣀⡹⠿⠿⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣴⣶⣶⣾⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣶⣶⣶⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣴⣿⠟⠉⠀⠀⠙⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠟⠀⠀⠀⠉⠙⢿⣦⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢦⣽⣿⡄⠀⠀⠀⠀⠀
⠀⠀⠀⣰⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣷⠀⠀⠀⠀⠀
⠀⠀⢰⣿⡏⣤⠀⠀⠀⠀⠀⢀⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣻⡀⠀⠀⢤⢠⣼⣿⡆⠀⠀⠀⠀
⠀⠀⠀⢿⣿⠁⠀⠀⠀⠀⣴⡾⠁⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣀⠀⠀⠀⠀⠀⠈⢻⣇⠀⠀⠈⣇⣿⣿⠀⠀⠀⠀⠀
⠀⠀⠀⢸⣿⠀⡀⣀⠀⢠⣿⠃⠀⠀⢀⣾⣿⣿⡿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⡷⠀⠀⠀⠀⠀⢸⣿⠀⢠⣠⣿⣿⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠈⢿⣷⣇⣽⠀⢈⡏⠀⠀⠀⠸⣿⣿⣿⣦⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣧⣤⠥⠀⠀⠀⠀⣿⣿⣧⣾⣿⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠛⠿⣿⣧⣾⣿⡄⠀⠀⠀⠙⠿⠿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠋⠀⠀⠀⠀⠀⢸⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⣿⡇⣴⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢶⣼⣿⣀⣠⣤⣤⣤⣀⠀⠀⠀⠀⠀
⠀⠀⣠⣶⣾⠿⠛⠛⠻⢷⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⡿⠋⠉⠉⠉⠛⢿⣦⡀⠀⠀
⢀⣾⡿⠋⠀⠀⠀⠀⠀⠀⠙⣿⡆⢀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣿⡟⠀⠀⠀⠀⠀⠀⠀⠹⣿⡆⠀
⣼⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⣸⣷⣿⣷⣧⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⠀⢠⡾⣠⣇⣠⣿⣿⣿⡇⠀⢀⠀⠀⠀⢀⠀⠀⢹⣷⠀
⣿⣷⡀⠀⣷⠀⠀⠀⣼⣦⣴⣿⠏⠙⠻⠿⣷⡿⠷⣶⣶⡾⠿⠿⠷⢶⣶⣦⣤⣾⣿⣷⣿⣿⠿⠿⠛⠛⠙⠻⣿⣤⣾⣇⠀⢀⣸⣇⣀⣼⣿⠃
⠘⢿⣿⣾⣿⣷⣴⣾⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠻⠿⠿⠿⠟⠛⠛⠁⠀


            You guessed it... puppies!
```


4.

```
0:00.0 Host bridge: Intel Corporation 440FX - 82441FX PMC [Natoma]
00:01.0 ISA bridge: Intel Corporation 82371SB PIIX3 ISA [Natoma/Triton II]
00:01.3 Non-VGA unclassified device: Intel Corporation 82371AB/EB/MB PIIX4 ACPI (rev 08)
00:03.0 VGA compatible controller: Amazon.com, Inc. Device 1111
00:04.0 Non-Volatile memory controller: Amazon.com, Inc. Device 8061
00:05.0 Ethernet controller: Amazon.com, Inc. Elastic Network Adapter (ENA)
```


## Report:



### 1. Finding the MD5 digest of the plaintext password

Upon first compiling a local instance of the server, we noticed -Wformat-security flag as a warning, indicating to a ```printf``` whose string argument was passed directly as argument, without a proper format specifier. 

```
printf(auth_username)
```

It then became clear that we could expose content from the stack by sending a request containing a username with format specifiers. After a few attempts, we managed to extract the MD5 digest, by sending ```%p %d %p %p %p %p %p %s %p``` as username. In the code that we developed, however, we followed a more repetitive approach:

```
Start by trying "%s" as username. If the password is not found, try "%x %s". If not found, try "%x%x %s". And so on...
```

By observing the server code, one can see that a pointer to the password is stored in the same stack frame, and therefore, the password will be found eventually, through this process.


### 2. Breaking the encryption

Our intuition behind the algorithm that breaks the encryption originated from the fact that **the server differentiates its response** when the padding is correct vs when the padding is incorrect.

According to the AES decryption protocol, after decrypting the first ciphertext block (in our case, the *only* block), the result gets xor'ed with the Initialization Vector.

By sending requests, differentiating each time the last byte of the IV, we noticed that in all but 2 cases, the response code is "500 Internal Server Error", implying that the padding is wrong. 

In the first of the two cases, the IV is the same as the one given, and the response verifies the password authorization. 

In the second case, however, the server replies with "Invalid Password", implying that the padding is correct and equal to 1. This means that the last byte of the padded plaintext, when xor'ed with the modified byte of IV, will result in a value of 1. The last byte of plaintext is given by: ``` ModByte xor 0x01 xor LastByte``` where ```LastByte``` is the last byte of the cipherblock.

This process can be generalized in order to find every byte of the plaintext password, in reverse order:


```
Initialize the list plain_text[16] with None
  
for i = index of last byte of the chiphertext block; to the first byte of the chiphertext block; i next byte:
  Replace this character (c') with all the ascii characters, until a character other than the original character (c) is found for which the padding is correct
  if c found:
    plain_text[i] = (16-i) ^ c ^ c'
  else
    plain_text[i] = 16-i
```

Note that in our case *we know* that the padded plaintext is exactly 16 bytes and for that reason we provided an algorithm for this case. This can be easily generalized, though.

It is easy to see that this algorithm makes no more than 16*256 requests. We made a few modifications in order to improve it: 
  - We sorted the ascii values in an order that we presumed to be more probable
  - After finding the last byte, we avoided calculating other padding bytes 



### 3. Stealing ```/etc/secret```

To achieve buffer overflow, we first identified what safeguards the server creators had taken in order to avoid such an attack, in detail:

- Canaries
- Non-executable stack
- Address Space Layout Randomization (ASLR)

Since we had a non-executable stack, we couldn't inject our own code in the buffer and execute it through the buffer overflow, so we had to divert the execution elsewhere, namely, into ```send_file()``` (main.c), with a pointer to ```/etc/secret``` as argument.

Then we took the following approach:


- Initially, we noticed that in ```post_param```, the buffer```post_data``` is allocated dynamically *in the stack*. After careful observation we noticed that the size of the buffer originates from the Content-Length parameter of the post request. 


  ``` 
  t += 3; // now the *t shall be the beginning of user payload, after \r\n
  t2 = request_header("Content-Length"); // and the related header if there is
  payload = t;
  payload_size = t2 ? atol(t2) : (rcvd - (t - buf));
  
  ```

  Of course, Content-Length is simply a label, and it is possible to send a request with a faulty Content-Length value. So, we decided to give Content-Length a value of 66 and put something much larger in the buffer (post_data) via strcpy, which will cause the buffer to overflow

  ```⠀ 
  char post_data[payload_size+1];     // dynamic size, to ensure it's big enough
  strcpy(post_data, payload);
  ```

- Since ASLR shuffles addresses, we calculated the following addresses by determining their offsets from known addresses, exploited through the string format vulnerability of question 1:
    - buffer address
    - ```send_file()``` address
    -  original return address of post_param back to route.

- Similarly, the value of the canary variable was found directly through a string format attack.

- Then, we observed the placement of *local variables* in the stack:
  
          |/etc/secret|\0|80*trash|26*trash|param_name|8*trash|name|c|4*trash|p_post_data|value|

  (trash space does not require special initialization)

  These stack positions directly correspond to variables in the c program:
  - ```param_name``` is a char pointer, the argument of ```post_param()```.
  - ```name```, ```c``` and ```value``` correspond to 'temporary' variables used in the program. Initialization not required.
  - ```p_post_data``` is a pointer through which the buffer is meant to be accessed. 
  

- Next to the local variables, there were a few other parameters that were contained into the stack:

  - The Canary value
  - Old values of ```$ebx```, ```$esi```, ```$ebp```

  It was necessary to overwrite the values of the registers ***with their original values**, in order for the execution to continue back to ```route()``` after being diverted to ```send_file()```. If the program were to terminate abnormally after the execution of ```send_file()```, the contents of ```/etc/source``` would not be contained into the response request. In order to ensure the inclusion of the file into the request, it was necessary to divert the execution back to ```route()```, so that ``fflush()``, ```shutdown()``` and ```close()``` would get called.

- Finally, next to all of these parameters, the **return address** is located.

After careful offset calculations, we deduced the format of the stack frame:
```  
|post_data|26*trash|param_name|8*trash|name|c|4*trash|p_post_data|value|canary|old_ebx|old_esi|old_ebp|return address of frame|
```  

Then, we proceeded to overwrite the stack with the approprate data:
  - We inserted the register values and the canary in their respective positions.
  - As return address of the frame, we inserted the address of ```send_file()```
  - Adjacently, we inserted the original return address, so that the execution is continued smoothly. 
  - Next, we inserted a pointer (aka address) to the beginning of the buffer after the return address (this is the argument of ```send_file()```)
  - We inserted ```"/etc/secret"+'\0'``` into the buffer
  - We initialized ```p_post_data``` to point at the beginning of the buffer, as it was originally intended.
  - We initialized ```param_name``` with a pointer pointing to the terminating '\0' character (It has to point to a valid address, otherwise the second loop could fail)
  - Segments that are overwritten during the execution of ```post_param()``` and the excess buffer storage, were arbitrarily initialized with '!'.





Finally, the overflowed buffer had the following form:

```
                      ____________________________________________________________________________________________________
                     |                                                                                                   v
|/etc/secret\0|-80-| - |-8-|-4-|-4-|-4-| - |-4-|canary|old_ebx|old_esi|old_ebp|send_file addr.|original return addr.| - |'\0'|
^________________________________________|                                                                            |
^_____________________________________________________________________________________________________________________|


```   
A noteworthy obstacle that we encountered was that we were unable to insert '\0' characters directly into the buffer, since strcpy copies up to the first '\0' character. We overcame this problem by using this loop to our advantage: 

```⠀⠀
  for (char* c = post_data; *c != '\0'; c++)
    if (*c == '&' || *c == '=')
      *c = '\0';
```

Specifically, all we had to do was change '\0' characters to '&' and let the loop do the trick. Thankfully, no significant address contained the ascii values of = or &, as that would cause problems.


### 4. Gaining shell access - executing ```lspci```

In this part, we slightly modified the attack of part 3 and managed to access a shell in the server. Specifically:

  1. We located the address of the libc ```system()``` function and placed it (instead of ```send_file()```) in the return address segment of the frame.
  2. We placed a shell command such as ```lspci``` instead of  ```/etc/secret/```.

Originally, we thought that these changes would be sufficient to conduct the attack. However, we noticed that during the execution of ```system()```, the stack increases significantly and, consequently, the shell command gets overwritten **before it is executed**.

We thought of two ways to solve this problem: One would be to increase the buffer size in order for the instruction not to get overwritten by the frames of ```system()```. Another would be to move the command in another stack frame, after the injected addresses of functions. We followed the second approach, in order to avoid recalculating offsets.

After making this modification, the overwritten stack looked like this:


```
        ____________________________________________________________________________________________________________
       |                                                                                                            v
|-92-| - |-8-|-4-|-4-|-4-| - |-4-|canary|old_ebx|old_esi|old_ebp|send_file addr.|original return addr.| - |"lspci"|'\0'|
^__________________________|                                                                            |   ^
                                                                                                        |___|
```   

Another problem that we encountered was that the command overwrote some stored register values of the previous frame and that caused the program to crash, shortly after returning to ```route()```, when attempting to execute ```printf```. We overcame this problem simply by changing the original return address so that the execution continues a few (assembly) instructions after ```printf```, when the stack frame of ```route()``` is popped.

In the end, this approach was proven successful, as we were able to execute shell commands on the server and have it send back the result of the commands, without corrupting the graceful termination of each serving process.


