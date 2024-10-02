from Human import Human


class Teacher(Human):

    def __init__(self, name, lastname, subjects, __id=None):
        super().__init__(name, lastname, __id)
        self._subjects = subjects
        self._homeroom_class = None

    def set_class(self, _homeroom_class):
        self._homeroom_class = _homeroom_class
        self._homeroom_class._homeroom_teacher=self
    def get_class(self):
        return self._homeroom_class

    def __repr__(self):
        return f"teacher={self._name} {self._lastname}, {self._subjects}, homeroom_class={self._homeroom_class._grade}{self._homeroom_class._letter}"

    def __str__(self):
        if self._homeroom_class is not None:
            return f"Учитель: {self._name} {self._lastname}, Ведёт предметы: {[sub.value for sub in self._subjects]}, Руководитель класса: {self._homeroom_class._grade}{self._homeroom_class._letter}"
        else:
            return f"Учитель: {self._name} {self._lastname}, Ведёт предметы: {[sub.value for sub in self._subjects]}"
