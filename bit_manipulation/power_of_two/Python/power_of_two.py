import math 
  
def logoftwo(x): 
    return (math.log10(x) / math.log10(2)); 
  
def isPowerOfTwo(n): 
    return (math.ceil(logoftwo(n)) == math.floor(logoftwo(n))); 
  
print("Enter an integer to check if it is a power of 2 or not")
n=int(input())
if(isPowerOfTwo(n)): 
    print("Yes"); 
else: 
    print("No"); 
