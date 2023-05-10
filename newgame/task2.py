class Animal:
    def __init__(self,type, voice):
        self.type = type
        self.voice = voice

    def makevoice(self):
        print(self.voice)

    def fight(self, other):
        print(self.type, 'fight', other.type)
# Класс животного, эземпляр с видом, вывод голоса животного

dog = Animal('dog', 'гав гав')
dog.makevoice()
print(dog.type)

cat = Animal('cat', 'meow')
cat.makevoice()
dog.fight(cat)