#testing class

class dog:
    def __init__(self, name, age, hungry, live, timeWF):
        self.name = name
        self.age = age
        self.hungry = False
        self.live = True
        self.timeWF = 0
    def eat(self):
        self.hungry = False
        self.timeWF = 0
        print(self.name + " is eating")
    def bark(self):
        print(self.name + " is barking")
    def info(self):
        print(f"{self.name} is {self.age} years old and its hungry status is {self.hungry}")
    def older(self):
        self.age += 1
        self.timeWF += 1
        self.hungry = True
        if self.age > 13:
            self.live = False
            print(f"{self.name} is dead")

        print(f"{self.name} is now {self.age} years old")
    def timeWithoutFood(self):
        if self.timeWF >= 3:
            self.live = False
            print(f"{self.name} is dead")
#little game
dog1 = dog(input("Enter the name of your dog: "), int(input("Enter the age of your dog: ")), False, True, 0)

while dog1.live:
    dog1.info()
    action = input("What you dog will do? (eat, bark, older): ").lower().strip()
    if action == "eat":
        dog1.eat()
    elif action == "bark":
        dog1.bark()
    elif action == "older":
        dog1.older()
    else:
        print("Invalid action")
    dog1.timeWithoutFood()
    