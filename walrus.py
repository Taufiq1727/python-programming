def very_slow_func():
    print("Something.....")
    print("Something.....")
    print("Something.....")
    print("Something.....")
    print("Something.....")
    return 70

if((a:= very_slow_func())>10):
    print(a)


else:
    print("Its not greater than 10")

#while
while(data := input("enter a number")):
    print(data)
    if data == "q":
        break