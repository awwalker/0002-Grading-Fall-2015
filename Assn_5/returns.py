import funcynum as fn
import unittest

class Tester(unittest.TestCase):
    #assumes test is given as hl(char, width, offset
    def test_horizontal_line(self):
        self.assertEqual(fn.horizontal_line('*', 5, 0), '*****')
        self.assertEqual(fn.horizontal_line('x', 2, 4), '    xx')
        

    def test_vertical_line(self):
        self.assertEqual(fn.vertical_line('*',2, 5), "     *\n     *")
        self.assertEqual(fn.vertical_line('x',5, 0), "x\nx\nx\nx\nx")
    #assumes comes as (char, height, offset, number, interior_offset)
    def test_vertical_lines(self):
        self.assertEqual(fn.vertical_lines('+', 4, 0, 5,3), """+   +   +   +   +
+   +   +   +   +
+   +   +   +   +
+   +   +   +   +""")

    
    def test_check_answer(self):
        self.assertTrue(fn.check_answer(1, 2, 3, "+"))
        self.assertTrue(fn.check_answer(1, 2, -1, "-"))
        self.assertFalse(fn.check_answer(9, 5, 3, "+"))
        self.assertFalse(fn.check_answer(8, 2, 4, "-"))
        self.assertFalse(fn.check_answer(9, 5, 3, "*"))

if __name__ == "__main__":
    unittest.main()
