mylist = []
for i in range(4):
  user_number= int(input("Enter an number: "))
  mylist.append(user_number)
#print(mylist)
position=0
for i in range (4):
  print(mylist[position])
  position+=1
mylist[0], mylist[3]= mylist[3], mylist[0]
print(mylist)