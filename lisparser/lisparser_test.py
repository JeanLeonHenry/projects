import unittest

from lisparser import parse, evaluate, prettify


class ParsingTest(unittest.TestCase):
    def test_parsing_valid_exprs(self):
        exprs = """(+ 1 2)
        (+ (+ 1 2) 3)
        (+ 3 (+ 1 2))
        (* (/ -6 4) (- 56 23))
        """.splitlines()
        exprs = map(str.strip, exprs)
        results = [
            ["+", "1", "2"],
            ["+", ["+", "1", "2"], "3"],
            ["+", "3", ["+", "1", "2"]],
            ["*", ["/", "-6", "4"], ["-", "56", "23"]],
        ]
        for expr, result in zip(exprs, results):
            with self.subTest(expr):
                self.assertEqual(parse(expr), result)

    def test_handle_unvalid_exprs(self):
        exprs = """(+  2)
        12 3 
        (+  2)
        (+  2345)
        ()
        (u 2 3)
        ()()
          
        (+  )""".splitlines()
        exprs = map(str.strip, exprs)
        for e in exprs:
            with self.subTest(e):

                def parse_raise():
                    parse(e)

                self.assertRaises(ValueError, parse_raise)

    def test_eval_valid_exprs(self):
        exprs = """(+ 1 2)
            (+ (+ 1 2) 3)
            (+ 3 (+ 1 2))
            (* (/ -6 4) (- 56 23))
            """.splitlines()
        exprs = map(str.strip, exprs)
        results = [3, 6, 6, -66]
        for expr, result in zip(exprs, results):
            with self.subTest(expr):
                self.assertEqual(evaluate(parse(expr)), result)

    def test_zero_division(self):
        exprs = """(/ 1 0)
            (/ 3 (+ -2 2))""".splitlines()
        exprs = map(str.strip, exprs)
        for expr in exprs:
            with self.subTest(expr):

                def divide_by_zero():
                    evaluate(parse(expr))

                self.assertRaises(ZeroDivisionError, divide_by_zero)

    def test_printing(self):
        exprs = """(+ 1 2)
        (+ (+ 1 2) 3)
        (+ 3 (+ 1 2))
        (* (/ -6 4) (- 56 23))""".splitlines()
        exprs = map(str.strip, exprs)
        results = [
            "(+ 1 2)",
            "(+ (+ 1 2)\n    3)",
            "(+ 3\n    (+ 1 2))",
            "(* (/ -6\n        4)\n    (- 56\n        23))"
        ]
        for e, r in zip(exprs, results):
            with self.subTest(e):
                self.assertEqual(prettify(parse(e)), r, f"Failed printing {e}")
