# num=int(input("entere a number: "))
# bits=int(input("enter the number of bits: "))
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



# print("The binary number is:", become_binsary_again(num, bits))




def get_file(file_name):
    try:
        print(file_name)
        with open(file_name, "rb") as file:
            file_text = file.read()
            num=5
            byte_list=[]
            for byte in file_text:
                
                new_byte=byte^num
                byte_list.append(new_byte)
            byte_list_new = bytes(byte_list)

        print("Original bytes:", file_text[:50])    
        with open(file_name, "wb") as new_file:
            new_file.write(byte_list_new)
            
        with open(file_name, "rb") as file:
            modified_text = file.read() 


        # with open(file_name, "r") as new_file:
        #     new_file_text = new_file.read()
        #     print("The modified file content is:", new_file_text)
        print("Modified bytes:", modified_text[:50])

    except FileNotFoundError:
        print("File not found")

    




if __name__ == "__main__":
    get_file(r"C:\Users\maaya\.vscode\.vscode\check.txt")
