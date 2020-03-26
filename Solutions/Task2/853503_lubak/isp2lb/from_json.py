class Model(object):
    def __init__(self):
        self.name = "Stella"
        self.surname = "Mcqueen"
        self.height = 178


def from_json(text, obj):
    word = ""
    write_symbol = False
    is_digit = False
    key_value = []
    for symbol in text:
        # проходит по каждому символу строке
        # нахождение чисел
        if symbol.isdigit():
            #  функция isdigit() явл. ли элемент строки числом.
            word += symbol
            is_digit = True
        elif symbol.isdigit() is False and is_digit is True:
            key_value.append(word)
            is_digit = False
            word = ""

        if write_symbol and symbol != '"':
            word += symbol
        elif write_symbol and symbol != " " and symbol != '"':
            word += symbol

        if symbol == '"' and write_symbol is False:
            write_symbol = True
        elif symbol == '"' and write_symbol:
            key_value.append(word)
            write_symbol = False
            word = ""

    i = 0
    #  setattr
    #  Метод используется, когда имя атрибута или значение заранее неизвестно и содержится в переменной.
    for key, value in obj.__dict__.items():
        if str(key) == key_value[i]:
            if type(value) is int:
                setattr(obj, key, int(key_value[i + 1]))
            elif type(value) is float:
                setattr(obj, key, float(key_value[i + 1]))
            elif type(value) is str:
                setattr(obj, key, key_value[i + 1])
        i += 2
    return obj


if __name__ == "__main__":
    person = Model()
    print("Old: ", person.__dict__)
    person = from_json('{"name": "Kendal", "surname": "Jenner", "height": 180}', person)
    print("New: ", person.__dict__)
