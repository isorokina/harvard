#Tomēr mēs varam vēlēties palaist kārtošanas funkciju, neveidojot konkrētu kārtošanas cepures instanci (galu galā ir taču tikai viena cepure!). Mēs varam modificēt savu kodu šādi:

import random


class Hat:

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")