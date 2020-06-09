import math

BLACK = (0, 0, 0)
ARROW_BASE = 30
ARROW_LENGTH = 40

class TwoDCartesianCoordSystem:
	"""
	This class has no dependency on Pygame. So, it can be unit tested more
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

		# computing the X axis coordinates
		self.xAxisCoordStart, self.xAxisCoordEnd = self.computeXAxisCoordinates(origin, xLength, xRange)

		# computing the Y axis coordinates
		self.yAxisCoordStart, self.yAxisCoordEnd = self.computeYAxisCoordinates(origin, yLength, yRange)

		self.axesColor = color
		
		# computing X axis arrow coord
		self.xArrowCoord = self.computeXAxisArrowCoordinates(self.origin, self.xAxisCoordStart, self.xAxisCoordEnd)
		
		# computing Y axis arrow coord
		self.yArrowCoord = self.computeYAxisArrowCoordinates(self.origin, self.yAxisCoordStart, self.yAxisCoordEnd)

		# computing X axis label x coord and X axis arrow direction
		self.xAxisLabelXCoordAndDirection = self.computeXAxisLabelXCoordAndDirection(self.origin, self.xAxisCoordStart, self.xAxisCoordEnd)
		
		# computing Y axis label x coord and Y axis arrow direction
		self.yAxisLabelYCoordAndDirection = self.computeYAxisLabelXCoordAndDirection(self.origin, self.yAxisCoordStart)

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

	def computeXAxisArrowCoordinates(self, origin, xAxisCoordStart, xAxisCoordEnd):
		if xAxisCoordEnd[0] > origin[0]:
			xArrowPoint1 = (xAxisCoordEnd[0] - ARROW_LENGTH, xAxisCoordEnd[1] - ARROW_BASE / 2)
			xArrowPoint2 = (xAxisCoordEnd[0], xAxisCoordEnd[1])
			xArrowPoint3 = (xAxisCoordEnd[0] - ARROW_LENGTH, xAxisCoordEnd[1] + ARROW_BASE / 2)
		else:
			xArrowPoint1 = (xAxisCoordStart[0] + ARROW_LENGTH, xAxisCoordStart[1] - ARROW_BASE / 2)
			xArrowPoint2 = (xAxisCoordStart[0], xAxisCoordStart[1])
			xArrowPoint3 = (xAxisCoordStart[0] + ARROW_LENGTH, xAxisCoordStart[1] + ARROW_BASE / 2)

		return (xArrowPoint1, xArrowPoint2, xArrowPoint3)

	def computeYAxisArrowCoordinates(self, origin, yAxisCoordStart, yAxisCoordEnd):
		if yAxisCoordStart[1] < origin[1]:
			yArrowPoint1 = (yAxisCoordStart[0] - ARROW_BASE / 2, yAxisCoordStart[1] + ARROW_LENGTH)
			yArrowPoint2 = (yAxisCoordStart[0], yAxisCoordStart[1])
			yArrowPoint3 = (yAxisCoordStart[0] + ARROW_BASE / 2, yAxisCoordStart[1] + ARROW_LENGTH)
		else:
			yArrowPoint1 = (yAxisCoordEnd[0] - ARROW_BASE / 2, yAxisCoordEnd[1] - ARROW_LENGTH)
			yArrowPoint2 = (yAxisCoordEnd[0], yAxisCoordEnd[1])
			yArrowPoint3 = (yAxisCoordEnd[0] + ARROW_BASE / 2, yAxisCoordEnd[1] - ARROW_LENGTH)

		return (yArrowPoint1, yArrowPoint2, yArrowPoint3)

	def computeXAxisLabelXCoordAndDirection(self, origin, xAxisCoordStart, xAxisCoordEnd):
		# This method returns a tuple whose first element = x coord of X axis label
		# and second element = X axis arrow direction (1 == right, -1 == left).
		if xAxisCoordEnd[0] > origin[0]:
			return (xAxisCoordEnd[0], 1) 
		else:
			return (xAxisCoordStart[0], -1)
			
	def computeYAxisLabelXCoordAndDirection(self, origin, yAxisCoordStart):
		# This method returns a tuple whose first element = x coord of Y axis label
		# and second element = Y axis arrow direction (1 == top, -1 == bottom).
		if yAxisCoordStart[1] < origin[1]:
			return (origin[0], 1)
		else:
			return (origin[0], -1)
