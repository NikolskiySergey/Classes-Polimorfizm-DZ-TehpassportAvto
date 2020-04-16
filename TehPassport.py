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


# ===========================================================================================

# Напишем класс с данными автомобиля:
class Auto:
    # Создадим функцию-конструктор с набором аргументов для авто
    def __init__(self):
        self.auto_name = None
        self.auto_class = None
        self.auto_color = None
        self.auto_engine = None

    # Создадим функцию, вводящую с клавиатуры данные авто
    def input_data(self):
        self.auto_name = input("Input Auto Name: ")
        self.auto_class = input("Input Auto Class: ")
        self.auto_color = input("Input Auto Color: ")
        self.auto_engine = input("Input Engine volume: ")

    # Создадим функцию, сериализующую данные в строку для вывода на экран
    def serialize(self):
        return "Auto Name: {}\n" \
               "Auto Class: {}\n" \
               "Auto Color: {}\n" \
               "Engine volume : {}\n" \
            .format(self.auto_name, self.auto_class, self.auto_color, self.auto_engine)

# ==================================================================================================================
# ==================================================================================================================

# Создадим дочерний класс от ДВУХ пердыдущих (MaxUser(сам дочерний от User()) и Auto()):
class TehPassport(MaxUser, Auto):

    def __init__(self):
        MaxUser.__init__(self)
        Auto.__init__(self)

    def input_All(self):
        super().input_reg()
        super().input_data()

    def serialize(self):
        print(MaxUser.serialize(self))
        print(Auto.serialize(self))


drandulet = TehPassport()
drandulet.input_All()
print(TehPassport.mro())
drandulet.serialize()

print("MaxUser<-TehPassport: ", issubclass(MaxUser, TehPassport))
print("MaxUser<-User: ", issubclass(MaxUser, User))
print("TehPassport<-MaxUser: ", issubclass(TehPassport, MaxUser))
print("TehPassport<-Auto: ", issubclass(TehPassport, Auto))