#List properties:

vegetables = ["Carrot", "Tomato", "Potato", "Potato"]
print(vegetables, type(vegetables))

print(vegetables[0], vegetables[2])

#List methods:
# append, insert, remove, pop, clear, copy, extend, count, index, reverse, sort

#append
vegetables.append("Onion")
vegetables.append("Brinjal")
print(vegetables)

#insert
vegetables.insert(1, "Beans")
vegetables.insert(3, "Beetroot")
print(vegetables)

#pop
vegetables.pop()
vegetables.pop(3)
print(vegetables)

#remove
vegetables.remove("Carrot")
print(vegetables)

#count
potatoCount = vegetables.count("Potato")
print(potatoCount)

#copy
basket = vegetables.copy()
print(basket)

#Extend
fruits = ["Apple", "Banana", "Mango", "Apple"]
basket.extend(fruits)
print(basket) 

#reverse
basket.reverse()
print(basket)

#sort
basket.sort()
print(basket)

basket.sort(reverse=True)
print(basket)

#index
apple = basket.index("Apple")
print(apple)

#clear
vegetables.clear()
print(vegetables)