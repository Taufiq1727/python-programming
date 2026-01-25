def marks(**kwargs):
    for item in kwargs.keys():
        print(f"The marks of {item} is {kwargs[item]}")

marks(shubham = 23,vikranth = 67, Taufiq = 100)