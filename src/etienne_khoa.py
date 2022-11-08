class Employee:
    _frozen = False

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self._frozen = True
#
    # def __setattr__(self, *args, **kwargs):
    #     # if attr in ['first_name', ]:  # 'last_name'
    #     if self._frozen:
    #         raise AttributeError('error')
    #     object.__setattr__(self, *args, **kwargs)

    def __str__(self):
        return f'my name is {self.last_name}, {self.first_name} {self.last_name}'


if __name__ == '__main__':
    toto = Employee('Elon', "D'haussy")
    print(toto.first_name)
    print(toto)
    toto.last_name = 'SF'
    # toto.first_name = 'SF'
    print(toto)
