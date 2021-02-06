import unittest
import fullName

class TestFullName(unittest.TestCase):
    
    def test_fullName(self):
        self.assertEqual(fullName.fullName("Mark", "Gekelman"), "Mark Gekelman")

        with self.assertRaises(ValueError):
            fullName.fullName(0, 0)
        
if __name__ == '__main__':
    unittest.main()