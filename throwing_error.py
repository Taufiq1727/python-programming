a = int(input("enter number 1 :"))
b = int(input("enter number 2 :"))
if b == 0:
    raise ValueError("Please dont devide by 0")
print(f"The division is {a/b}")