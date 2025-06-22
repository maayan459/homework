n=2
import sys
def check_words(n):
    
    try:
        with open(r"C:\Users\maaya\.vscode\.vscode\check2.txt", "r") as file:
            file_text = file.read()
            text_list= file_text.split(" ")
           
#text_list2=[file_text.split("space") for word in text_list]
        num_words={}
        for word in text_list:
         if word in num_words:
          num_words[word] += 1
         else:
           num_words[word] = 1
       

        sorted_list= sorted(num_words.items(), key=lambda x: x[1], reverse=True)
        for i in range(n):
         print("The most common word is:" , sorted_list[i][0], "with", sorted_list[i][1] ,"occurrences")
        
    except FileNotFoundError as e:
        print("The file does not exist. Please check the file name and try again.")

check_words(n)        
      
