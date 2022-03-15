class AnimalShelter():
    def __init__(self):
        self.cats = []
        self.dogs = []

    def enqueue(self, animal, type):
        if type == 'cat':
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeueCat(self):
        if len(self.cats) == 0:
            return None
        else:
            cat = self.cats.pop(0)
            return cat

    def dequeueDog(self):
        if len(self.dogs) == 0:
            return None
        else:
            dog = self.dogs.pop(0)
            return dog

    def dequeueAny(self):
        if len(self.cats) == 0:
            result = self.dogs.pop(0)
        else:
            result = self.cats.pop(0)
        return result


custQ = AnimalShelter()
custQ.enqueue('cat1', 'cat')
custQ.enqueue('cat2', 'cat')
custQ.enqueue('dog1', 'dog')
custQ.enqueue('cat3', 'cat')
custQ.enqueue('dog2', 'dog')
custQ.enqueue('cat4', 'cat')
custQ.enqueue('dog3', 'dog')
print(custQ.dequeueAny())
print(custQ.dequeueCat())
print(custQ.dequeueDog())
