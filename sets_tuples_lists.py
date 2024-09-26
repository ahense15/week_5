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

fruits[0] = "pineapple" #reassign values 
fruits.append("pineapple") # adds a value to the list
fruits.remove("apple") # removes an item from the list
fruits.insert(0, "pineapple") # inserts an item into a specific spot in the list
fruits.sort() # sorts the list alphabetically 
fruits.reverse() # reverses the list in order
fruits.clear()


# print(fruits[0])
for fruit in fruits:
    print(fruit)