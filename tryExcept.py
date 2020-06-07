# Try-except error handling 1

# astr = "Hello bob"
# try:
#   istr = int(astr) # int() cant convert letters to int
# except:
#     istr = -1
    
# print("First =", istr)   

# astr = "123"
# try:
#     istr = int(astr)
# except:
#     istr = int(astr)
# print("Second =", istr)     
       
# Sample try/except with user input

rawString = input("Enter a number: ")
try:
    inputValue = int(rawString)
except:
    inputValue = -1
    
if inputValue > 0:
    print("Nice work")
else:
    print("Not a number")
 





