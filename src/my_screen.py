import pygame
import numpy as np
import math
from src.bvh import bvh_collision

def init(size=(800, 600), ):
	pygame.init()
	screen = pygame.display.set_mode(size)
	return screen

def render(surface, objects, root, mouse_pos):
	vertices = []

	for obj in objects:
		vertices.append(obj[2]) # Reconstruct the vertices list because I am lazy
		match obj[0]:
			case "line":
				pygame.draw.line(surface, obj[1], obj[2], obj[3])
			case "circle":
				pygame.draw.circle(surface, obj[1], obj[2], obj[3])
	# Brute force Collision
	# if brute_force_collision(vertices, mouse_pos):
	#	pygame.draw.circle(surface, "green", (400, 300), 50)

	# BVH Collision
	if bvh_collision(root, mouse_pos, surface):
		pygame.draw.circle(surface, "red", (300, 400), 50)

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

def brute_force_collision(vertices, obj_pos):
	for vert in vertices:
		if obj_pos[0] <= vert[0] + 5 and obj_pos[0] >= vert[0] - 5:
			if obj_pos[1] <= vert[1] + 5 and obj_pos[1] >= vert[1] - 5:
				return True
	return False
