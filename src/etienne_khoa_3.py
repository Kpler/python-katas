from dataclasses import dataclass


@dataclass(frozen=True)
class Employee2:
    first_name: str
    last_name: str

    def __str__(self):
        return f'my name is {self.last_name}, {self.first_name} {self.last_name}'


if __name__ == '__main__':
    toto = Employee2('Elon', "Tran")
    print(toto)
    tata = Employee2('Elon', "Tran")
    print(toto == tata)
    print(toto.__eq__(tata))