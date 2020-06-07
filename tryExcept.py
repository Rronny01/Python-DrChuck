# Try-except error handling 1

astr = "Hello bob"
try:
  istr = int(astr) # int() cant convert letters to int
except:
    istr = -1
    
print("First =", istr)   

astr = "123"
try:
    istr = int(astr)
except:
    istr = int(astr)
print("Second =", istr)     
       

 





