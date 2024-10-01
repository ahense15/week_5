cars = ["bmw", "maserati", "audi", "mercades", "ferrari"]
print(f"these are the list of cars{cars}")
print(f"the first car is {cars[0]}")
print(f"the last car is {cars[-1]}")

cars[0]= "toyota"
print (f"the first car is {cars[0]}")

print(f"the last car is {cars[-1]}")
cars[-1] = "lamborghini"
print(f"the last car is {cars[-1]}")
cars.append("bugatti")
print(cars)
cars.remove("maserati")
#looping through the list
# otherwise c;;ed iteration through the list
# for car in cars:
    #print(len(car))
    #print(car)       
    #carRequest = input("add a new car please: ")
    #cars.append(carRequest)
    #print(cars)
    #print(len(cars))
    # print(cars.upper())
    #print(cars)
    #if len(cars) > 10:
        #break


#challenge
#create a list of friends
# make sure the initial list is none
friends = []
# add a new friend to the list, add at least 5 friends


# remove a friend
# insert a friend at a specific index maybe 2
friends.insert(0, "")
# print the list of friends
print(friends)
# loop through the list and print the friends name
for friend in friends:
    friendRequest = input("name a new friend: ")
    friends.append(friendRequest)
    if friends > 5:
        removeFriend=input("Who do you want me to remove")
        friends.remove(removeFriend)
        print(friends)
    if len(friends) > 10:
        break 

# see if a particular friend is in the list (boolean value)
# if the loop is greater than 10 break the look











# Collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates.
# Tuple = () ordered and unchangeable, duplicats OK, FASTER
fruits = ["apple", "orange", "banana", "coconut", "strawberry", "kiwi", "dragonfruit"]

# print(dir(fruits)) prints out all of the methods that come with the function 
# print(help(fruits)) tells what each method does 
#print(len(fruits)) tells how much in each list
# print("apple" in fruits)
# print("pineapple" in fruits)

# fruits[0] = "pineapple" #reassign values 
# fruits.append("pineapple") # adds a value to the list
# fruits.remove("apple") # removes an item from the list
# fruits.insert(0, "pineapple") # inserts an item into a specific spot in the list
# fruits.sort() # sorts the list alphabetically 
# fruits.reverse() # reverses the list in order
# fruits.clear()
prints(fruits.index("coconut"))

# print(fruits[0])
# for fruit in fruits:
   # print(fruit)


fruits = {"apple", "orange", "banana", "coconut", "kiwi", "plum", "avacado"}

 # fruits.pop()      pops off the first element in each instance
    # fruits.clear()      clears the set
    # fruits.add("pineapple")       adds an element
    # fruits.remove("apple")        removes an element
# print("apple" in fruits)      chacks if a specific element is in the set and will print a boolean

print(fruits)

# print(fruits[3])  doesn't work because sets are random and unordered.

fruits = ("apple", "orange", "banana", "coconut", "kiwi", "plum", "avacado")

# print(fruits.count("coconut"))
# print(fruits.index("apple"))

print(fruits)
for fruit in fruits:
    print(fruit)

#------------------------------------------------------------------------------------------------------------------
# dictionaries = a collection of {key:value} pairs, ordered and changeable. no duplicates
    
capitals = {
    "USA": "Washington D.C.",
    "India": "New Dehli",
    "China": "Beijing",
    "Russia": "Moscow"
}

# print(dir(capitals))
# print(help(capitals))
# print(capitals(capitals.get("Japan"))

if capitals.get("Russia"):
    print("the capital exists")
else:
    print("That doesnt exist")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detroit"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

print(capitals)

keys = capitals.keys()

for key in capitals():
    print(keys)

values = capitals.values()
for value in capitals.values():
    print(value)

items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")
