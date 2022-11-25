import unittest
from Funcion import sum_numbers

class TestSum(unittest.TestCase):
    def test_sum_numbers_default_args (self):
        #Test de argumentos por defecto
        self.assertEqual(sum_numbers(),5050)
        self.assertEqual(sum_numbers(numbers=None), 5050)

    def test_sum_numbers_various_inputs(self):
        #Test de valores varios
        self.assertEqual(sum_numbers(range(1, 11)), 55)
        self.assertEqual(sum_numbers([1, 2, 3]),6)
        self.assertEqual(sum_numbers((1, 2, 3),6))
        self.assertEqual(sum_numbers([]),)
    
        
if __name__ == '__main__':
    unittest.main()