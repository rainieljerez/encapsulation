class Pet:

    def __init__(self, name='', animal_type='', age=0):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

def get_pet_input():
    print("================")
    print ("Pet Information")
    name = input("Enter pet's name: ")
    animal_type = input("Enter pet's animal type: ")
    age = int(input("Enter pet's age: "))
    print("================")

    my_pet = Pet()
    my_pet.set_name(name)
    my_pet.set_animal_type(animal_type)
    my_pet.set_age(age)

    return my_pet

def display_pet(pet):
    print("")
    print("================")
    print("Pet Information")
    print(f"Name:        {pet.get_name()}")
    print(f"Animal Type: {pet.get_animal_type()}")
    print(f"Age:         {pet.get_age()} year(s) old")
    print("================")


def main():
    my_pet = get_pet_input()
    display_pet(my_pet)


if __name__ == "__main__":
    main()
