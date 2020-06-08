import pygame as pg
import math

BLACK = (0, 0, 0)
ARROW_BASE = 30
ARROW_LENGTH = 40

FONT_SIZE = 35

class Pygame2dCartesianCoordSystem():
	def __init__(self, screen, origin, xLength, yLength, xRange, yRange, xLabel='X', yLabel='Y', color=BLACK,
				 thickness=2):
		self.screen = screen
		self.origin = origin
		self.xLabel = xLabel
		self.yLabel = yLabel
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
		
		font = pg.font.SysFont(None, FONT_SIZE, bold=True, italic=False)
 
		# Render the text. "True" means anti-aliased text.
		# Black is the color. This creates an image of the
		# letters, but does not put it on the screen
		self.xLabelText = font.render(self.xLabel, True, self.color)
		self.xLabelHorizontalShift = font.size(xLabel)[0]
		self.yLabelText = font.render(self.yLabel, True, self.color)
		self.yLabelHorizontalShift = font.size(yLabel)[0] / 2
		self.originText = font.render("O", True, self.color)

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

	def draw(self):
		# drawing x axis
		pg.draw.line(self.screen, self.axesColor, self.xAxisCoordStart, self.xAxisCoordEnd, self.thickness)
		pg.draw.polygon(self.screen, self.axesColor, self.xArrowCoord)
		self.screen.blit(self.xLabelText, (self.xAxisCoordEnd[0] - self.xLabelHorizontalShift, self.xAxisCoordEnd[1] + FONT_SIZE / 3))
		
		# drawing y axis
		pg.draw.line(self.screen, self.axesColor, self.yAxisCoordStart, self.yAxisCoordEnd, self.thickness)
		pg.draw.polygon(self.screen, self.axesColor, self.yArrowCoord)
		self.screen.blit(self.yLabelText, (self.yAxisCoordStart[0] - self.yLabelHorizontalShift, self.yAxisCoordStart[1] - 4 * FONT_SIZE / 3))

		self.screen.blit(self.originText, (self.origin[0], self.origin[1] - FONT_SIZE))
