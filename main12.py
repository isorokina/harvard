#Objektorientētā programma mudina jūs iekļaut visu klases funkcionalitāti klases definīcijā. Ko darīt, ja kaut kas noiet greizi? Ko darīt, ja kāds mēģina ierakstīt kaut ko nejauši? Ko darīt, ja kāds mēģina izveidot studentu bez vārda? Mainiet savu kodu šādi:

class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
