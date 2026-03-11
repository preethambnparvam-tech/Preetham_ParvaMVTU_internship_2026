multiplesof2 = {2,4,6,8,10,12,8}
print(multiplesof2,type(multiplesof2))

randomSet = {1,True,False,0}
print(randomSet)

#set methods:
# union, intersection,difference, copy, difference_update, intersection_update,isdisjoint, issubset, issuperset, pop, remove, symmetric_difference_update, update, clear, add

set1 = {3,5,11,5,19,7,21,2,6}

set2 = {13,6,8,12,15,9,11,19}
print( "S1: ",set1)
print("S2: ",set2)

#union(|)
print("Union S1 and S2: ", set1.union(set2))

#update(|=)
set1.union(set2)
print("S1:", set1)

set1.update(set2)
print("S1 modifies to: ", set1)
#intersection(&)
print("Intersection of S1 and S2: ", set1.intersection(set2))

#Difference(-=)
print("Difference S1 and S2:",set1.difference(set2))
print("Difference S2 and S1:",set2.difference(set1))

#difference_update(-)
# set1.difference_update(set2)
# print("After Difference(S1 - S2), S1 contains:", set1)

#symmetric_difference(^)
print("Symmetric Difference of S1 and S2: ", set1.symmetric_difference(set2))

#symmetric Difference update(^=)
set3 = set1 ^ set2
print("Symmetric difference update: ",set3)

#isdisjoint
print(set1.isdisjoint(set2))

#issubset and issuperset
set3 = {1,2,3,4,5,6,7,8}
set4 = {1,3,5,7}
print("S3 is a parent of S4",set3.issuperset(set4))
print("S4 is a child of S3",set4.issubset(set3))

#pop
print("Original S1: ",set1)
set1.pop()
set1.pop()
print("After pop S1 is: ",set1)

#discard
set1.discard(14)
print(set1)

#add
set1.add(50)
set1.add(27)
print("After adding S1: ",set1)

#copy
new_set = set1.copy()
print("Copied the item from S1: ", new_set)

#intersection_update(&=)
set1.intersection_update(set2)
print("Intersection_update:", set1)