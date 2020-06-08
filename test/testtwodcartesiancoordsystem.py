import unittest
import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from twodcartesiancoordsystem import TwoDCartesianCoordSystem

class TestTwoDCartesianCoordSystem(unittest.TestCase):
    def testComputeXAxisCoordinates(self):
        ccs = TwoDCartesianCoordSystem(origin=(80, 300), xLength=200, yLength=300, xRange=(-5, 15),
									 yRange=(50, -3))
        self.assertEqual(ccs.xAxisCoordStart, (30, 300))
        self.assertEqual(ccs.xAxisCoordEnd, (230, 300))

    def testComputeYAxisCoordinates(self):
        ccs = TwoDCartesianCoordSystem(origin=(80, 300), xLength=200, yLength=300, xRange=(-5, 15),
									 yRange=(50, -3))
        self.assertEqual(ccs.yAxisCoordStart, (80, 50))
        self.assertEqual(ccs.yAxisCoordEnd, (80, 350))

if __name__ == '__main__':
	unittest.main()