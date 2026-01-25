with open("Taufiq.txt", "r")as f:
    content = f.read()
    print(content)#no need to write f.close() when using "with" syntax