class path:
	'Documentation string'

	def __init__(self, input):
		self.input = input
		self.operations = input.split(", ")
		self.current_position = [0,0]
		self.direction = 0
		self.step_number = 0
		self.ending_locations = [[0,0]]
		self.crosses = []

	def dir_letter(self):
		d = "NESW"
		return d[self.direction]

	def display_position(self):
		print(self.current_position)

	def turn(self, direction):
		d = "NESW"
		f = self.direction

		if direction == "R":
			self.direction += 1
		elif direction == "L":
			self.direction -= 1
		
		if self.direction > 3:
			self.direction = 0
		elif self.direction < 0:
			self.direction = 3

		t = self.direction
		#print("Turning from",d[f]," to ",d[t])

	def move(self,distance):
		f = self.current_position

		if self.direction == 0:
			self.current_position[1] += distance
		elif self.direction == 1:
			self.current_position[0] += distance
		elif self.direction == 2:
			self.current_position[1] -= distance
		elif self.direction == 3:
			self.current_position[0] -= distance

		t = self.current_position
		#print("Moving from ",f," to ",t)

	def step(self,cross):
		s = self.operations[self.step_number]
		m = int(s[1::])
		#print("Step ",self.step_number," ",s)

		self.turn(s[0])
		if cross == True:
			c = self.cross_check()
			print
			if c != []:
				#print("Step ",self.step_number+1,self.current_position,", facing ",self.dir_letter(),", moving ",self.operations[self.step_number][1::])
				#print("Crosses at ",c)
				moved = 0
				for i in c:
					move = i - moved
					#print("Moving ",move,"to cross")
					self.move(move)
					moved += move
					self.crosses.append(self.current_position[::])
				#print("Cross coordinates: ",self.crosses)
				m -= moved
				#print("--------")
		self.move(m)

		self.ending_locations.append(self.current_position[::])
		self.step_number += 1

		if self.step_number == len(self.operations):
			self.step_number = len(self.operations)-1

	def complete_path(self,cross):
		print("Starting to traverse entire path, ",len(self.operations),"total operations")
		for op in self.operations:
			self.step(cross)
		print("Done traversing entire path, currently at:")
		print(self.current_position,", facing ",self.dir_letter())
		#print("Crosses at ",self.crosses)

	def cross_check(self):
		#print("Checking for path ahead, facing", self.dir_letter())
		#print("Checking from: ", self.current_position)

		# a list of all the coordinates of points that are ahead of the current position depending on what direction you're facing
		ahead = []

		# distances to possible lines
		d = []

		# distances to lines that are going to be crossed
		c = []

		#  a value to keep track of which index is necessary to pull out of the current position coordinates to calculate the distance away
		i = 0

		if self.dir_letter() == "N":
			ahead = [pos for pos in self.ending_locations if pos[1] > self.current_position[1]]
			left = [pos for pos in ahead if pos[0] <= self.current_position[0]]
			right = [pos for pos in ahead if pos[0] >= self.current_position[0]]
			i = 1
		elif self.dir_letter() == "E":
			ahead = [pos for pos in self.ending_locations if pos[0] > self.current_position[0]]
			left = [pos for pos in ahead if pos[1] >= self.current_position[1]]
			right = [pos for pos in ahead if pos[1] <= self.current_position[1]]
		elif self.dir_letter() == "S":
			ahead = [pos for pos in self.ending_locations if pos[1] < self.current_position[1]]
			left = [pos for pos in ahead if pos[0] >= self.current_position[0]]
			right = [pos for pos in ahead if pos[0] <= self.current_position[0]]
			i = 1
		elif self.dir_letter() == "W":
			ahead = [pos for pos in self.ending_locations if pos[0] < self.current_position[0]]
			left = [pos for pos in ahead if pos[1] <= self.current_position[1]]
			right = [pos for pos in ahead if pos[1] >= self.current_position[1]]

		if ahead != []:		
			for pos in left:
				try:
					l = self.ending_locations.index(pos)
					distance_away = abs(right[right.index(self.ending_locations[l+1])][i]-self.current_position[i])
					d.append(distance_away)
				except ValueError:
					pass
			for pos in right:
				try:
					r = self.ending_locations.index(pos)
					distance_away = abs(left[left.index(self.ending_locations[r+1])][i]-self.current_position[i])
					d.append(distance_away)
				except ValueError:
					pass
			if d != []:
				d.sort()				
				for i,distance in enumerate(d):
					if int(self.operations[self.step_number][1::]) >= d[i]: 
						c.append(d[i])
		return c

	def cross_distances(self):
		cd = []
		for pos in self.crosses:
			cd.append(abs(pos[0])+abs(pos[1]))
		print(cd)
		return cd

		



		
