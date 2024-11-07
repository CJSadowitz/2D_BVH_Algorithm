import pygame
import numpy as np
import math

def init(size=(800, 600), ):
	pygame.init()
	screen = pygame.display.set_mode(size)
	return screen

def render(surface, objects, mouse_pos):
	for obj in objects:
		match obj[0]:
			case "line":
				pygame.draw.line(surface, obj[1], obj[2], obj[3])
			case "circle":
				pygame.draw.circle(surface, obj[1], obj[2], obj[3])

def get_line_object(orig, end_pos, color):
	object = ["line"]

	object.append(color)
	object.append(orig)
	object.append(end_pos)

	return object

def get_circle_object(orig, radius, color):
	object = ["circle"]

	object.append(color)
	object.append(orig)
	object.append(radius)

	return object

def update_mouse_pos():
	return pygame.mouse.get_pos()
