class Model(object):
    __instance = None

    @staticmethod
    # декоратора @staticmethod - чтобы метод можно было вызвать через объекты данного класса,
    # но сам объект в качестве аргумента в них не передавался.
    def get_instance():
        if Model.__instance is None:
            Model()
        return Model.__instance

    def __init__(self):
        if Model.__instance is None:
            self.name = "Bella"
            self.surname = "Hadid"
            self.height = 184.2
        Model.__instance = self


def float_test(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def to_json(info):
    json = "{"
    # Метод items() возвращают список кортежей dict (key, value)
    for key, value in info.__dict__.items():
        json += "\"" + str(key) + "\": " + ((str(value)) if float_test(value) else ("\"" + str(value) + "\"")) + "  "
    json += "}"
    return json

if __name__ == "__main__":
    person = Model()  # синглтон
    print(person)
    person = Model.get_instance()
    print(person)
    print(to_json(person))

    ellie = Model()  # преобразование в json
    ellie.name = "Ellie"
    ellie.surname = "Bill"
    ellie.height = 180.2
    print(to_json(ellie))
