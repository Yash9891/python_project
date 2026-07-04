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


# try:
#     result=10/0
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed  ")


# Handel erros in funtion 


def divide_safe(a,b):   
                try:
                    result=a/b
                except ZeroDivisionError as p:
                    print("Error found : ", p)
        
                except TypeError as e: # e= error
                    print(f"Error found : {e}")
                    print("Type of error ", type(e))
                else:
                     return result

# result=divide_safe(10,0)

# result=divide_safe(10, "33")
# print(result)


# Haldling file errors : FileNotFoundError
# file path ="PythonBasics/test.txt34"

def read_file(filepath):
        try:
            file=open(filepath, "r")
            data=file.read()
            print(data)
        except FileNotFoundError as e:
              print(f"Error in  {filepath} , Error Type: {type(e)}")
        finally:
              print("File reading is done")
              
        
# read_file("PythonBasics/test.txtyyyyy")


# How to captures multiple erros in a single line

def checking_value(value):
      try:
         ans=100/value
         print("Ans : ", ans)
      except (ZeroDivisionError, ValueError,TypeError ) as e:
        print(f"Somethig went wrong \nError: {type(e)}" )
# checking_value("2")


# Trigger your own erros : raising errors

def check_age(age):
      if age<0:
            raise ZeroDivisionError("Age can not be negative")
      if age>150:
            raise ZeroDivisionError("Age can not be greater then 100")
      print("Age: ", age)

# check_age(190)  
 
try:
    check_age(190)  
except ZeroDivisionError as e:
      print(f" Error handel : {e}")

          
        
              




