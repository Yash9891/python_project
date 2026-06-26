sentence="Harry poter good Harry Harry  is Good"  # any word or any list in python starts from 0 index 
# print(a[0:5]) # it will print from 0 to 4 index   

# print(a[-1]) # it will print last index of string  -1,-2,-3----------

# print(a[-5:]) 

#print length of a string

# print(len(sentence)) # it will print length of string 

# print(sentence.endswith("is good")) # it will return true if string ends with good otherwise false

#check count of a word in string
# print(sentence.count("Harry")) # it will return count of word in string

# print(sentence.capitalize()) # it will capitalize first letter of string

# print(sentence.lower())
# print(sentence.upper())

#how to get the inded in strings

# print(sentence.find("Good")) # it will return index of first letter of word in string

#Replace a word in string

# string2="Yash"
# replaced_string=sentence.replace("Harry",string2)
# print(replaced_string)



# Strings are immutable in python
name="Yash"
# name[0]="P" #it will give error because string is immutable in python
# print(name)

name1=name[1:]
print("P"+name1) #it will print Pash