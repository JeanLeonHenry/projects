"""Interpreter of simple Lisp math with pretty printing abilities"""


class Expression:
    def __init__(self, input: str):
        pass

    def evaluate(self) -> float:
        pass

    def pretty_print(self) -> str:
        pass


if __name__ == "__main__":
    expr = Expression(input("Input your expression : "))
    print(f"""
    Result : {expr.evaluate()}
    Print : 
    {expr.pretty_print()}
    """)
