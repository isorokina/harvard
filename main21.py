#Atgriežoties pie students.py, mēs varam modificēt savu kodu šādi, risinot dažas neizmantotās iespējas saistībā ar @classmethod:

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()