# filepath =PythonBasics/data/txt/testingfile.txt

#1. Reading txt files  _ Option 1 to read files

'''
filepath ="PythonBasics/data/txt/testingfile.txt"

file=open(filepath, "r")   # opening the file
desc=file.read()  # reading

file.close() # closing the file 

print(desc)
'''


#2 Option 2nd to read the  using with: U can use indixing here 

# filepath ="PythonBasics/data/txt/testingfile.txt"
# with open(filepath, "r") as file:
#     data=file.read()

# print(data)
# print(type(data))

# If u want lines in a list 
# with open(filepath, "r") as file2:
#     data_in_lines =  file2.readlines()

# print( data_in_lines)
# print(type(data_in_lines))

# print(data_in_lines[3])


# with open(filepath, "r") as file3:
#     first_line=file3.readline()
#     second_line=file3.readline()
#     third_line=file3.readline()

# print(f"1st line: {first_line} 2nd line: {second_line}")


# print(type(first_line))

# phonenum=int(third_line)

# print(f"{phonenum }, {type(phonenum)}")


# with open(filepath, "r") as file4:
#     for num,data in enumerate(file4, start=1):
#         remove_blackslashn=data.strip() 
#         print(f"{num} Line {data}")



# How to write in files 

# Even if file path is wrong it will create new patha dn store the data 

# filepath2 ="PythonBasics/data/txt/writefile.txt67"

# data="Hello,  How r u 2 \ni am fine"

# with open(filepath2, "w") as file:
#     file.write(data)

# print("File is done check : ",filepath2 )


# sample_list = [
#     "First line of text\n",
#     "Second line of text\n",
#     "Third line of text\n",
#     "Fourth line of text\n",
#     "Fifth line of text"
# ]
# filepath2 ="PythonBasics/data/txt/writefile.txt"
# with open(filepath2, "w" ) as file:
#     file.writelines(sample_list)
# print("File is written")


# Append: add data in existing files

filepath2 ="PythonBasics/data/txt/writefile.txt"

# data="\nHello 12 3"
# with open(filepath2, "a" ) as file: # use  a to perform append operations 
#     file.write("\nThis is a new append line")
#     file.write(data)

# print("Data appended")


# Split the lines for large files  based on new line (\n)

# with open(filepath2, "r") as file:
#     data_content=file.read()
 
# all_lines=data_content.splitlines()

# print(all_lines)

# print(all_lines[0])


# Split the lines based on space

# with open(filepath2, "r") as file3:
#     data=file3.read()

# words=data.split(" ") # split will divide the data based on space
# print(words)

 # If u want to search something inside the files

filepath ="PythonBasics/data/txt/testingfile.txt"
with open(filepath, "r") as file:
    data=file.read()

print(data)

if "Apple23" in data:
    print(f"Data is found")
    updateddata=data.replace("Apple", "Mango ")
    # If u want to reaplace something  in file only if data is there 
    with open( filepath, "w") as file:
        file.write(updateddata)
    print("Data is updated")

else:
    print("No data present: No update")
