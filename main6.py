#Šajā īstenošanā var izmantot arī vārdnīcu. Atcerieties, ka vārdnīcas nodrošina atslēgu un vērtību pāri.
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")


def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student


if __name__ == "__main__":
    main()