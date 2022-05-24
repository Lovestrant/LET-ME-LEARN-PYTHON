# print ("Hello World!")

# age = input("Enter Age\n")
# username = input("Enter Username\n")

# print(f'hello, your age: {age} and username is {username}')

# Theage = int(age)
# sum = str(Theage)+"10"

# print(f"The sum is: {sum}")

#Python Arrays

# thearray = ["hello", "welcome", 20]

# print(f"The first element of Array: {thearray[0]}")
# print(f"The Last element of Array: {thearray[2]}")

# print(f"The whole Array: {thearray}")

# addFinalValue = input("Enter value to add to array\n")

# thearray.append(addFinalValue)
# print(f"The whole Array: {thearray}")

# popItemFromArray = input("Enter index to pop\n")

# thearray.pop()

# print(f"The whole Array: {thearray}")

# #Tuples, lists,dictionaries, 

# firstTuple = (1,3,4,6)

# myList = [[1,2,3], [3,4,5]]

# print(myList[0][2])

# firstTuple.append("Hello")

# print(f"Tuple is: {firstTuple}")

#Variable

# age = 30
# print(age)
# age = 59
# print(age)

# is_Online = False
# is_Not_Online = True

# if(is_Online == False) :
#     print("False")
# else :
#     print("True")

# #Convert Int to float
# # TheSum = input("Enter first: ")
# # sum = float(TheSum)

# # print("sum is: "+ str(sum))

# # sum = float(input("Enter The sum: "))

# # print(sum)

# hello_message = "Hello World"

# print(hello_message.upper())
# print(hello_message.lower())
# print(hello_message.capitalize())
# print(hello_message.casefold())
# print(hello_message.encode())

# print(hello_message.find("d"))

# print(hello_message.replace("e","o"))
# print(hello_message)

# print("hi" in hello_message)

# print("World" in hello_message.lower())

# #Arithmetic Operations

# print(3*2)
# print(3+3)
# print(12/2) #It returns a float number
# print(12//2) #It returns a int number

# x = 10

# print(x)
# x +=5
# print(x)

# x *=2
# print(x)

# x //=2
# print(x)

# #comparison operators <, > <=, >=, ==, !=

# comparison = 10 >5
# print(comparison)
# print(10 <5)

# print( 10 >=5)

# # Logical operators AND, OR, 

# price = 25

# print(price >100 and price < 30)

# temperature = 29

# if temperature > 30:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif temperature == 29:
#     print("Temperature is 29 degree Celcious")
#     print("It's almost hot, Prepare to drink plenty of water")
# else:
#     print("Not that much hot")
#     print("You might stop drinking lots of water")

# print("IF Exercusion Done")

# weightVal = float(input("Enter your Weight"))

# diamension = input("is your weight in Kg(K) or bounds(B)")

# if diamension.lower() == "k":
#     print(f"Your weight is: {weightVal}")
#     print("Thank you")
# elif diamension.lower() == "b":
#     weightVal = weightVal/2.22
#     print(weightVal)
# else:
#     print("Invalid Input")


#While Loops

i = 1
while i<=10:
    print(f"The I Val is: {i}")
    print("*" * i)
    i +=1

names = ["John", "Kips", "Jeroo", "Dennis"]
print(names[0:2]) #It excludes the end Index

names.insert(2, "Joy")

print(names)

# names.remove("Jeroo") # This removes a named value from an array list
# print(names)

# names.clear()
# print(names)

print(1 in names) # Returns false if 1 don't exist in array
print('Kips'  in names)

print(len(names))

#For Loops in Python
for Items in names:
    print(Items)

# Same as

items = 1
while items < len(names):
    print(names[items])
    items += 1


numbers = range(5)
for items in numbers:
    print(items)

theNumbers = range(5,11)

for num in theNumbers:
    print(num)







