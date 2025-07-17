#variables 

name = "Ali" #string
#print("01",name)
name = "Janisar" #string
#print("02",name)
id3 = 20 #int
memberId = 1234 #int
height = 5.9  #float
isOnline = True #boolean

# #type casting
# print(type(name))
# print(type(id3))
# print(type(memberId))
# print(type(height))
# print(type(isOnline))


##scope 
# memberId = id3
# print(memberId)

# def scopeTesting(name):
#     name = "janisar"
#     print(name)

# scopeTesting("Mallah")
# scopeTesting("Salman")
# scopeTesting("Amir")


##Input
def get_string_input(prompt):
    value = input(prompt)
    if value.isdigit():
        print("❌ Error: Please enter text, not numbers.")
        return get_string_input(prompt)
    return value

def get_int_input(prompt):
    value = input(prompt)
    if value.isdigit():
        return int(value)
    else:
        print("❌ Error: Please enter a valid number.")
        return get_int_input(prompt)

name = get_string_input("Enter your name: ")
age = get_int_input("Enter your age: ")
qualification = get_string_input("Enter your qualification: ")
phoneNo = get_int_input("Enter your phone number: ")

print("\n✅ User Details:")
print("Name:", name)
print("Age:", age)
print("Qualification:", qualification)
print("Phone Number:", phoneNo)
