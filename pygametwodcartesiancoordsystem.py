import pygame as pg

from twodcartesiancoordsystem import TwoDCartesianCoordSystem
from constants import *

class PygameTwoDCartesianCoordSystem(TwoDCartesianCoordSystem):
	"""
	This class performs the actual Cartesian axes drawing. It also handles
	the Pygame Font related logic.
	"""
	def __init__(self, screen, origin, xLength, yLength, xRange, yRange, xLabel='X', yLabel='Y', color=BLACK,
				 thickness=3, titleLst=[]):
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
		
		if self.yAxisLabelYCoordAndDirection[1] > 0:
			# Y axis arrow direction is pointing to top
			self.yLabelVerticalShift = self.yAxisCoordStart[1] - 4 * FONT_SIZE / 3
		else:
			# Y axis arrow direction is pointing to bottom
			self.yLabelVerticalShift = self.yAxisCoordEnd[1] + FONT_SIZE / 3
			
		self.originText = font.render(ORIGIN_LABEL, True, self.color)
		originLabelQuadrant = self.computeOriginLabelPosition(self.origin, self.xAxisCoordEnd, self.yAxisCoordStart)
		
		if originLabelQuadrant == QUADRANT_1:
			self.originLabelX = self.origin[0]
			self.originLabelY = self.origin[1] - FONT_SIZE
		elif originLabelQuadrant == QUADRANT_2:
			self.originLabelX = self.origin[0] - font.size(ORIGIN_LABEL)[0]
			self.originLabelY = self.origin[1] - FONT_SIZE
		elif originLabelQuadrant == QUADRANT_3:
			self.originLabelX = self.origin[0] - font.size(ORIGIN_LABEL)[0]
			self.originLabelY = self.origin[1]
		elif originLabelQuadrant == QUADRANT_4:
			self.originLabelX = self.origin[0]
			self.originLabelY = self.origin[1]

		fontTitle = pg.font.SysFont(None, FONT_TITLE_SIZE, bold=True, italic=False)

		self.titleTextLst = []
		self.titleHorizontalShiftLst = []
		self.titleYCoord = self.yAxisCoordStart[1] - 2.7 * FONT_SIZE
		
		for title in self.titleLst:
			self.titleTextLst.append(fontTitle.render(title, True, self.color))
			self.titleHorizontalShiftLst.append(fontTitle.size(title)[0] / 2)

	def draw(self):
		# drawing x axis
		
		pg.draw.line(self.screen, self.axesColor, self.xAxisCoordStart, self.xAxisCoordEnd, self.thickness)
		pg.draw.polygon(self.screen, self.axesColor, self.xArrowCoord)
		
		if self.xAxisLabelXCoordAndDirection[1] > 0:
			# X axis arrow direction is pointing to right
			self.screen.blit(self.xLabelText,
							 (self.xAxisLabelXCoordAndDirection[0] - self.xLabelHorizontalShift, self.xLabelVerticalShift))
		else:
			#  X axis arrow direction is pointing to left
			self.screen.blit(self.xLabelText,
							 (self.xAxisLabelXCoordAndDirection[0], self.xLabelVerticalShift))

		# drawing y axis
		
		pg.draw.line(self.screen, self.axesColor, self.yAxisCoordStart, self.yAxisCoordEnd, self.thickness)
		pg.draw.polygon(self.screen, self.axesColor, self.yArrowCoord)
		#self.screen.blit(self.yLabelText,
					#	(self.yAxisCoordStart[0] - self.yLabelHorizontalShift, self.yLabelVerticalShift))

		self.screen.blit(self.yLabelText,
						(self.yAxisLabelYCoordAndDirection[0] - self.yLabelHorizontalShift, self.yLabelVerticalShift))

		# drawing origin
		self.screen.blit(self.originText, 
						(self.originLabelX, self.originLabelY))
						
		# drawing title
		i = len(self.titleTextLst)
		titleYCoord = self.titleYCoord
		
		for titleText in reversed(self.titleTextLst):
			self.screen.blit(titleText,
							(self.yAxisCoordStart[0] - self.titleHorizontalShiftLst[i - 1], titleYCoord))
			i -= 1
			titleYCoord -= FONT_TITLE_SIZE
