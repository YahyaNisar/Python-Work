##3.4
guest=['omer', 'danial','abd.r','huzaifa']

print("List of my friends is:",guest)
print(guest[0].title()+", "+"You are invited to dinner at my house on Thursday at 9:30pm ")
print(guest[1].title()+", "+"You are invited to dinner at my house on Thursday at 9:30pm ")
print(guest[2].title()+", "+"You are invited to dinner at my house on Thursday at 9:30pm ")
# better method to print message was to creat a mesaage and store it in a varaible and then print a mesaage along with item in list
# it will take less time and message can also be used later
## I have to ask how to start printing list from the atart of line

##3.5

print(guest[1].title()+" "+"cannot make for Thursday" )

guest[1]="salman"
# alternative method


## insert funtion is used in a way guest.insert(1, "human"), dont forget to pit item in qotation marks ass well along with insert funtion in in normal barackets
print (guest[1],"you are invited to my party on Thursday")
print (guest)
#3.6
print( "Now i have found a bigger dinning table so i decided to invite some more friends to the party ")
guest.insert(0,"qanita")
guest.insert(3,"saleem")
guest.append("yahya")
print(guest)
print(guest[0].title()," you are my chief guest on Thursday")

#3.7
print("Sorry guys i got mad to invite so many friends, I forgot my new dining table is not going to arrive until next month, Telephone ka bill tumlogo ka baap bharega, phley wo bad mai prhai")
c=guest.pop(1)
d=guest.pop(1)
e=guest.pop(1)
f=guest.pop(1)
g=guest.pop(1)
print("\n\1")
print(guest)
print ("\n\3")
print("Sorry guys you people are not invited, so sad!:","\n"+c.title(),"\n"+d.title(),"\n"+e.title(),"\n"+f.title(),"\n"+g.title(),"\n")

# how to print list in new line with the strt without white space
print("People who are invited to my party:", "\n"+guest[0].title(), "\n"+guest[1])
del guest[0]
del guest[0]
print(guest)
#in del funtion there should be white spce betwenn del and list name like : del guest[0]
# i have to learn the how to add and remove line between output
