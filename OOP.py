class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hi, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")

# Create an instance of the Person class
person = Person("Akinyi", 23, "female")

# Call the introduce method to display information about the person
person.introduce()