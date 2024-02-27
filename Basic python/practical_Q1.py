# Practical No.14
# Practical Related Question Q.1
class Animal:
    multicellular = True
    eukaryotic = True
    def breathe(self):
        print("I breathe oxygen.")

    def feed(self):
        print("I eat food.")

class Herbivorous(Animal):
    def feed(self):
        print("I eat only plants. I am vegetarian.")
        herbi = Herbivorous()
        herbi.feed()
        herbi.breathe()