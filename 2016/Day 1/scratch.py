places_list = [[0,0,0],[8, 0, 1], [8, -4, 2], [4, -4, 3], [4, 4, 0]]
#places_list = [[4, 0, 1], [4, -3, 2], [-1, -3, 3], [-1, -6, 2], [4, -6, 1], [4, -8, 2], [6, -8, 1], [6, -13, 2], [8, -13, 1], [8, -18, 2], [3, -18, 3], [3, -13, 0], [4, -13, 1], [4, -16, 2], [6, -16, 1], [6, -14, 0], [5, -14, 3], [5, -9, 0], [2, -9, 3], [2, -8, 0], [0, -8, 3], [0, -7, 0], [-3, -7, 3], [-3, -12, 2], [-2, -12, 1], [-2, -15, 2], [2, -15, 1], [2, -17, 2], [-2, -17, 3], [-2, -20, 2], [-1, -20, 1], [-1, -24, 2], [3, -24, 1], [3, -27, 2], [8, -27, 1], [8, -24, 0], [196, -24, 1], [196, -28, 2], [197, -28, 1], [197, -76, 2], [202, -76, 1], [202, -80, 2], [131, -80, 3], [131, -77, 0], [129, -77, 3], [129, 111, 0], [126, 111, 3], [126, 113, 0], [123, 113, 3], [123, 116, 0], [118, 116, 3], [118, 115, 2], [117, 115, 3], [117, 113, 2], [121, 113, 1], [121, 115, 0], [126, 115, 1], [126, 118, 0], [129, 118, 1], [129, 115, 2], [125, 115, 3], [125, 112, 2], [129, 112, 1], [129, 107, 2], [133, 107, 1], [133, 111, 0], [136, 111, 1], [136, 107, 2], [140, 107, 1], [140, 106, 2], [143, 106, 1], [143, 107, 0], [142, 107, 3], [142, 111, 0], [143, 111, 1], [143, 115, 0], [144, 115, 1], [144, 116, 0], [141, 116, 3], [141, 118, 0], [139, 118, 3], [139, 120, 0], [138, 120, 3], [138, 125, 0], [141, 125, 1], [141, 121, 2], [146, 121, 1], [146, 119, 2], [141, 119, 3], [141, 114, 2], [140, 114, 3], [140, 116, 0], [139, 116, 3], [139, 113, 2], [136, 113, 3], [136, 114, 0], [139, 114, 1], [139, 118, 0], [143, 118, 1], [143, 122, 0], [142, 122, 3], [142, 123, 0], [140, 123, 3], [140, 121, 2], [144, 121, 1], [144, 120, 2], [147, 120, 1], [147, 116, 2], [149, 116, 1], [149, 113, 2], [150, 113, 1], [150, 118, 0], [154, 118, 1], [154, 113, 2], [152, 113, 3], [152, 118, 0], [153, 118, 1], [153, 113, 2], [152, 113, 3], [152, 116, 0], [149, 116, 3], [149, 114, 2], [151, 114, 1], [151, 119, 0], [153, 119, 1], [153, 121, 0], [158, 121, 1], [158, 116, 2], [160, 116, 1], [160, 113, 2], [165, 113, 1], [165, 108, 2], [167, 108, 1], [167, 104, 2], [165, 104, 3], [165, 103, 2], [162, 103, 3], [162, 98, 2], [159, 98, 3], [159, 100, 0], [164, 100, 1], [164, 101, 0], [167, 101, 1], [167, 103, 0], [169, 103, 1], [169, 102, 2]]
#places_list = [[8, 0, 1], [8, -4, 2], [4, -4, 3]]

# finds the indexes of the places that are in front of the last place in the list
def front_indexes(places_list):
	front_indexes = []
#	print(places_list)
	if len(places_list) > 2:
		last_loc = places_list[-1]
		for i,place in enumerate(places_list):
			if is_front(last_loc,place):
				front_indexes.append(i)
	return front_indexes

# find the indexes of the places that are directly ahead of the last place in the list
def ahead_indexes(places_list):
	ahead_indexes = []
#	print(places_list)
	if len(places_list) > 2:
		last_loc = places_list[-1]
		for i,place in enumerate(places_list):
			if is_ahead(last_loc,place):
				ahead_indexes.append(i)
	try:
		ahead_indexes.remove(len(places_list)-1)
	except:
		pass
	return ahead_indexes

def right_indexes(places_list):
	right_indexes = []
#	print(places_list)
	if len(places_list) > 2:
		last_loc = places_list[-1]
		for i,place in enumerate(places_list):
			if is_right(last_loc,place):
				right_indexes.append(i)
	return right_indexes

def left_indexes(places_list):
	left_indexes = []
	if len(places_list) > 2:
		last_loc = places_list[-1]
		for i,place in enumerate(places_list):
			if is_left(last_loc,place):
				left_indexes.append(i)
	return left_indexes

def is_front(current_location,check_location):
	direction = current_location[2]
	if direction == 0:
		return check_location[1] > current_location[1]
	elif direction == 1:
		return check_location[0] > current_location[0]
	elif direction == 2:
		return check_location[1] < current_location[1]
	elif direction == 3:
		return check_location[0] < current_location[0]
	else:
		return

def is_ahead(current_location,check_location):
	direction = current_location[2]
	if direction == 0:
		return check_location[0] == current_location[0]
	elif direction == 1:
		return check_location[1] == current_location[1]
	elif direction == 2:
		return check_location[0] == current_location[0]
	elif direction == 3:
		return check_location[1] == current_location[1]
	else:
		return

def is_right(current_location,check_location):
	direction = current_location[2]
	if direction == 0:
		return check_location[0] > current_location[0]
	elif direction == 1:
		return check_location[1] < current_location[1]
	elif direction == 2:
		return check_location[0] < current_location[0]
	elif direction == 3:
		return check_location[1] > current_location[1]
	else:
		return

def is_left(current_location,check_location):
	direction = current_location[2]
	if direction == 0:
		return check_location[0] < current_location[0]
	elif direction == 1:
		return check_location[1] > current_location[1]
	elif direction == 2:
		return check_location[0] > current_location[0]
	elif direction == 3:
		return check_location[1] < current_location[1]
	return

def cross_distance(places_list,lr,direction):
	print("Getting cross direction",direction)

	# if facing North or South
	if (direction == 0 or direction == 2):
		cross_point = places_list[lr][1]
	# if faceing East or West
	elif (direction == 1 or direction == 3):
		cross_point = places_list[lr][0]

	print(cross_point)
	return cross_point

def cross_check(places_list):
	print("Cross Check")
	check_places = []
	cross_points = []

	# set last_loc to the last place in the input list and remove it from the list
	check_places.extend(places_list)
	last_loc = check_places.pop(-1)

	# set the direction of the last element in check_places to the direction of the last_loc
	direction = check_places[-1][2] = last_loc[2]

	f = front_indexes(check_places)
	a = ahead_indexes(check_places)
	r = right_indexes(check_places)
	l = left_indexes(check_places)

	#check for right-left lines
	print("------")
	print("Checking for right-left lines")
	for i in f:
		print("Checking index",i,places_list[i])
		# try to draw a line from right to left
		try:
			lr = r.index(i)
			lr = r[lr]
			lf = l.index(i+1)
			lf = l[lf]
			print("R-L Line",places_list[lr],places_list[lf])
			cross_points.append(cross_distance(places_list,lr,last_loc[2]))
		except ValueError:
			#print("Not R-L")
			pass

	#check for left-right lines
	print("------")
	print("Checking for left-right lines")
	for i in f:
		print("Checking index",i,places_list[i])
		#try to draw a line from left to right
		try:
			lf = l.index(i)
			lf = l [lf]
			lr = r.index(i+1)
			lr = r[lr]
			print("L-R Line",places_list[lf],places_list[lr])
			cross_points.append(get_cross_point(places_list,lr,last_loc[2]))
		except ValueError:
			pass
	cross_points.sort()
	print(cross_points)


	if direction == 0:
			closest_cross = cross_points[0]
			if last_loc[1] > closest_cross:
				return [last_loc[0],closest_cross]


	b = True
	if b:
		display_length = 17
		print("Last location".ljust(display_length),last_loc)
		print("Check List:".ljust(display_length),check_places)
		print("-------")
		print("Front Indexes:".ljust(display_length),f)
		print("-------")
		print("Ahead Indexes:".ljust(display_length),a)
		print("Right Indexes:".ljust(display_length),r)
		print("Left Indexes:".ljust(display_length),l)
	return

cross_check(places_list)