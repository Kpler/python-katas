from datetime import datetime


class Employee:
    def __init__(self, first_name, last_name, birth_date=None):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def __str__(self):
        return f'my name is {self.last_name}, {self.first_name} {self.last_name}'

    def age(self):
        now = datetime.now()
        return (now - self.birth_date).days / 365


if __name__ == '__main__':
    toto = Employee('Madeleine', "D'haussy")
    toto.birth_date = datetime(2021, 7, 1)
    print(toto)
    print(toto.birth_date)
    print(toto.age())