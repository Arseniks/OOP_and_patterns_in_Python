class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        for test_num in ('string', 1.5):
            with self.subTest(x=test_num):
                self.assertRaises(TypeError, factorize, test_num)

    def test_negative(self):
        for test_num in (-1, -10, -100):
            with self.subTest(x=test_num):
                self.assertRaises(ValueError, factorize, test_num)

    def test_zero_and_one_cases(self):
        for test_num in (0, 1):
            with self.subTest(x=test_num):
                self.assertEqual(factorize(test_num), (test_num, ))

    def test_simple_numbers(self):
        for test_num in (3, 13, 29):
            with self.subTest(x=test_num):
                self.assertEqual(factorize(test_num), (test_num, ))

    def test_two_simple_multipliers(self):
        for test_num, res in (6, (2, 3)), (26, (2, 13)), (121, (11, 11)):
            with self.subTest(x=test_num):
                self.assertEqual(factorize(test_num), res)

    def test_many_multipliers(self):
        for test_num, res in (1001, (7, 11, 13)),\
                             (9699690, (2, 3, 5, 7, 11, 13, 17, 19)):
            with self.subTest(x=test_num):
                self.assertEqual(factorize(test_num), res)
