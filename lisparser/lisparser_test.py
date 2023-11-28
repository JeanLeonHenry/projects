import unittest

from lisparser import Expression, ops


class EvaluationTest(unittest.TestCase):
    def test_simple_operations(self):
        for op, res in zip(ops, [8, -2, 0.6, 15]):
            with self.subTest(op):
                self.assertEqual(Expression(f"({op} 3 5)").evaluate(), res)


class PrintingTest(unittest.TestCase):
    def test_depth_one(self):
        exprs = [
            ("(+ 3 5)", "(+ 3 5)"),
            ("(+ (+ 3 5) (+ 8 9))", "(+ (+ 3 5)\n  (+ 8 9))"),
        ]
        for expr, result in exprs:
            with self.subTest(expr):
                self.assertEqual(Expression(expr).pretty_print(), result)
