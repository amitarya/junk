/* See COPYRIGHT for copyright information. */

#include <inc/stdio.h>
#include <inc/string.h>
#include <inc/assert.h>

#include <kern/monitor.h>
#include <kern/console.h>
#include <kern/pmap.h>
#include <kern/kclock.h>
#include <kern/env.h>
#include <kern/trap.h>
#include <kern/sched.h>
#include <kern/picirq.h>

#include <kern/vmm.h>

void
i386_init(void)
{
	extern char edata[], end[];

	// Before doing anything else, complete the ELF loading process.
	// Clear the uninitialized global data (BSS) section of our program.
	// This ensures that all static/global variables start out zero.
	memset(edata, 0, end - edata);

	// Initialize the console.
	// Can't call cprintf until after we do this!
	cons_init();

	//cprintf("6828 decimal is %o octal!\n", 6828);

	// Lab 2 memory management initialization functions
//	extern int _binary_obj_user_abc_size[];
//	cprintf("obj: %x ()\n",_binary_obj_user_abc_size);	
	i386_detect_memory();
	i386_vm_init();

	// Lab 3 user environment initialization functions
	env_init();
	idt_init();
	// Lab 4 multitasking initialization functions
	pic_init();
	kclock_init();
	// Should always have an idle process as first one.
	cprintf("creating idle\n");
	ENV_CREATE(user_idle);

	// Start fs.
	ENV_CREATE(fs_fs);
	ENV_CREATE(user_icode_kernel);
	cprintf("creating icode\n");
	ENV_CREATE(user_icode);
//	ENV_CREATE(user_forever);

	//ENV_CREATE2(TEST, TESTSIZE);
	
#if defined(TEST)
	// Don't touch -- used by grading script!
//	ENV_CREATE2(TEST, TESTSIZE);
#else
	// Touch all you want.
	// ENV_CREATE(user_testsandy);
//	 ENV_CREATE(user_writemotd);
//	ENV_CREATE(user_testfile);
//	ENV_CREATE(user_icode);
//	cprintf("creating helo\n");
//	ENV_CREATE(user_yield);
//	ENV_CREATE(user_yield);
//	ENV_CREATE(user_dumbfork);
	//ENV_CREATE(user_faultread);
	//ENV_CREATE(user_faultwrite);
	//ENV_CREATE(user_faultdie);
	//ENV_CREATE(user_faultalloc);
	//ENV_CREATE(user_faultallocbad);
	//ENV_CREATE(user_faultregs);
	//ENV_CREATE(user_testfile);
//	ENV_CREATE(user_kernel);
	//ENV_CREATE(user_forktree);
	//ENV_CREATE(user_mem_check
	//ENV_CREATE(user_mem_check);
#endif // TEST*

	// Schedule and run the first user environment!
	sched_yield();
}


/*
 * Variable panicstr contains argument to first call to panic; used as flag
 * to indicate that the kernel has already called panic.
 */
static const char *panicstr;
/*
 * Panic is called on unresolvable fatal errors.
 * It prints "panic: mesg", and then enters the kernel monitor.
 */
void
_panic(const char *file, int line, const char *fmt,...)
{
	va_list ap;

	if (panicstr)
		goto dead;
	panicstr = fmt;

	// Be extra sure that the machine is in as reasonable state
	__asm __volatile("cli; cld");

	va_start(ap, fmt);
	cprintf("kernel panic at %s:%d: ", file, line);
	vcprintf(fmt, ap);
	cprintf("\n");
	va_end(ap);

dead:
	/* break into the kernel monitor */
	while (1)
		monitor(NULL);
}

/* like panic, but don't */
void
_warn(const char *file, int line, const char *fmt,...)
{
	va_list ap;

	va_start(ap, fmt);
	cprintf("kernel warning at %s:%d: ", file, line);
	vcprintf(fmt, ap);
	cprintf("\n");
	va_end(ap);
}
