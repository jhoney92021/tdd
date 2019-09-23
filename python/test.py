# import for UNIT TESTING
import unittest

# thing to be tested ex: reverseArray
def reverseArray(list):
    pass

# actual test cases

class reverseArrayTest(unittest.TestCase):
    # each method is a case or test to be run on a unit 
    def testOne(self):
        self.assertEqual(reverseArray([1,2,3]), [3,2,1])



if __name__ == "__main__":
    unittest.main()
    # runs tests

