import unittest
from cubes import calculateCubes

class CubesTestCase(unittest.TestCase):
    """Tests for `cubes.py`."""

    def test_not_enough_to_fill(self):
        """ when the list of cubes is all zero we should get -1"""
        self.assertEqual(calculateCubes(1000, [0,0,0,0]), -1)

    def test_too_much_to_fill(self):
        '''when the list of cubes has values that are too big to fill cube A then we should get -1'''
        self.assertEqual(calculateCubes(1000, [0,0,0,0,4]), -1)

    def test_should_fill(self):
        ''' when we have values that can fill the cube exaclty we should return not -1'''
        self.assertEqual(calculateCubes(1000, [0,125,0,0]), 125)

    def test_should_overfill(self):
        ''' when we have values that can fill the cube and then we have extra'''
        self.assertEqual(calculateCubes(1000, [1000,120,0,0]), 160)

    def test_everything_is_zero(self):
        ''' when cubeA is 0 we should see -1 because you cant fill a nonexistant space with anything so it should be -1 '''
        ''' THIS IS BEHAVIOR I HAVE ASSUMED I DID NOT SEE A CASE LIKE THIS DESCRIBED IN THE PROBLEM STATEMENT '''
        self.assertEqual(calculateCubes(0, [0,0,0,0]), -1)

    def test_cubeA_is_zero_(self):
        ''' when cubeA is zero but the list of cubes is nto zero we should see -1'''
        self.assertEqual(calculateCubes(0, [233,12,1,2]), -1)

    def test_really_big_cubeA(self):
        ''' testing really big volume '''
        self.assertEqual(calculateCubes(1000000000, [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]), 496)


if __name__ == '__main__':
    unittest.main()
