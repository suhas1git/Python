mylist = []
mylist.append(1)
mylist.append(2**4)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

addlist=mylist+mylist
print "==========="
print addlist
print "==========="
mullist=mylist*4
print mullist
# prints out 1,2,3
for x in mylist:
    print(x)