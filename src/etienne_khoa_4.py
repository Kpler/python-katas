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

    def __eq__(self, other):
        return all(self.__getattribute__(attr) == other.__getattribute__(attr)
                   for attr in self.__dict__.keys())


if __name__ == '__main__':
    toto = Employee('Madeleine', "D'haussy")
    tata = Employee('Madeleine', "D'haussy")
    print(toto == tata)
    print(toto.__eq__(tata))
