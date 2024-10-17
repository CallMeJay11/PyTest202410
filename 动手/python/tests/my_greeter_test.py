import unittest
#from src.my_greeter import MyGreeter
#增加系统路径，以便makefile编译时候能够认出my_greeter
import sys
sys.path.append(str('src/'))
from my_greeter import MyGreeter

class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._my_greeter = MyGreeter()

    def test_init(self):
        self.assertIsInstance(self._my_greeter, MyGreeter)

    def test_greeting(self):
        #self.assertTrue(len(self._my_greeter.greeting())>0)
        self.assertTrue(len(str(self._my_greeter.greeting()))>0)
        

if __name__ == '__main__':
    unittest.main()
