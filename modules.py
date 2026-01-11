import math
import my_module
import requests


# square root of any number
print(math.sqrt(16))
#this is a built in module


my_module.hello()#this is my module that prints hello world when we call it 
r = requests.get("https://www.google.com/")
print(r.text)#gives the html code for the link