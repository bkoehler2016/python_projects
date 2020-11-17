#!/usr/bin/python3

def checkName(name):
  checkName = input("Is your name " + name + "? ") 
  
  if checkName.lower() == "yes":    
    print("Hello,", name)  
  else:    
    name = input("We're sorry about that. What is your name again? ")    
    print("Welcome,", name)

checkName("Keenan")