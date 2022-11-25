from unittest.mock import *
from unittest import TestCase, main

class SomeClass():
    def hidden_method(self):
        return 0
    
    def public_method(self,x):
        return self.hidden_method()+x

class TestSomeClass(TestCase):
    def test_public_methond(self):
        test_object=SomeClass()
        test_object.hidden_method= MagicMock(name="hidden-method")
        test_object.hidden_method.return_value=10
        res=test_object.public_method(5)
        self.assertEqual(15, res, "return value from public_method it's incorrect")

if __name__ == "__main__":
    main()


