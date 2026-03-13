set1 = {3,5,11,5,19,7,21,2,6}

set2 = {13,6,8,12,15,9,11,19}
print( "S1: ",set1)
print("S2: ",set2)

#union(|)
print("Union S1 and S2: ", set1|set2)

#update(|=)
set1 |= set2
print("S1 is updated to: ", set1)

#intersection(&)
print("Intersection of S1 and S2: ", set1 & set2)

#Difference(-)
print("Difference S1 and S2:",set1 - set2)

#symmetric_difference(^)
print("Symmetric Difference of S1 and S2: ", set1 ^ set2)

#symmetric Difference update(^=)
set3 = set1 ^ set2
print("Symmetric difference update: ",set3)


#issuperset(>=)
set3 = {1,2,3,4,5,6,7,8}
set4 = {1,3,5,7}
print("S3 is a parent of S4",set3 >= set4)

#issubset(<=)
print("S4 is a child of S3",set3 <= set4)

#intersection_update(&=)
set1 &= set2
print("Intersection_update:", set1)

#difference_update(-=)
set1 -= set2
print("After Difference Update is:", set1)
