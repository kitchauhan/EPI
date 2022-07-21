import sys


print('starting the program')
def count_bits(x: int) -> int:
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits

print('Calling function '+ str(sys.maxsize))
bits = count_bits(5)

print(bits)  
print('program ended')  