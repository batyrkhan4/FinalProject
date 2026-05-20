class BaseOperation:
    """
    Base class for all calculator operations.
    """

    def __init__(self, result):
        self.result = result

    def get_expression(self):
        raise NotImplementedError("Subclasses must implement get_expression()")

    def get_result(self):
        return self.result


class BinaryOperation(BaseOperation):
    """
    Represents operations with two numbers, for example: 2 + 2.
    """

    def __init__(self, expression, result):
        super().__init__(result)
        self.expression = expression

    def get_expression(self):
        return self.expression


class ScientificOperation(BaseOperation):
    """
    Represents scientific operations, for example: sin(90), sqrt(16).
    """

    def __init__(self, function_name, value, result):
        super().__init__(result)
        self.function_name = function_name
        self.value = value

    def get_expression(self):
        return f"{self.function_name}({self.value})"