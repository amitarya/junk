/* See COPYRIGHT for copyright information. */

#include <inc/mmu.h>
#include <inc/memlayout.h>
#include <inc/trap.h>

#include <kern/picirq.h>


###################################################################
# exceptions/interrupts
###################################################################

/* The TRAPHANDLER macro defines a globally-visible function for handling
 * a trap.  It pushes a trap number onto the stack, then jumps to _alltraps.
 * Use TRAPHANDLER for traps where the CPU automatically pushes an error code.
 */ 
#define TRAPHANDLER(name, num)						\
	.globl name;		/* define global symbol for 'name' */	\
	.type name, @function;	/* symbol type is function */		\
	.align 2;		/* align function definition */		\
	name:			/* function starts here */		\
	pushl $(num);							\
	jmp _alltraps

/* Use TRAPHANDLER_NOEC for traps where the CPU doesn't push an error code.
 * It pushes a 0 in place of the error code, so the trap frame has the same
 * format in either case.
 */
#define TRAPHANDLER_NOEC(name, num)					\
	.globl name;							\
	.type name, @function;						\
	.align 2;							\
	name:								\
	pushl $0;							\
	pushl $(num);							\
	jmp _alltraps

.text

/*
 * Lab 3: Your code here for generating entry points for the different traps.
 */
 TRAPHANDLER_NOEC(DivideByZero,T_DIVIDE)
 TRAPHANDLER(BadSegment,T_GPFLT)
 TRAPHANDLER(PageFault, T_PGFLT)
 TRAPHANDLER_NOEC(BreakPoint, T_BRKPT)
 TRAPHANDLER_NOEC(syscaller, T_SYSCALL)
 TRAPHANDLER_NOEC(vmm_syscall, VMM_SYSCALL)


TRAPHANDLER_NOEC(irq_timer, IRQ_OFFSET + IRQ_TIMER)
TRAPHANDLER_NOEC(irq_kbd, IRQ_OFFSET + IRQ_KBD)
TRAPHANDLER_NOEC(irq_slave, IRQ_OFFSET + IRQ_SLAVE)
TRAPHANDLER_NOEC(irq_ide, IRQ_OFFSET + IRQ_IDE)
TRAPHANDLER_NOEC(irq_error, IRQ_OFFSET + IRQ_ERROR)
TRAPHANDLER_NOEC(irq_spurious, IRQ_OFFSET + IRQ_SPURIOUS)
TRAPHANDLER_NOEC(irq_serial, IRQ_OFFSET + IRQ_SERIAL)
/*
 * Lab 3: Your code here for _alltraps
 */
_alltraps:
		pushl %ds
		pushl %es
		pushal
		movl $GD_KD, %eax
		movl %eax,%ds
		movl %eax,%es
		pushl %esp
		call trap



