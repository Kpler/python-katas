class Human:
    def __init__(self, first_name):
        self.first_name = first_name


class Employee(Human):
    def __init__(self, first_name, last_name):
        super().__init__(first_name)
        self.last_name = last_name

    def __str__(self):
        return f'my name is {self.last_name}, {self.first_name} {self.last_name}'


if __name__ == '__main__':
    toto = Employee('Elon', "D'haussy")
    print(toto)
