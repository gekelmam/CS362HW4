import unittest
import cube

class TestCube(unittest.TestCase):
    
    def test_cubeFunc(self):
        self.assertEqual(cube.cubeFunc(5), 125)
        self.assertEqual(cube.cubeFunc(1), 1)
        with self.assertRaises(ValueError):
            cube.cubeFunc("three")
            cube.cubeFunc(-1)   
            cube.cubeFunc(0)
            

if __name__ == '__main__':
    unittest.main()