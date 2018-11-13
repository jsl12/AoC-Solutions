class keypad:
	'Documentation string'

	def __init__(self,input):
		self.input = input.splitlines()
		self.keys = [[1,2,3],[4,5,6],[7,8,9]]
		self.current_position = [1,1]
		self.path = ""
		self.numbers = []

	def enter_all_keys(self):
		for line in self.input:
			self.enter_key(line)
		

	def enter_key(self,input):
		self.path = ""
		# print("Starting key:".ljust(20),self.current_key())
		# print("Input:".ljust(20),input)
		# print("Current Position".center(20),
		# 	"Starting Key".center(20),
		# 	"Direction".center(20),
		# 	"Ending".center(20))

		for c in input:
			#print(str(self.current_position).center(20),
			#	str(self.current_key()).center(20),
			#	c.center(20),
			#	end='')
			if c == "U":
				self.current_position[0] -= 1
			elif c == "D":
				self.current_position[0] += 1
			elif c == "R":
				self.current_position[1] += 1
			elif c == "L":
				self.current_position[1] -= 1

			for i in range(2):
				if self.current_position[i] == 3:
					self.current_position[i] = 2
				elif self.current_position[i] == -1:
					self.current_position[i] = 0

			
			s = str(self.current_key())

			self.path = self.path + s[0]

			#print(str(self.current_key()).center(20))
		self.numbers.append(self.current_key())
				

	def current_key(self):
		try:
			return self.keys[self.current_position[0]][self.current_position[1]]
		except IndexError:
			return self.current_position

	def number_string(self):
		s = ""
		for i in self.numbers:
			s = s + str(i)
		return s
