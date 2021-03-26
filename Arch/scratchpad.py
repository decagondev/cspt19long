# # add_to_pc?

# # LDI 
# # 1
# # 1 
# # PRN <--- pc
# # 2
# LDI = 0b10000010
# HLT = 0b00000001
# pc = 0
# mem = [
#     LDI,
#     2,
#     3,
#     HLT
# ]
# # opperand_size = LDI >> 6
# # add_to_pc = opperand_size + 1

# # DECODE
# inst = mem[pc]
# add_to_pc = (inst >> 6) + 1
# # print(opperand_size)

# pc += add_to_pc
# print(mem[pc])

import sys
if len(sys.argv) != 2:
    # print the usage?
    print(f"Usage: {sys.argv[0]} <filename>")
    # exit
    sys.exit(1)

file_name = sys.argv[1]
# print(file_name)
try:
    with open(file_name) as f:
        for line in f:
            l = line.split('#')
            sanitized_l = l[0].strip()
            if sanitized_l == '':
                continue
            # print(l)
            print(int(sanitized_l, 2))
            # print(int(line, 2))

except FileNotFoundError:
    print(f"{sys.argv[0]}: {sys.argv[1]} not found.")
    sys.exit(2)