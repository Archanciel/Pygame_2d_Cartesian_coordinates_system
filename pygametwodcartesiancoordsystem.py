import pygame as pg

from twodcartesiancoordsystem import TwoDCartesianCoordSystem

BLACK = (0, 0, 0)
FONT_SIZE = 35

class PygameTwoDCartesianCoordSystem(TwoDCartesianCoordSystem):
	def __init__(self, screen, origin, xLength, yLength, xRange, yRange, xLabel='X', yLabel='Y', color=BLACK,
				 thickness=2, title=''):
		super().__init__(origin, xLength, yLength, xRange, yRange, xLabel='X', yLabel='Y', color=BLACK,
				 thickness=2, title='')

		self.screen = screen

		font = pg.font.SysFont(None, FONT_SIZE, bold=True, italic=False)

		# Render the text. "True" means anti-aliased text.
		# Black is the color. This creates an image of the
		# letters, but does not put it on the screen
		self.xLabelText = font.render(self.xLabel, True, self.color)
		self.xLabelHorizontalShift = font.size(xLabel)[0]
		self.yLabelText = font.render(self.yLabel, True, self.color)
		self.yLabelHorizontalShift = font.size(yLabel)[0] / 2
		self.originText = font.render("O", True, self.color)

	def draw(self):
		# drawing x axis
		pg.draw.line(self.screen, self.axesColor, self.xAxisCoordStart, self.xAxisCoordEnd, self.thickness)
		pg.draw.polygon(self.screen, self.axesColor, self.xArrowCoord)
		self.screen.blit(self.xLabelText,
						 (self.xAxisCoordEnd[0] - self.xLabelHorizontalShift, self.xAxisCoordEnd[1] + FONT_SIZE / 3))

		# drawing y axis
		pg.draw.line(self.screen, self.axesColor, self.yAxisCoordStart, self.yAxisCoordEnd, self.thickness)
		pg.draw.polygon(self.screen, self.axesColor, self.yArrowCoord)
		self.screen.blit(self.yLabelText, (
		self.yAxisCoordStart[0] - self.yLabelHorizontalShift, self.yAxisCoordStart[1] - 4 * FONT_SIZE / 3))

		self.screen.blit(self.originText, (self.origin[0], self.origin[1] - FONT_SIZE))
