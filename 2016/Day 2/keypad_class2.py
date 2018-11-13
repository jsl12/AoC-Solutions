class keypad2:
	'Documentation string'

	def __init__(self,input):
		self.input = input.splitlines()
		#self.keys = [[0,0,1,0,0],[0,2,3,4,0],[5,6,7,8,9],[0,"A","B","C",0],[0,0,"D",0,0]]
		#self.keys = ["00100","02340","56789","0BAC0","00D00"]
		self.keys = ["0","1","234","56789","ABC","D","0"]
		self.keys = [x.center(7,"0") for x in self.keys]
		self.current_position = [3,1]
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
			start_key = self.current_key()
			start_position = self.current_position[:]
			# print(str(self.current_position).center(20),
			# 	start_key.center(20),
			# 	c.center(20),
			# 	end='')
			if c == "U":
				self.current_position[0] -= 1
			elif c == "D":
				self.current_position[0] += 1
			elif c == "R":
				self.current_position[1] += 1
			elif c == "L":
				self.current_position[1] -= 1

			if self.current_key() == "0":
				self.current_position = start_position

			s = self.current_key()

			self.path = self.path + s[:]

			# print(str(self.current_key()).center(20))
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
