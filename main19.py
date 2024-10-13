#Šeit ir piemērs, kā neizmantot klases metodi. Termināļa logā ierakstiet  code hat.py un kodējiet šādi:
import random


class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        print(name, "is in", random.choice(self.houses))


hat = Hat()
hat.sort("Harry")