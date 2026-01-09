name = " hello world "
print(len(name))#prints length of string
print(name.endswith("ld "))#check wheather it ends with that letter or no
print(name.startswith(" he"))#same as the previous one but checks for starting
print(name.capitalize())#make the first letter capital
print(name.upper(),name)#this function makes the string in upper case and creates a new string 
print(name.lower(),name)#this function makes the string in lower  case and creates a new string 
print(name.title())#changes the string to title case like all the new words first letter capital
print(name.strip())#removes space from right and left side of the string
print(name.lstrip())#removes space from left side of string only
print(name.rstrip())#removes space from right side of string only
print(name.find("hell"))#finds the index of given charecter
print(name.replace("world","Taufiq"))#replaces the given word by the name which we provide


text = "apple,bananas,mango"
print(text.split(","))#splits the string and convert it to lists
print(",".join(['apple', 'bananas', 'mango']))#converts the lists to string


a= "python1230"
print(a.isalpha())#checks the string contains only alphabets
print(a.isdigit())#checks the string contains only numeric values
print(a.isalnum())#checks wheater string contains both number andf alphabets 
print(a.isspace())#checks if string contains space
