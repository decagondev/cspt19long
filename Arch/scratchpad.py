# add_to_pc?

# LDI 
# 1
# 1 
# PRN <--- pc
# 2
LDI = 0b10000010
HLT = 0b00000001
pc = 0
mem = [
    LDI,
    2,
    3,
    HLT
]
# opperand_size = LDI >> 6
# add_to_pc = opperand_size + 1

# DECODE
inst = mem[pc]
add_to_pc = (inst >> 6) + 1
# print(opperand_size)

pc += add_to_pc
print(mem[pc])