class Dog():

    # CLASS OBJECT ATTRIBUTES
    species = 'mammal'

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

sam = Dog('Lab', 'Frankie')

print(sam.breed)
print(sam.name)