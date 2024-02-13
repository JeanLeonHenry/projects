"""Interpreter of simple Lisp math with pretty printing abilities"""

import re
import operator as op
from typing import Union, Sequence, List

Tree = Sequence[Union[str, 'Tree']]
OPS = dict(zip("+-*/", [op.add, op.sub, op.mul, op.floordiv]))


def is_simple(expr: str) -> bool:
    """Check if expr is a well formed simple expression."""
    match = re.fullmatch(r"\([\+\/\*-]\ -?\d+\ -?\d+\)", expr)
    return match is not None


def is_digit(expr: str) -> bool:
    return re.fullmatch(r"-?\d+", expr) is not None


def parse(expr: str) -> Tree:
    if not is_digit(expr):
        if is_simple(expr):
            # not a digit and simple
            return expr[1:-1].split()
    else:
        # expr is a digit
        return expr

    if (
        len(expr) < len("(+ 0 0)")
        or expr[0]+expr[-1] != "()"
        or expr[1] not in OPS.keys()
    ):
        raise ValueError(f"Expression '{expr}' is malformed.")

    operation = expr[1]
    to_parse = expr[3:-1]
    stack: List[str] = []
    split_index = None
    for index, c in enumerate(to_parse):
        if c == " " and not stack:
            # we met a space and the stack is empty
            # we found the first operand
            split_index = index
            break
        if c in "()":
            # we don't care about anything other than parens
            if c == "(":
                stack.append(c)  # we only append opening parens to the stack
            else:
                # we met a closing parens
                if stack:
                    # stack contains an opening parens we must close
                    stack.pop()
                    if not stack:
                        # we just emptied the stack
                        if index != len(to_parse)-1:
                            # we found the end of the first operand
                            split_index = index+1
                            break
    operands = [to_parse[:split_index],
                to_parse[split_index:].strip()]
    return [operation, *map(parse, operands)]


def evaluate(tree: Tree) -> int:
    if isinstance(tree, str):
        return int(tree)
    operation, *operands = tree
    evaluated = list(map(evaluate, operands))
    if operation == "/" and evaluated[1] == 0:
        raise ZeroDivisionError
    return OPS[operation](*evaluated)


if __name__ == "__main__":
    expr = input("Enter your lisp computation : ")
    try:
        print(evaluate(parse(expr)))
    except ValueError:
        print("Error : bad input")
    except ZeroDivisionError:
        print("Error: division by zero")
