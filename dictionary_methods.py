marks = {
    "harry ": 100,
    "shubham" : 56,
    "taufiq": 101
}
print(marks.items())#prints items in dictionary
print(marks.keys())#prints the keys of dict(lhs of the dict)
print(marks.values())#prints rhs of dict (keys value)
marks.update({"harry ": 99,"simran ": 100})#updates the marks from the dict
print(marks)

print(marks.get("taufiq2"))#prints none
# print(marks["taufiq2"])#error
marks.pop("taufiq")
print(marks)