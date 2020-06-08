import pygame as pg

from twodcartesiancoordsystem import TwoDCartesianCoordSystem

BLACK = (0, 0, 0)
FONT_SIZE = 35

class PygameTwoDCartesianCoordSystem(TwoDCartesianCoordSystem):
	"""
	This class performs the actual Cartesian axes drawing. It also handles
	the Pygame Font related logic.
	"""
	def __init__(self, screen, origin, xLength, yLength, xRange, yRange, xLabel='X', yLabel='Y', color=BLACK,
				 thickness=2, titleLst=[]):
		super().__init__(origin, xLength, yLength, xRange, yRange, xLabel, yLabel, color,
				 thickness, titleLst)

		self.screen = screen

		font = pg.font.SysFont(None, FONT_SIZE, bold=True, italic=False)

		# Render the text. "True" means anti-aliased text. This creates 
		# an image of the text, but does not put it on the screen
		self.xLabelText = font.render(self.xLabel, True, self.color)
		self.xLabelHorizontalShift = font.size(xLabel)[0]
		self.xLabelVerticalShift = self.xAxisCoordEnd[1] + FONT_SIZE / 3
		self.yLabelText = font.render(self.yLabel, True, self.color)
		self.yLabelHorizontalShift = font.size(yLabel)[0] / 2
		self.yLabelVerticalShift = self.yAxisCoordStart[1] - 4 * FONT_SIZE / 3
		self.originText = font.render("O", True, self.color)
		self.originVerticalShift = self.origin[1] - FONT_SIZE

		self.titleTextLst = []
		self.titleHorizontalShiftLst = []
		self.titleYCoord = self.yAxisCoordStart[1] - 2.7 * FONT_SIZE
		
		for title in self.titleLst:
			self.titleTextLst.append(font.render(title, True, self.color))
			self.titleHorizontalShiftLst.append(font.size(title)[0] / 2)

	def draw(self):
		# drawing x axis
		pg.draw.line(self.screen, self.axesColor, self.xAxisCoordStart, self.xAxisCoordEnd, self.thickness)
		pg.draw.polygon(self.screen, self.axesColor, self.xArrowCoord)
		self.screen.blit(self.xLabelText,
						 (self.xAxisCoordEnd[0] - self.xLabelHorizontalShift, self.xLabelVerticalShift))

		# drawing y axis
		pg.draw.line(self.screen, self.axesColor, self.yAxisCoordStart, self.yAxisCoordEnd, self.thickness)
		pg.draw.polygon(self.screen, self.axesColor, self.yArrowCoord)
		self.screen.blit(self.yLabelText,
						(self.yAxisCoordStart[0] - self.yLabelHorizontalShift, self.yLabelVerticalShift))

		# drawing origin
		self.screen.blit(self.originText, 
						(self.origin[0], self.originVerticalShift))
						
		# drawing title
		i = len(self.titleTextLst)
		titleYCoord = self.titleYCoord
		
		for titleText in reversed(self.titleTextLst):
			self.screen.blit(titleText,
							(self.yAxisCoordStart[0] - self.titleHorizontalShiftLst[i - 1], titleYCoord))
			i -= 1
			titleYCoord -= FONT_SIZE
