import unittest

class Test_PerfectNumber(unittest.TestCase):
    def Test_Fizz(self):
        self.assertEquals(fizzbuzz(3), "fizz")
    def Test_Buzz(self):
        self.assertEquals(fizzbuzz(5), "buz")


def fizzbuzz(a):
            if a % 3 == 0:
                print('fizz')
            elif a % 5 == 0:
                print('buzz')
            else:
                print(a)
       


if __name__ == '__main__':
    unittest.main()