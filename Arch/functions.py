def print_a(z):
    print(z)

def f2(a):
    print_a(a)
    

def f1():
    x = 12
    f2(x)


f1()

# 00 LDI
# 01 3
# 02 3
# 03 CALL < PC => 03 >> PUSH 05
# 04 07
# 05 PRINT_TOM <- PC
# 06 HLT <- PC
# 07 PRN <- PC
# 08 3
# 09 RET <- PC => POP PC
# 0A
# 0B