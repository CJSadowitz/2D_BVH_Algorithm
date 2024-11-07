import pygame
import src.my_screen
import random
from src.bvh import generate_bvh
from src.bvh import BVH_Node

def scene_one(tuple_screen, vertex_count):
	objects = []
	num_vertices = vertex_count
	vertices = generate_rand_vertex_pos(tuple_screen, num_vertices)
	all_aabbs = get_all_aabb(vertices)

	for list in all_aabbs:
		for object in list:
			objects.append(object)

	for vertex in vertices:
		objects.append(src.my_screen.get_circle_object(vertex, (10), "blue"))

	return objects

def traverse_bvh(root, aabb_list=[]):
	if (root.l_child == None and root.r_child == None):
		return aabb_list.append(root.aabb)
	aabb_list.append(root.aabb)
	traverse_bvh(root.l_child, aabb_list)
	traverse_bvh(root.r_child, aabb_list)

def get_all_aabb(vertices):
	# Create the tree
	root = generate_bvh(vertices)
	aabbs = [] # [[],[],[]...[]]
	# Iterate through the tree until there is a list with every aabb
	traverse_bvh(root, aabbs)

	return aabbs

def generate_rand_vertex_pos(tuple_screen, num_vertices):
	vertices = []

	# Change to ensure that no vertex location overlaps
	for i in range(num_vertices):
		vertex = []
		random_x = random.randint(10, tuple_screen[0] - 10)
		random_y = random.randint(10, tuple_screen[1] - 10)
		vertex.append(random_x)
		vertex.append(random_y)
		vertices.append(vertex)

	return vertices
