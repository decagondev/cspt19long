import sys
# components of a computer,
# What is a computer to us?

# data driven machine - that does STUFF!




# what is a cpu to us?
# unit that asks. What Next?
# FETCH, DECODE, EXECUTE
# what are registers to us?
# tiny super fast pieces of memory, built in to the CPU

# what is ram / memory to us?
# store that holds the instructions and data that the cpu is asking for
# a place for a software engineer to store a program (instructions and data)

# some instructions for the cpu.
PRINT_TOM = 0b01011010 # print tom to the console
PRINT_NUM = 0b10010000 # print a number stored in ram 1 byte ahead of the instruction
HALT      = 0b10110111 # halt the operation of our data driven machine
STORE      = 0b10000010 # store a number from the ram 2 byte ahead of the instruction in to a register denote from 1 byte ahead of the instruction in ram
PRINT_REG  = 0b01111101 # print a number at the index in to registers, provided by the number from current instruction + 1 in ram
ADD        = 0b01101101 # adds the num stored at the register at the index from ram 1 byte away from the instruction
PUSH = 0b01000101 # push the value at given reg to the ramn address pointed to by R7 (SP)
POP = 0b01000110 # pop the value in to given reg from ram pointed to by the sp
CALL = 0b01010000 
RET = 0b00010001

ram = [0] * 256

SP = 7

def load_mem(filename):
    try:
        addr = 0
        with open(filename) as f:
            for line in f:
                # split the line on #
                comment_split = line.split('#')
                # strip the data
                data = comment_split[0].strip()

                # deal with empty line
                if data == '':
                    continue

                # extract the value (convert the number to an int).
                val = int(data, 2)

                # store the val in ram at current address?
                ram[addr] = val

                # increment address
                addr += 1
    except FileNotFoundError:
        print(f"{sys.argv[0]}: {sys.argv[1]} not found.")
        sys.exit(2)
        
# list for the ram.
# ram = [
#     PRINT_TOM,
#     PRINT_NUM,
#     23,
#     STORE,
#     1,
#     10,
#     STORE,
#     3,
#     20,
#     PRINT_REG,
#     1,
#     PRINT_REG,
#     3,
#     ADD,
#     1,
#     3,
#     PRINT_REG,
#     1,
#     PRINT_REG,
#     3,
#     HALT
# ]
if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <filename>")
    sys.exit(1)

load_mem(sys.argv[1])
# a program counter to keep track of what we are executing.
pc = 0
sp = 7

# registers
registers = [0] * 8 # r0 - r7
registers[sp] = 0xf4


# a loop for the cpu execute cycle.
while True:
    # FETCH
    inst = ram[pc]
    opa = ram[pc + 1]
    opb = ram[pc + 2]

    # DECODE
    if inst == HALT:
        # EXECUTE
        break
        # DECODE
    elif inst == PRINT_TOM:
        # EXECUTE
        print("Tom")
        pc += 1

    elif inst == PRINT_NUM:
        # EXECUTE
        num = ram[pc + 1]
        print(num)
        # DECODE
        pc += 2

    elif inst == PRINT_REG:
        # EXECUTE
        reg_index = ram[pc + 1]
        num = registers[reg_index]
        print(num)
        # DECODE
        pc += 2

    elif inst == STORE:
        # EXECUTE
        reg_index = ram[pc + 1]
        num = ram[pc + 2]
        registers[reg_index] = num
        # DECODE
        pc += 3
    
    elif inst == ADD:
        # EXECUTE
        reg_index_a = ram[pc + 1]
        reg_index_b = ram[pc + 2]
        
        registers[reg_index_a] += registers[reg_index_b]
        # DECODE
        pc += 3

    elif inst == CALL:
        # EXECUTE
        reg_index_a = ram[pc + 1]
        

        # push the PC + 2 literal number on to the stack
        registers[sp] -= 1
        ram[registers[sp]] = pc + 2
        
        # move the pc to point to addr stored at given reg
        pc = registers[reg_index_a]
        # DECODE

    elif inst == RET:
        # pop the top of the stack on to pc
        pc = ram[registers[sp]]
        registers[sp] += 1

    
    elif inst == PUSH:
        # execute

        # decrement SP (R7)
        registers[sp] -= 1

        # put the val from ram in to reg
        ram[registers[sp]] = registers[opa]

    elif inst == POP:
        # execute
        # put the val from the ram pointed to by sp in to reg given in opa
        registers[opa] = ram[registers[sp]]

        # increment SP (R7)
        registers[sp] += 1

        
    else:
        print("I have no idea what you want me to do!?!?!")
        break


