def is_greater_than_9(x):
    if x >9:
        return True
    else:
        return False


a = [1,23,4,543,35,43,2,33,3,454]
new = list(filter(is_greater_than_9, a))
print(new)
new = list(filter(lambda x : x>9 , a))#just using the lambda function
print(new)


