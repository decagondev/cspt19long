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
STORE      = 0b00010001 # store a number from the ram 2 byte ahead of the instruction in to a register denote from 1 byte ahead of the instruction in ram
PRINT_REG  = 0b01111101 # print a number at the index in to registers, provided by the number from current instruction + 1 in ram
ADD        = 0b01101101 # adds the num stored at the register at the index from ram 1 byte away from the instruction

# list for the ram.
ram = [
    PRINT_TOM,
    PRINT_NUM,
    23,
    STORE,
    1,
    10,
    STORE,
    3,
    20,
    PRINT_REG,
    1,
    PRINT_REG,
    3,
    ADD,
    1,
    3,
    PRINT_REG,
    1,
    PRINT_REG,
    3,
    HALT
]

# a program counter to keep track of what we are executing.
pc = 0

# registers
registers = [0] * 8 # r0 - r7

# a loop for the cpu execute cycle.
while True:
    # FETCH
    inst = ram[pc]

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
        
    else:
        print("I have no idea what you want me to do!?!?!")
        break


