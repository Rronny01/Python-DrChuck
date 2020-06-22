# while loop

# n = 5
# while n > 0:
#     print(n)
#     n = n-1
# print("loop ends!")
# print(n)

# Infinite loop

# n = 5 

# while n > 0:
#     print("Soap")
#     print("Rinse")
# print("Dry off")


# Breaking out of a loop

# while True:
#     line = input("> ")
#     if line == "done" :
#         break
#     print(line)
# print("Done!")    
    
    
# Finishing an iteration with continue

# while True:
#     yourInput = input("> ")
#     if yourInput[0] == "#" :
#         continue
#     if yourInput == "done" :
#         break
#     print(yourInput)
# print("Done!")

# while is indefinite loop

# for is definite loop

# A simple definite loop using for

# for i in [5, 4, 3, 2, 1]:
#     print(i)
# print("End of code")

# A definite loop using strings

# friends = ["Moh", "Sak", "Mub"] # an  array
# for friend in friends :
#     print("Happy Eid,", friend)
# print("End of code")


# loop idioms

# Looping through a set

# print("Before")
# for thing in [9, 12, 13, 32, 45, 56, 67]:
#     print(thing)
# print("After")


# finding the largest input Value

# largestSoFar = 1
# print("Before the largest: ", largestSoFar)
# for theNumber in [6, 56, 34, 34, 5, 90, 75]:
#     if theNumber > largestSoFar :
#         largestSoFar = theNumber
#     print("The number:", str(theNumber) + ", " + "Largest so far:", str(largestSoFar))
# print("After the largest: ", largestSoFar)


# counting in a loop

# ork = 0
# print("Before the:", ork)
# for thing in [9, 12, 34, 45, 43, 52, 90]:
#     ork = ork + 1
#     print("This is my num:", str(thing) + ". " + "This is turn #", str(ork))
# print("After the loop:", str(ork))

# summing in a looping

# starting = 0
# print("Before the:", starting)
# for thing in [9, 12, 34, 45, 43, 52, 90]:
#     starting = starting + thing
#     print("This is my num:", str(thing) + ". " + "Running total #", str(starting))
# print("After the loop:", str(starting))


# finding average in a looping
count = 0
sum = 0

print("At the beginning count:", str(count) + "; " + "Sum:", str(sum))
for value in [4, 56, 34, 34, 65, 49]:
    count = count + 1
    sum = sum + value
    print("Count:", str(count) + ", " + "Value:", str(value) + ", " + "Sum:", str(sum) )
print("At the end count:", str(count) + "; " + "Sum:", str(sum) + ", " + "Average:", str(sum/count))






    





    
      
    
    