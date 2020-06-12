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

	def testComputeXAxisCoordinates_X_neg_X_zero(self):
		ccs = TwoDCartesianCoordSystem(origin=(1145, 550), xLength=200, yLength=400,
										   xRange=(-55, 0), yRange=(50, 0), titleLst=["xR=(-55,0)", "yR=(50,0)"])

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

	def testComputeXAxisArrowCoordinates_X_neg_X_pos(self):
		origin = (80, 400)
		ccs = TwoDCartesianCoordSystem(origin=origin, xLength=200, yLength=300, xRange=(-5, 15),
									   yRange=(50, -3), titleLst=["xR=(-5,15)", "yR=(50,-3)"])

		self.assertEqual(((220, 385.0), (260, 400), (220, 415.0)), ccs.computeXAxisArrowCoordinates(origin, (60, 400), (260, 400)))

	def testComputeXAxisArrowCoordinates_X_zero_X_pos(self):
		origin = (500, 530)
		ccs = TwoDCartesianCoordSystem(origin=origin, xLength=200, yLength=300, xRange=(0, 15),
										   yRange=(50, 3), titleLst=["xR=(0,15)", "yR=(50,3)"])

		self.assertEqual(((660, 515.0), (700, 530), (660, 545.0)), ccs.computeXAxisArrowCoordinates(origin, (500, 530), (700, 530)))

	def testComputeXAxisArrowCoordinates_X_pos_X_pos(self):
		origin = (720, 530)
		ccs = TwoDCartesianCoordSystem(origin, xLength=200, yLength=400, xRange=(25, 55),
										   yRange=(50, 3), titleLst=["xR=(25,55)", "yR=(50,3)"])

		self.assertEqual(((880, 515.0), (920, 530), (880, 545.0)), ccs.computeXAxisArrowCoordinates(origin, (720, 530), (920, 530)))

	def testComputeXAxisArrowCoordinates_X_neg_X_neg(self):
		origin = (1145, 550)
		ccs = TwoDCartesianCoordSystem(origin, xLength=200, yLength=400,
										   xRange=(-55, -5), yRange=(50, 0), titleLst=["xR=(-55,-5)", "yR=(50,0)"])

		self.assertEqual(((985, 535.0), (945, 550), (985, 565.0)), ccs.computeXAxisArrowCoordinates(origin, (945, 550), (1145, 550)))

	def testComputeYAxisArrowCoordinates_Y_pos_Y_neg(self):
		origin = (300, 255)
		ccs = TwoDCartesianCoordSystem(origin, xLength=200, yLength=300, xRange=(-5, 15),
									   yRange=(30, -40), xLabel='Time', yLabel='Speed',
									   titleLst=["xR=(-5,15)", "yR=(30,-40)"])

		self.assertEqual(((285.0, 265), (300, 225), (315.0, 265)), ccs.computeYAxisArrowCoordinates(origin, (300, 225), (300, 525)))

	def testComputeYAxisArrowCoordinates_Y_pos_Y_zero(self):
		origin = (1145, 550)
		ccs = TwoDCartesianCoordSystem(origin, xLength=200, yLength=400,
										   xRange=(-55, -5), yRange=(50, 0), titleLst=["xR=(-55,-5)", "yR=(50,0)"])

		self.assertEqual(((1130.0, 540), (1145, 500), (1160.0, 540)), ccs.computeYAxisArrowCoordinates(origin, (1145, 500), (1145, 550)))

	def testComputeYAxisArrowCoordinates_Y_pos_Y_pos(self):
		origin = (500, 530)
		ccs = TwoDCartesianCoordSystem(origin, xLength=200, yLength=400, xRange=(0, 15),
										   yRange=(50, 3), titleLst=["xR=(0,15)", "yR=(50,3)"])

		self.assertEqual(((485.0, 520), (500, 480), (515.0, 520)), ccs.computeYAxisArrowCoordinates(origin, (500, 480), (500, 530)))

	def testComputeYAxisArrowCoordinates_Y_neg_Y_neg(self):
		origin = (300, 570)
		ccs = TwoDCartesianCoordSystem(origin, xLength=200, yLength=200, xRange=(0, 55),
										   yRange=(-50, -3), titleLst=["xR=(0,55)", "yR=(-50,-3)"])

		self.assertEqual(((285.0, 580), (300, 620), (315.0, 580)), ccs.computeYAxisArrowCoordinates(origin, (300, 570), (300, 620)))

	def testComputeXAxisLabelXCoordAndDirection_X_neg_X_pos(self):
		origin = (80, 400)
		ccs = TwoDCartesianCoordSystem(origin=origin, xLength=200, yLength=300, xRange=(-5, 15),
									   yRange=(50, -3), titleLst=["xR=(-5,15)", "yR=(50,-3)"])

		self.assertEqual((260, 1), ccs.computeXAxisLabelXCoordAndDirection(origin, (60, 400), (260, 400)))

	def testComputeXAxisLabelXCoordAndDirection_X_zero_X_pos(self):
		origin = (500, 530)
		ccs = TwoDCartesianCoordSystem(origin=origin, xLength=200, yLength=300, xRange=(0, 15),
										   yRange=(50, 3), titleLst=["xR=(0,15)", "yR=(50,3)"])

		self.assertEqual((700, 1), ccs.computeXAxisLabelXCoordAndDirection(origin, (500, 530), (700, 530)))

	def testComputeXAxisLabelXCoordAndDirection_X_pos_X_pos(self):
		origin = (720, 530)
		ccs = TwoDCartesianCoordSystem(origin, xLength=200, yLength=400, xRange=(25, 55),
										   yRange=(50, 3), titleLst=["xR=(25,55)", "yR=(50,3)"])

		self.assertEqual((920, 1), ccs.computeXAxisLabelXCoordAndDirection(origin, (720, 530), (920, 530)))

	def testComputeXAxisLabelXCoordAndDirection_X_neg_X_neg(self):
		origin = (1145, 550)
		ccs = TwoDCartesianCoordSystem(origin, xLength=200, yLength=400,
										   xRange=(-55, -5), yRange=(50, 0), titleLst=["xR=(-55,-5)", "yR=(50,0)"])

		self.assertEqual((945, -1), ccs.computeXAxisLabelXCoordAndDirection(origin, (945, 550), (1145, 550)))

	def testComputeYAxisLabelXCoordAndDirection_Y_pos_Y_neg(self):
		origin = (300, 255)
		ccs = TwoDCartesianCoordSystem(origin, xLength=200, yLength=300, xRange=(-5, 15),
									   yRange=(30, -40), xLabel='Time', yLabel='Speed',
									   titleLst=["xR=(-5,15)", "yR=(30,-40)"])

		self.assertEqual((300, 1), ccs.computeYAxisLabelXCoordAndDirection(origin, (300, 225)))

	def testComputeYAxisLabelXCoordAndDirection_Y_pos_Y_zero(self):
		origin = (1145, 550)
		ccs = TwoDCartesianCoordSystem(origin, xLength=200, yLength=400,
										   xRange=(-55, -5), yRange=(50, 0), titleLst=["xR=(-55,-5)", "yR=(50,0)"])

		self.assertEqual((1145, 1), ccs.computeYAxisLabelXCoordAndDirection(origin, (1145, 500)))

	def testComputeYAxisLabelXCoordAndDirection_Y_pos_Y_pos(self):
		origin = (500, 530)
		ccs = TwoDCartesianCoordSystem(origin, xLength=200, yLength=400, xRange=(0, 15),
										   yRange=(50, 3), titleLst=["xR=(0,15)", "yR=(50,3)"])

		self.assertEqual((500, 1), ccs.computeYAxisLabelXCoordAndDirection(origin, (500, 480)))

	def testComputeYAxisLabelXCoordAndDirection_Y_neg_Y_neg(self):
		origin = (300, 570)
		ccs = TwoDCartesianCoordSystem(origin, xLength=200, yLength=200, xRange=(0, 55),
										   yRange=(-50, -3), titleLst=["xR=(0,55)", "yR=(-50,-3)"])

		self.assertEqual((300, -1), ccs.computeYAxisLabelXCoordAndDirection(origin, (300, 570)))

	def testComputeOriginLabelPositionFirstQuadrant(self):
		print("testComputeOriginLabelPositionFirstQuadrant")
		origin = (80, 400)
		ccs = TwoDCartesianCoordSystem(origin, xLength=200, yLength=300, xRange=(-5, 15),
									   yRange=(50, -3), titleLst=["xR=(-5,15)", "yR=(50,3)"])
									   
		self.assertEqual(1, ccs.computeOriginLabelPosition(origin, (230, 400), (80, 150)))

	def testComputeOriginLabelPositionSecondQuadrant(self):
		print("testComputeOriginLabelPositionSecondQuadrant")
		origin = (250, 1300)
		ccs = TwoDCartesianCoordSystem(origin, xLength=200, yLength=400, xRange=(-55, -5),
									   yRange=(50, 0), xLabel="Loss", titleLst=["xR=(-55,-5)","yR=(50,0)"])
									   
		self.assertEqual(2, ccs.computeOriginLabelPosition(origin, (250, 1300), (250, 900)))

	def testComputeOriginLabelPositionThirdQuadrant(self):
		print("testComputeOriginLabelPositionThirdQuadrant")
		origin = (1000, 1300)
		ccs = TwoDCartesianCoordSystem(origin, xLength=200, yLength=400, xRange=(-55, -5),
									   yRange=(-50, -3), xLabel="Loss", yLabel="Depth", titleLst=["xR=(-55,-5)","yR=(-50,-3)"])
									   
		self.assertEqual(3, ccs.computeOriginLabelPosition(origin, (1000, 1300), (1000, 1300)))

	def testComputeOriginLabelPositionFourthQuadrant(self):
		print("testComputeOriginLabelPositionFourthQuadrant")
		origin = (550, 1300)
		ccs = TwoDCartesianCoordSystem(origin, xLength=200, yLength=400, xRange=(0, 55),
									   yRange=(-50, -3), yLabel="Depth", titleLst=["xR=(0,55)","yR=(-50,-3)"])									   
		self.assertEqual(4, ccs.computeOriginLabelPosition(origin, (750, 1300), (550, 1300)))
		
	def testComputeXTicks_X_neg_X_pos_limits_equal_tick(self):
		xRange = (-4, 6)
		yRange = (7, -7)
		ticks = (2, 3)
		origin = (80, 400)
		ccs = TwoDCartesianCoordSystem(origin, 200, 300, xRange, yRange)
		
		self.assertEqual([-4, -2, 2, 4, 6], ccs.computeXAxisTicks(ticks, xRange))
		
	def testComputeXTicks_X_neg_X_pos_limits_diff_tick(self):
		xRange = (-5, 7)
		yRange = (7, -7)
		ticks = (2, 3)
		origin = (80, 400)
		ccs = TwoDCartesianCoordSystem(origin, 200, 300, xRange, yRange)
		
		self.assertEqual([-4, -2, 2, 4, 6], ccs.computeXAxisTicks(ticks, xRange))
		
	def testComputeXTicks_X_zero_X_pos_limits_equal_tick(self):
		xRange = (0, 6)
		yRange = (7, -7)
		ticks = (2, 3)
		origin = (80, 400)
		ccs = TwoDCartesianCoordSystem(origin, 200, 300, xRange, yRange)
		
		self.assertEqual([2, 4, 6], ccs.computeXAxisTicks(ticks, xRange))
		
	def testComputeXTicks_X_zero_X_pos_limits_diff_tick(self):
		xRange = (0, 7)
		yRange = (7, -7)
		ticks = (2, 3)
		origin = (80, 400)
		ccs = TwoDCartesianCoordSystem(origin, 200, 300, xRange, yRange)
		
		self.assertEqual([2, 4, 6], ccs.computeXAxisTicks(ticks, xRange))		
		
	def testComputeXTicks_X_neg_X_zero_limits_diff_tick(self):
		xRange = (-7, 0)
		yRange = (7, -7)
		ticks = (2, 3)
		origin = (80, 400)
		ccs = TwoDCartesianCoordSystem(origin, 200, 300, xRange, yRange)
		
		self.assertEqual([-6, -4, -2], ccs.computeXAxisTicks(ticks, xRange))		
		
	def testComputeXTicks_X_neg_X_zero_limits_equal_tick(self):
		xRange = (-6, 0)
		yRange = (7, -7)
		ticks = (2, 3)
		origin = (80, 400)
		ccs = TwoDCartesianCoordSystem(origin, 200, 300, xRange, yRange)
		
		self.assertEqual([-6, -4, -2], ccs.computeXAxisTicks(ticks, xRange))		

	def testComputeXTicks_X_neg_X_neg_limits_diff_tick(self):
		xRange = (-9, -3)
		yRange = (7, -7)
		ticks = (2, 3)
		origin = (80, 400)
		ccs = TwoDCartesianCoordSystem(origin, 200, 300, xRange, yRange)
		
		self.assertEqual([-8, -6, -4], ccs.computeXAxisTicks(ticks, xRange))		
		
	def testComputeXTicks_X_neg_X_neg_limits_equal_tick(self):
		xRange = (-9, -4)
		yRange = (7, -7)
		ticks = (2, 3)
		origin = (80, 400)
		ccs = TwoDCartesianCoordSystem(origin, 200, 300, xRange, yRange)
		
		self.assertEqual([-8, -6, -4], ccs.computeXAxisTicks(ticks, xRange))		

	def testComputeXTicks_X_pos_X_pos_limits_diff_tick(self):
		xRange = (3, 9)
		yRange = (7, -7)
		ticks = (2, 3)
		origin = (80, 400)
		ccs = TwoDCartesianCoordSystem(origin, 200, 300, xRange, yRange)
		
		self.assertEqual([4, 6, 8], ccs.computeXAxisTicks(ticks, xRange))		
		
	def testComputeXTicks_X_pos_X_pos_limits_equal_tick(self):
		xRange = (2, 6)
		yRange = (7, -7)
		ticks = (2, 3)
		origin = (80, 400)
		ccs = TwoDCartesianCoordSystem(origin, 200, 300, xRange, yRange)
		
		self.assertEqual([2, 4, 6], ccs.computeXAxisTicks(ticks, xRange))		
				
if __name__ == '__main__':
	unittest.main()
