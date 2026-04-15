def write_file():  
    data = input("Enter data: ")  
    with open("data.txt", "w") as f:  
        f.write(data)  
 
def read_file():  
    try:  
        with open("data.txt", "r") as f:  
            print(f.read())  
    except:  
        print("File not found")  
 
def append_file():  
    data = input("Enter data: ")  
    with open("data.txt", "a") as f:  
        f.write("\n" + data)  
 
write_file()  
append_file()  
read_file() 