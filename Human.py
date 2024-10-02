import random as rand


class Human:
    all_id = set()

    def __init__(self, name, lastname, __id=None):
        self._name = name
        self._lastname = lastname
        if __id == None:
            self.__id = Human.id_maker()
        elif __id in Human.all_id:
            raise Exception('Такой id занят')
        else:
            self.__id = __id
        Human.all_id.add(self.__id)

    @staticmethod
    def id_maker():
        id = rand.randint(1, 1000)
        if id in Human.all_id:
            Human.id_maker()
        else:
            return id

    def __lt__(self, other):
        if self._lastname == other._lastname:
            return self._name < other._name
        else:
            return self._lastname < other._lastname

    def __hash__(self):
        return self.__id

    def __eq__(self, other):
        return self._name == other._lastname and self._lastname == other.name
