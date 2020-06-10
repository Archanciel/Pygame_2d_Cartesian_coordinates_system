import pygame as pg
import math
import os
import time
from pygametwodcartesiancoordsystem import PygameTwoDCartesianCoordSystem
from constants import *

def handleDoubleClick():
	global timerDC
	global running
	
	if timerDC == 0:
		timerDC = 0.01
		# Click again before 0.1 seconds to double click.
	elif timerDC < 0.1:
		# Double click happened
		running = False
		
def updateTimerForDoubleClick():
	# Increase timerDC after mouse was pressed the first time.
	global timerDC
	global dt

	if timerDC != 0:
		timerDC += dt

	# Reset after 0.5 seconds.
	if timerDC >= 0.1:
		timerDC = 0

	# dt == time in seconds since last tick.
	# / 1000 to convert milliseconds to 10th of seconds.
	dt = clock.tick(FPS) / 10000

background_color = WHITE
pg.init()

if os.name == 'posix':
	(width, height) = (1600, 2560)
	screen = pg.display.set_mode((width, height), pg.FULLSCREEN)
else:
	(width, height) = (1240, 780)
	os.environ['SDL_VIDEO_WINDOW_POS'] = '5,30'
	screen = pg.display.set_mode((width, height))

pg.display.set_caption('Cartesian axis')
(w, h) = screen.get_size()

running = True
clock = pg.time.Clock()
timerDC = 0
dt = 0

screen.fill(background_color)
cartesianAxesLst = []

if os.name == 'posix':
	cartesianAxesLst.append(
		PygameTwoDCartesianCoordSystem(screen=screen, origin=(110, 600), xLength=200, yLength=400, xRange=(-5, 15),
									   yRange=(50, -3), titleLst=["xR=(-5,15)","yR=(50,-3)"]))
	cartesianAxesLst.append(
		PygameTwoDCartesianCoordSystem(screen=screen, origin=(400, 600), xLength=200, yLength=400, xRange=(-5, 15),
									   yRange=(30, -40), xLabel='Time', yLabel='Speed', titleLst=["xR=(-5,15)","yR=(30,-40)"]))
	cartesianAxesLst.append(
		PygameTwoDCartesianCoordSystem(screen=screen, origin=(700, 600), xLength=200, yLength=400, xRange=(0, 15),
									   yRange=(50, 3), titleLst=["xR=(0,15)","yR=(50,3)"]))
	cartesianAxesLst.append(
		PygameTwoDCartesianCoordSystem(screen=screen, origin=(1000, 600), xLength=200, yLength=400, xRange=(25, 55),
									   yRange=(50, 3), titleLst=["xR=(25,55)","yR=(50,3)"]))
	cartesianAxesLst.append(
		PygameTwoDCartesianCoordSystem(screen=screen, origin=(250, 1300), xLength=200, yLength=400, xRange=(-55, -5),
									   yRange=(50, 0), xLabel="Loss", titleLst=["xR=(-55,-5)","yR=(50,0)"]))
	cartesianAxesLst.append(
		PygameTwoDCartesianCoordSystem(screen=screen, origin=(550, 1300), xLength=200, yLength=400, xRange=(0, 55),
									   yRange=(-50, -3), yLabel="Depth", titleLst=["xR=(0,55)","yR=(-50,-3)"]))
	cartesianAxesLst.append(
		PygameTwoDCartesianCoordSystem(screen=screen, origin=(1000, 1300), xLength=200, yLength=400, xRange=(-55, -5),
									   yRange=(-50, -3), xLabel="Loss", yLabel="Depth", titleLst=["xR=(-55,-5)","yR=(-50,-3)"]))
#origin, xLength, yLength, xRange, yRange, xLabel='X', yLabel='Y', color=BLACK, thickness=2, leftMargin=0, topMargin=0):
else:
	cartesianAxesLst.append(
		PygameTwoDCartesianCoordSystem(screen=screen, origin=(80, 400), xLength=200, yLength=300, xRange=(-5, 15),
									   yRange=(50, -3), titleLst=["xR=(-5,15)","yR=(50,-3)"]))
	cartesianAxesLst.append(
		PygameTwoDCartesianCoordSystem(screen=screen, origin=(300, 255), xLength=200, yLength=300, xRange=(-5, 15),
									   yRange=(30, -40), xLabel='Time', yLabel='Speed', titleLst=["xR=(-5,15)","yR=(30,-40)"]))
	cartesianAxesLst.append(
		PygameTwoDCartesianCoordSystem(screen=screen, origin=(500, 530), xLength=200, yLength=400, xRange=(0, 15),
									   yRange=(50, 3), titleLst=["xR=(0,15)","yR=(50,3)"]))
	cartesianAxesLst.append(
		PygameTwoDCartesianCoordSystem(screen=screen, origin=(720, 530), xLength=200, yLength=400, xRange=(25, 55),
									   yRange=(50, 3), titleLst=["xR=(25,55)","yR=(50,3)"]))
	cartesianAxesLst.append(
		PygameTwoDCartesianCoordSystem(screen=screen, origin=(1145, 550), xLength=200, yLength=400, xRange=(-55, -5),
									   yRange=(50, 0), xLabel="Loss", titleLst=["xR=(-55,-5)","yR=(50,0)"]))
	cartesianAxesLst.append(
		PygameTwoDCartesianCoordSystem(screen=screen, origin=(300, 555), xLength=200, yLength=200, xRange=(0, 55),
									   yRange=(-50, -3), yLabel="Depth", titleLst=["xR=(0,55)","yR=(-50,-3)"]))
	cartesianAxesLst.append(
		PygameTwoDCartesianCoordSystem(screen=screen, origin=(720, 555), xLength=200, yLength=400, xRange=(-55, -5),
									   yRange=(-50, -3), xLabel="Loss", yLabel="Depth", titleLst=["xR=(-55,-5)","yR=(-50,-3)"]))

while running:
	clock.tick(FPS)
		
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False
		elif event.type == pg.MOUSEBUTTONDOWN: #on Android, tap the sreen to quit
			handleDoubleClick()

	screen.fill(background_color)
	
	for cartesianAxes in cartesianAxesLst:
		cartesianAxes.draw()
	
	pg.display.flip()

		
pg.quit()