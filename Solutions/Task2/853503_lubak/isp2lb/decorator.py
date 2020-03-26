def cached(func):
    summed_up = {}
    # Внутри себя декоратор определяет функцию-"обертку". Она будет обернута вокруг декорируемой,
    # получая возможность исполять произвольный код до и после неё
    def hash_table(num1, num2):
        # код который отрабатывает до вызова функции
        if summed_up.get(key(num1, num2)) or summed_up.get(key(num2, num1)):
            print("GET FROM TABLE: ", end=" ")
            return summed_up[key(num1, num2)]
        else:
            print("CALCULATING: ", end=" ")
            summed_up[key(num1, num2)] = func(num1, num2)
            summed_up[key(num2, num1)] = func(num1, num2)
            return func(num1, num2)

    return hash_table


@cached
def addition(a, b):
    return a + b


def key(a, b):
    return str(a)+str(b)




if __name__ == "__main__":
    try:
        while True:
            num1 = (input("First number: "))
            num2 = (input("Second number: "))
            print(addition(num1, num2))
    except ValueError:
        print("End")
