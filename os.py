import os 

a = os.listdir("dir")
print(a)
print(os.getcwd())#gives the current directory
print(os.path.exists("dir"))#true if this directory exists
# os.remove("taufiq.txt")
os.rmdir("dir")#removes the empty files