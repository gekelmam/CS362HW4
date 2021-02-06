import unittest
import avgElements

a = [0, -1, 3, 8, 9]
a0 = [1, 'W', 3]
a1 = []

class TestAvgElements(unittest.TestCase):
    
    def test_avgFunc(self):
        self.assertEqual(avgElements.avgFunc(a), 3.8)
        
        with self.assertRaises(ValueError):
            avgElements.avgFunc(a1)
            avgElements.avgFunc(a0)
        
if __name__ == '__main__':
    unittest.main()