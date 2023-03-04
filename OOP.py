# Консольный Калькулятор - пример итоговой Абстракции в ООП !!!
class Parser:
    def __init__(self):
        pass

    @staticmethod
    def __convert_type(value_str):
        result = 0
        if isinstance(value_str, str):
            if "." in value_str:
                result = float(value_str)
            else:
                result = int(value_str)
        return result

    def _parse(self, expression):
        packed_value = tuple(expression.split(" "))
        if len(packed_value) != 3:
            print("Wrong indentation, check your expression")
            return 0, 0, "+"
        a, op, b = packed_value
        return self.__convert_type(a), self.__convert_type(b), op


class Core:
    def __init__(self):
        self._parser = Parser()
        self._functions = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: a / b,
            "*": lambda a, b: a * b
        }

    def calculate(self, expression):
        a, b, op = self._parser._parse(expression)
        result = self._functions.get(op)(a, b)
        return result


class Interface:
    def __init__(self):
        self._core = Core()

    def run_calculator(self):
        while True:
            print("Enter your expression(example 2 + 2) ")
            expression = input()
            result = self._core.calculate(expression)
            print("Result: {} ".format(result))
            print("=" * 40)


if __name__ == "__main__":
    calculator = Interface()
    calculator.run_calculator()
