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

while True:
    yourInput = input("> ")
    if yourInput[0] == "#" :
        continue
    if yourInput == "done" :
        break
    print(yourInput)
print("Done!")
    
      
    
    