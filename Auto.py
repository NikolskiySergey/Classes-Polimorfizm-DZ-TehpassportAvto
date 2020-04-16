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

tachka = Auto()
tachka.__init__()
tachka.input_reg()
tachka.serialize()
print(tachka.serialize())