class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        print("Создан объект " + self.first_name + " " + self.last_name)

    def PrintName(self):
        print(self.first_name)

    def PrintLastName(self):
        print(self.last_name)

    def PrintFullName(self):
        print(self.first_name + " " + self.last_name)
