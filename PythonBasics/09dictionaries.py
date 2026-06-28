#Dictionaries stores key value pairs-No indexing in Dictionaries

# dec={}
# print(type(dec))


#key can not be duplicate in dic
person={"name":["Prahsant","Yash"],
        "age":23,
        "city":"Pune",
        "salary":455657
        }


nestedPersons={

    "name":{

        "Yash":{
        "age"   :23,
        "city"  :"Pune"
    },
    "Prahsant":{
        "age"   :25,
        "city"  :"Mumbai"

    },
    "Prahsant":{
        "age"   :35,
        "city"  :"Jaipur"

    }
    
}
}

# print(person) #it will print the last value of key if key is duplicate in dic
    
 
#get value using key 
# print(person["name"]) #it will print the value of key name
# print(person.get("age")) #it will print the value of key age



#get data from nested dictionary

# print(nestedPersons["name"]["Prahsant"]["city"]) #it will print the city of Prahsant from nested dictionary


# u can use numbers as a key="yash",2

# numbers={
#     1:"Yash",
#     2:"Two",
#     3:["Three","Pop","List",45.6]
# }

# print(numbers[1]) #it will print the value of key 1

# print(numbers[3][1:])


#creating dic using zip function

# salary={2300,45999,6755,79999}
# names=["yash","Prashant","super","Pop"]

# dict1=dict(zip(names,salary))
# print(dict1)


# creating dict using constructor

# car=dict(brand="Toyota",price=345657,year=2026)
# print(car)

#How to find key is present in dic 


# for key1 in person:
#     print( key1, "Keys is available in dic :",  person[key1])


#name = key 
# if "name" in person:
#     print("Name is found", person["name"])


# get the key from nested dic

# if "name" in nestedPersons:
#     print("Present ", nestedPersons["name"])


# Update dic

# person["name"]="Yash"
# print(person)

#updating nested dict

# nestedPersons["name"]["Prahsant"]["city"]="Delhi"

# print(nestedPersons["name"]["Prahsant"])

# print(nestedPersons["name"]["Prahsant"]) 



#Merge two dics

# num1={"a":1,"b":34}
# num2={"b":38,"c":455}

# merged=num2|num1
# print(merged)


# print(person.keys())
# print(person.values())
# print(person.items())


# Square of elements  , u is key and u**2= value
squares={u:u**2 for u in range(1,11)}# 0,2,3,4,5,6   # last lement in range should be n+1 5 = 5+1
print(squares)