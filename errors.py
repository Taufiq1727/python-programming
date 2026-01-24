while True:
    try:
        a = int(input("enter number 1 :"))
        b = int(input("enter number 2 :"))
        print(f"The division is {a/b}")

    except ValueError:
        print("Please dont perform bad typecasts ")

    except ZeroDivisionError:
        print("not divisible by 0")


    except Exception as e:
        print("some error occured", e)