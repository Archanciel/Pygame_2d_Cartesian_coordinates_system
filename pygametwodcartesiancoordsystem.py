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
		self.xLabelWidth, xLabelHeight = font.size(xLabel)
		self.xLabelVerticalShift = self.xAxisCoordEnd[1] + xLabelHeight / 3
		self.yLabelText = font.render(self.yLabel, True, self.color)
		yLabelWidth, yLabelHeight = font.size(yLabel)
		self.yLabelHorizontalShift = yLabelWidth / 2
		
		if self.yAxisLabelYCoordAndDirection[1] > 0:
			# Y axis arrow direction is pointing to top
			self.yLabelVerticalShift = self.yAxisCoordStart[1] - yLabelHeight
		else:
			# Y axis arrow direction is pointing to bottom
			self.yLabelVerticalShift = self.yAxisCoordEnd[1]
			
		self.originText = font.render(ORIGIN_LABEL, True, self.color)
		originLabelQuadrant = self.computeOriginLabelPosition(self.origin, self.xAxisCoordEnd, self.yAxisCoordStart)
		
		if originLabelQuadrant == QUADRANT_1:
			self.originLabelX = self.origin[0]
			self.originLabelY = self.origin[1] - FONT_SIZE / ORIGIN_VERTICAL_POS_CORRECTION
		elif originLabelQuadrant == QUADRANT_2:
			self.originLabelX = self.origin[0] - font.size(ORIGIN_LABEL)[0]
			self.originLabelY = self.origin[1] - FONT_SIZE / ORIGIN_VERTICAL_POS_CORRECTION
		elif originLabelQuadrant == QUADRANT_3:
			self.originLabelX = self.origin[0] - font.size(ORIGIN_LABEL)[0]
			self.originLabelY = self.origin[1]
		elif originLabelQuadrant == QUADRANT_4:
			self.originLabelX = self.origin[0]
			self.originLabelY = self.origin[1]

		fontTitle = pg.font.SysFont(None, FONT_TITLE_SIZE, bold=True, italic=False)
		
		if originLabelQuadrant == QUADRANT_1 or originLabelQuadrant == QUADRANT_2:
			self.titleYCoord = self.yLabelVerticalShift - yLabelHeight * 1.5
		else:
			self.titleYCoord = self.yAxisCoordStart[1] - yLabelHeight * 1.8
	
		self.titleSurfaceLst = []
		self.titleHorizontalShiftLst = []
		
		for title in self.titleLst:
			self.titleSurfaceLst.append(fontTitle.render(title, True, self.color))
			self.titleHorizontalShiftLst.append(fontTitle.size(title)[0] / 2)

	def draw(self):
		# drawing I axis
		
		pg.draw.line(self.screen, self.axesColor, self.xAxisCoordStart, self.xAxisCoordEnd, self.thickness)
		pg.draw.polygon(self.screen, self.axesColor, self.xArrowCoord)
		
		if self.xAxisLabelXCoordAndDirection[1] > 0:
			# X axis arrow direction is pointing to right
			self.screen.blit(self.xLabelText,
							 (self.xAxisLabelXCoordAndDirection[0] - self.xLabelWidth, self.xLabelVerticalShift))
		else:
			#  X axis arrow direction is pointing to left
			self.screen.blit(self.xLabelText,
							 (self.xAxisLabelXCoordAndDirection[0], self.xLabelVerticalShift))

		# drawing Y axis
		
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
		i = len(self.titleSurfaceLst)
		titleYCoord = self.titleYCoord
		
		for titleSurface in reversed(self.titleSurfaceLst):
			self.screen.blit(titleSurface,
							(self.yAxisCoordStart[0] - self.titleHorizontalShiftLst[i - 1], titleYCoord))
			i -= 1
			titleYCoord -= FONT_TITLE_SIZE
