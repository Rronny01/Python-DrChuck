# Example of functions; def == define function 1

# big = max("Hello world") 
# print(big)

# tiny = min("Hello world")
# print(tiny) # print (space) blank

# Building our own function

# favoriteNumber = input("What is your favorite number: ")
# print("Your favorite number is:", favoriteNumber) 

# def myFavoriteNumber(): 
#     n = 5
#     while n > 0:
#         n = n-1
# print("My favorite number is:", myFavoriteNumber()) # n == 0; none
        
        
# Parameters; with a placeholder/arguments 

# def greet(lang):
#     if lang == "es":
#         print("Hola")
        
#     elif lang == "fr":
#         print("Bonjour")       
        
#     else:
#         print("Hello")
        
# greet("en")  
# greet("fr")
# greet("es")    

# Example of functions; with Return keyword 

def greet(lang):
    if lang == "es":
        return"Hola"
        
    elif lang == "fr":
        return "Bonjour"      
        
    else:
        return "Hello"
        
print(greet("en"), "Mohammad")  
print(greet("fr"), "Sylvia")
print(greet("es"), "Manglia" )    

  
        
        
        
    


