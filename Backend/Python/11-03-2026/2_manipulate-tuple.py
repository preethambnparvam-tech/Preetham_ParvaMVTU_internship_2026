states = ("Karnataka", "Tamil Nadu", "Kerala")

statesList = list(states)
print(statesList)
print(type(statesList))

statesList.append("Maharastra")
print(statesList)

statesList.remove("Kerala")
print(statesList)

states = tuple(statesList)
print(states,type(states))