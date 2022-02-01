
import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
namesascsv = input("Give me everybody's names, separated by a comma. i.e: ', '\n")
names = namesascsv.split(", ")

# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#print(len(names))

num_items = len(names)
homienum = random.randint(0, num_items - 1)

print("It is " + names[homienum] + "'s turn to pay.")

