#Tomēr mūsu kodu var vēl vairāk uzlabot. Ievērojiet, ka ir nevajadzīgs mainīgais. Mēs varam noņemt student = {}, jo mums nav jāizveido tukša vārdnīca.
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}


if __name__ == "__main__":
    main()