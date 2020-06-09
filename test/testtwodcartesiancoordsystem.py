import unittest
import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from twodcartesiancoordsystem import TwoDCartesianCoordSystem

class TestTwoDCartesianCoordSystem(unittest.TestCase):
	def testComputeXAxisCoordinates_X_neg_X_pos(self):
		ccs = TwoDCartesianCoordSystem(origin=(80, 400), xLength=200, yLength=300, xRange=(-5, 15),
									   yRange=(50, -3), titleLst=["xR=(-5,15)", "yR=(50,-3)"])

		self.assertEqual((30, 400), ccs.xAxisCoordStart)
		self.assertEqual((230, 400), ccs.xAxisCoordEnd)

	def testComputeXAxisCoordinates_X_zero_X_pos(self):
		ccs = TwoDCartesianCoordSystem(origin=(500, 530), xLength=200, yLength=400, xRange=(0, 15),
										   yRange=(50, 3), titleLst=["xR=(0,15)", "yR=(50,3)"])

		self.assertEqual((500, 530), ccs.xAxisCoordStart)
		self.assertEqual((700, 530), ccs.xAxisCoordEnd)

	def testComputeXAxisCoordinates_X_pos_X_pos(self):
		ccs = TwoDCartesianCoordSystem(origin=(720, 530), xLength=200, yLength=400, xRange=(25, 55),
										   yRange=(50, 3), titleLst=["xR=(25,55)", "yR=(50,3)"])

		self.assertEqual((720, 530), ccs.xAxisCoordStart)
		self.assertEqual((920, 530), ccs.xAxisCoordEnd)

	def testComputeXAxisCoordinates_X_neg_X_neg(self):
		ccs = TwoDCartesianCoordSystem(origin=(1145, 550), xLength=200, yLength=400,
										   xRange=(-55, -5), yRange=(50, 0), titleLst=["xR=(-55,-5)", "yR=(50,0)"])

		self.assertEqual((945, 550), ccs.xAxisCoordStart)
		self.assertEqual((1145, 550), ccs.xAxisCoordEnd)

	def testComputeYAxisCoordinates_Y_pos_Y_neg(self):
		ccs = TwoDCartesianCoordSystem(origin=(300, 255), xLength=200, yLength=300, xRange=(-5, 15),
									   yRange=(30, -40), xLabel='Time', yLabel='Speed',
									   titleLst=["xR=(-5,15)", "yR=(30,-40)"])

		self.assertEqual((300, 135), ccs.yAxisCoordStart)
		self.assertEqual((300, 435), ccs.yAxisCoordEnd)

	def testComputeYAxisCoordinates_Y_pos_Y_zero(self):
		ccs = TwoDCartesianCoordSystem(origin=(1145, 550), xLength=200, yLength=400,
										   xRange=(-55, -5), yRange=(50, 0), titleLst=["xR=(-55,-5)", "yR=(50,0)"])

		self.assertEqual((1145, 150), ccs.yAxisCoordStart)
		self.assertEqual((1145, 550), ccs.yAxisCoordEnd)

	def testComputeYAxisCoordinates_Y_pos_Y_pos(self):
		ccs = TwoDCartesianCoordSystem(origin=(500, 530), xLength=200, yLength=400, xRange=(0, 15),
										   yRange=(50, 3), titleLst=["xR=(0,15)", "yR=(50,3)"])

		self.assertEqual((500, 130), ccs.yAxisCoordStart)
		self.assertEqual((500, 530), ccs.yAxisCoordEnd)

	def testComputeYAxisCoordinates_Y_neg_Y_neg(self):
		ccs = TwoDCartesianCoordSystem(origin=(300, 570), xLength=200, yLength=200, xRange=(0, 55),
										   yRange=(-50, -3), titleLst=["xR=(0,55)", "yR=(-50,-3)"])

		self.assertEqual((300, 570), ccs.yAxisCoordStart)
		self.assertEqual((300, 770), ccs.yAxisCoordEnd)

if __name__ == '__main__':
	unittest.main()
