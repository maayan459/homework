num=int(input("entere a number: "))
bits=int(input("enter the number of bits: "))
def become_binary(num, bits):
    binay_num=bin(num)[2:].zfill(bits)
    return binay_num

def become_decimal(num,bits):
    binary=become_binary(num, bits)
    final=""
    for i in range(len(binary)):
        if binary[i]=='1':
            final += '0'
        else:
            final += '1'
 
    return int(final, 2)+1


def become_binsary_again(number,bits):
    num=become_decimal(number,bits)

    num=bin(num)[2:].zfill(bits)
    return num



print("The binary number is:", become_binsary_again(num, bits))