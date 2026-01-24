def divide(a,b):
    try :
        c= a/b
        print(c)
        return c

    except Exception as e:
        print(e)

    else:
        print("Hey I am good")  #excuted when no error

    finally:
        print("This is always executed") #this is always excuted


a = int(input("enter number 1:"))
b = int(input("enter number 2:"))
divide(a,b)

      