def add(a,b):
    x = a+b
    return x

c = add(3,5)
print(c)

#default argument
def add(a,b , plus = 0):
    x = a+b+plus
    return x

c = add(3,5,2)
print(c)

#keyword arguments
def student(name,age):
    print(f"name = {name}\nage = {age}")
    
student(age = 20,name = "Taufiq")
    

