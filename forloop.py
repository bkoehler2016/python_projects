"""
a way to print objects in a list
"""

a = ["Jared", 13, "Mary", 14, "Brigham", 12, "Ashley", 3, "Ben", 4] 
  
# printing the list using * operator separated  
# by space
print("printing the list using * operator separated by space")  
print(*a) 
  
# printing the list using * and sep operator 
print("printing lists separated by commas") 
  
print(*a, sep = ", ")  
  
# print in new line 
print("printing lists in new line") 
  
print(*a, sep = "\n") 