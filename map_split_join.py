# l1=int(input())
# l1.sort()
# l2=[]
# l1=list(set(l1))
# l=len(l1)
# print("last ",l1[l-1])
# print("2nd last= ",l1[l-2])

#by map and split

list1=input()
list1=list(map(int,list1.split(" ")))
print(list1)

 #join
car=["benz","bmw","ferari"]
veh="gf gf fkj gfk"
print(car)
print(' '.join(veh.capitalize() for word in veh.split(' ')))

