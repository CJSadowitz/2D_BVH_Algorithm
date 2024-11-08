import math
import src.my_screen
import statistics
import pygame

def generate_aabb(vertices):
	# Find the two positions that will include all vertices
	min_y = math.inf
	min_x = math.inf
	max_y = -math.inf
	max_x = -math.inf
	for vertex in vertices:
		# Find the minimum y value
		min_x = min(min_x, vertex[0])
		min_y = min(min_y, vertex[1])

		max_x = max(max_x, vertex[0])
		max_y = max(max_y, vertex[1])

	return [(min_x - 10, min_y - 10), (max_x + 10, max_y + 10)]

def dist(vert_1, vert_2):
	return math.sqrt(pow(vert_2[1] - vert_1[1], 2) + pow(vert_2[0] - vert_1[0],2))

def create_aabb(vertices):
	# Create 4 Line objects
	objects = []

	aabb_location = generate_aabb(vertices)

	bottom_l = (aabb_location[0][0], aabb_location[0][1])
	bottom_r = (aabb_location[1][0], aabb_location[0][1])

	top_l    = (aabb_location[0][0], aabb_location[1][1])
	top_r    = (aabb_location[1][0], aabb_location[1][1])

	objects.append(src.my_screen.get_line_object(bottom_l, bottom_r, "red"))
	objects.append(src.my_screen.get_line_object(bottom_r, top_r, "red"))
	objects.append(src.my_screen.get_line_object(top_r, top_l, "red"))
	objects.append(src.my_screen.get_line_object(top_l, bottom_l, "red"))

	longest_length = None
	if (dist(bottom_l, bottom_r) > dist(top_l, top_r)):
		longest_length = 'x'
	else:
		longest_length = 'y'

	return longest_length, objects

def generate_bvh(vertices):
	# Create a tree of aabbs
	# Create a node
	root = BVH_Node(vertices)
	root.longest, root.aabb = create_aabb(vertices)
	# Continue until leaves are 2 or less vertices
	if len(vertices) <= 1:
		# This is a leaf
		root.is_leaf = True
		return root

	# Find the median value of either x or y, don't use the index, iterate through the list and create a new list of
	# X and another Y to calculate the median value use this as the middle index
	x_list = []
	y_list = []
	for vertex in vertices:
		x_list.append(vertex[0])
		y_list.append(vertex[1])

	# Sort the indices such the left half are together and the right half are together
	center = None
	if root.longest == 'x':
		center = statistics.median(x_list)
	else:
		center = statistics.median(y_list)
	# Move all vertices that have values less to left half more to right half
	left_half = []
	right_half = []
	for vertex in vertices:
		if root.longest == 'x':
			if vertex[0] <= center:
				left_half.append(vertex)
			else:
				right_half.append(vertex)
		elif root.longest == 'y':
			if vertex[1] <= center:
				left_half.append(vertex)
			else:
				right_half.append(vertex)
	root.l_child = generate_bvh(left_half)
	root.r_child = generate_bvh(right_half)

	return root

def bvh_collision(root, obj_pos, surf):
	# Determine if the object is within the aabb's of the tree. Only when its in a child node, check with vertex

	# Check if object with current root aabb
	y_min = math.inf
	y_max = -math.inf
	x_min = math.inf
	x_max = -math.inf
	for tuple in root.aabb:
		x_min = min(x_min, tuple[2][0])
		x_max = max(x_max, tuple[3][0])
		y_min = min(y_min, tuple[2][1])
		y_max = max(y_max, tuple[3][1])

	if obj_pos[0] <= x_max and obj_pos[0] >= x_min and obj_pos[1] <= y_max and obj_pos[1] >= y_min:
		# Inside the aabb; check if in the child node, draw this one
		aabb_draw(root.aabb, surf)
		if root.is_leaf:
			return True
		return bvh_collision(root.r_child, obj_pos, surf) or bvh_collision(root.l_child, obj_pos, surf)
	return False

def aabb_draw(aabb, surface):
	for list in aabb:
		pygame.draw.line(surface, "yellow", list[2], list[3])

class BVH_Node:
	def __init__(self, vertices):
		self.vertices = vertices
		self.aabb = []
		self.l_child = None
		self.r_child = None
		self.longest = None
		self.is_leaf = False
