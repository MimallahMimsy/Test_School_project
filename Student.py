from Human import Human



class Student(Human):
    def __init__(self, name, lastname, _class = None, __id=None):
        super().__init__(name, lastname, __id)
        self._class = _class

    def set_class(self, st_class):
        self._class = st_class
        if self._class is not None:
            self._class._students.append(self)

    def get_class(self):
        return self._class

    def __str__(self):
        return f'{self._name} {self._lastname}'

    def __repr__(self):
        return f'{self._name} {self._lastname}'
