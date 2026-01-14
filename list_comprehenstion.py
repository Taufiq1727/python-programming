#create a list cntaining the table of 5

a = 5
table = []
for i in range(1,11):
    table.append(a*i)

print(table)
#this method is long it can be rewrited as in this method -->

tables = [5*i for i in range(1,11)]
print(tables)
