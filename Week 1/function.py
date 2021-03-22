import unittest


class Test_PerfectNumber(unittest.TestCase):

    def Test_Number_True(self):
        self.assertTrue(perfect_number(3))
    def Test_Number_False(self):
        self.assertFalse(perfect_number(4))


def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n



if __name__ == '__main__':
    unittest.main()