import math
import src.my_screen

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

	return objects

def generate_bvh(vertices):
	# Create a tree of aabbs
	# Create a node
	root = BVH_Node(vertices)
	root.aabb = create_aabb(vertices)
	# Continue until leaves are 2 or less vertices
	if len(vertices) <= 1:
		# root.aabb = create_aabb(vertices)
		return root

	# Create children with half of the vertex count
	index_half = math.floor(len(vertices) / 2)
	root.l_child = generate_bvh(vertices[:index_half])
	root.r_child = generate_bvh(vertices[index_half:])

	return root

class BVH_Node:
	def __init__(self, vertices):
		self.vertices = vertices
		self.aabb = []
		self.l_child = None
		self.r_child = None
