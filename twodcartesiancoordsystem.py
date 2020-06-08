import math

BLACK = (0, 0, 0)
ARROW_BASE = 30
ARROW_LENGTH = 40

FONT_SIZE = 35

class TwoDCartesianCoordSystem:
	"""
	This class has no dependancy on Pygame. So, it can be unit tested more
	efficiently. It hosts the Cartesian axes computation logic used by its 
	subclass PygameTwoDCartesianCoordSystem. 
	"""
	def __init__(self, origin, xLength, yLength, xRange, yRange, xLabel='X', yLabel='Y', color=BLACK,
				 thickness=2, titleLst=[]):
		self.origin = origin
		self.xLabel = xLabel
		self.yLabel = yLabel
		self.titleLst = titleLst
		self.color = color
		self.thickness = thickness

		# computing how many pixels correspond to delta x
		self.xStep = math.floor(xLength / (xRange[1] - xRange[0]))
		
		# computing how many pixels correspond to delta y
		self.yStep = math.floor(yLength / (yRange[0] - yRange[1]))

		self.xAxisCoordStart, self.xAxisCoordEnd = self.computeXAxisCoordinates(origin, xLength, xRange)

		self.yAxisCoordStart, self.yAxisCoordEnd = self.computeYAxisCoordinates(origin, yLength, yRange)

		self.axesColor = color
		
		# computing x axis arrow coord
		xArrowPoint1 = (self.xAxisCoordEnd[0] - ARROW_LENGTH, self.xAxisCoordEnd[1] - ARROW_BASE / 2)
		xArrowPoint2 = (self.xAxisCoordEnd[0], self.xAxisCoordEnd[1])
		xArrowPoint3 = (self.xAxisCoordEnd[0] - ARROW_LENGTH, self.xAxisCoordEnd[1] + ARROW_BASE / 2)
		self.xArrowCoord = (xArrowPoint1, xArrowPoint2, xArrowPoint3)
		
		# computing y axis arrow coord
		yArrowPoint1 = (self.yAxisCoordStart[0] - ARROW_BASE / 2, self.yAxisCoordStart[1] + ARROW_LENGTH)
		yArrowPoint2 = (self.yAxisCoordStart[0], self.yAxisCoordStart[1])
		yArrowPoint3 = (self.yAxisCoordStart[0] + ARROW_BASE / 2, self.yAxisCoordStart[1] + ARROW_LENGTH)
		self.yArrowCoord = (yArrowPoint2, yArrowPoint3, yArrowPoint1)

	def computeXAxisCoordinates(self, origin, xAxisLength, xAxisValueRange):
		"""
		This method computes the X axis line start and end coordinates expressed in pixels.
		The returned tuples will be used by the Pygame.draw.line method to draw the X axis.

		:param origin: Cartesian axes system origin coordinate tuple in pixels. Its position
			   in the Pygame Surface.
		:param xAxisLength:
		:param xAxisValueRange: tuple containing the minimal and maximal x value

		:return: xAxisCoordStart and xAxisCoordEnd tuples
		"""
		if xAxisValueRange[0] < 0:
			if xAxisValueRange[1] < 0:
				xAxisCoordStart = (origin[0] - xAxisLength, origin[1])
			else:
				xAxisCoordStart = (origin[0] - abs(xAxisValueRange[0] * self.xStep), origin[1])
		else:
			xAxisCoordStart = (origin[0], origin[1])

		xAxisCoordEnd = (xAxisCoordStart[0] + xAxisLength, xAxisCoordStart[1])

		return xAxisCoordStart, xAxisCoordEnd

	def computeYAxisCoordinates(self, origin, yLength, yRange):
		"""
		This method computes the Y axis line start and end coordinates expressed in pixels.
		The returned tuples will be used by the Pygame.draw.line method to draw the X axis.

		:param origin: Cartesian axes system origin coordinate tuple in pixels. Its position
			   in the Pygame Surface.
		:param xAxisLength:
		:param xAxisValueRange: tuple containing the minimal and maximal y value

		:return: yAxisCoordStart and yAxisCoordEnd tuples
		"""
		if yRange[0] > 0:
			if yRange[1] > 0:
				yAxisCoordStart = (origin[0], origin[1] - yLength)
			else:
				yAxisCoordStart = (origin[0], origin[1] - yRange[0] * self.yStep)
		else:
			yAxisCoordStart = (origin[0], origin[1])

		yAxisCoordEnd = (yAxisCoordStart[0], yAxisCoordStart[1] + yLength)

		return yAxisCoordStart, yAxisCoordEnd
