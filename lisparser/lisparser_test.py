import unittest

from lisparser import parse, evaluate


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
