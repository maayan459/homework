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
   
        with open(file_name, "wb") as new_file:
            new_file.write(byte_list_new)
        
            

    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    get_file(r"C:\Users\maaya\.vscode\.vscode\check.txt")