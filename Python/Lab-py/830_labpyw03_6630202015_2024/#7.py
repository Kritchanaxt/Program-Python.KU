#7. 
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']

print("Result for the dog show are as follows:\n")
for index, dog in enumerate(dogs):
    place = str(index)
    print("Place: " + place + "Dog" + dog.title())
    print("Place: " + place + "Dog" + dog[index])
