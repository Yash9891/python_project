# result=10/0
# print(result)


#invalid index 
# name="Yash"
# print(name[20000])


# ValueError
# int("helloo")

# a=int("10")  # will not give any error
# print(a)


#FileNotFoundError
# open("PythonBasics/14.er33ros.py")  # will give error if file not found

# x= "hello"    NameError:
# x.upper()


try:
    result=10/0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed  ")