# Напишем свой класс
class User:
    # Создадим функцию-конструктор с набором аргументов (ФИО и возраст)
    def __init__(self):
        self.f_name = None
        self.m_name = None
        self.l_name = None
        self.age = None

    # Создадим функцию, вводящую с клавиатуры данные пользователя
    def input_reg(self):
        self.f_name = input("Input First name: ")
        self.m_name = input("Input Middle name: ")
        self.l_name = input("Input Last name: ")
        self.age = input("Input Age: ")

    # Создадим функцию, сериализующую данные в строку для вывода на экран
    def serialize(self):
        return "First name: {}\n" \
               "Middle name: {}\n" \
               "Last name: {}\n" \
               "Age : {}\n" \
            .format(self.f_name, self.m_name, self.l_name, self.age)

class MaxUser(User):
    def __init__(self):
        super().__init__()
        self.gender = None

    def input_reg(self):
        super().input_reg()
        self.gender = input("Введите Ваш пол: ")

    def serialize(self):
        res = super().serialize()
        return res + "Gender: {}\n" \
            .format(self.gender)

perets = MaxUser()
perets.input_reg()
print(perets.serialize())
