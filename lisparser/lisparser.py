"""Interpreter of simple Lisp math with pretty printing abilities"""


ops = "+-*/"


class Expression:
    def __init__(self, input: str):
        self.expr = self.parse(input)

    def parse(self, expr: str):
        pass

    def evaluate(self) -> float:
        return 0

    def pretty_print(self) -> str:
        return ""
