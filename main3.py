#Iepakojot šo kortežu tā, lai mēs varētu atgriezt abus vienumus mainīgajam ar nosaukumu student, mēs varam modificēt savu kodu šādi.

def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)


if __name__ == "__main__":
    main()