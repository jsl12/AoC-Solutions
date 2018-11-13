class keypad:
	'Documentation'

	def __init__(self,key_row_strings):
		self.original_keypad = key_row_strings[:]
		self.key_row_sizes = [len(row) for row in key_row_strings]

		self.keys = [row.center(max(self.key_row_sizes)+2," ") for row in key_row_strings]
		self.keys.insert(0,"".center(len(self.keys[0])," "))
		self.keys.append("".center(len(self.keys[0])," "))

		self.loc = []
		if len(self.keys) % 2 == 0:
			x_index = int(len(self.keys)/2)
		else:
			x_index = int((len(self.keys)-1)/2)
		self.loc.append(x_index)

		if len(self.keys[self.loc[0]]) % 2 == 0:
			y_index = int(len(self.keys[self.loc[0]])/2)
		else:
			y_index = int((len(self.keys[self.loc[0]])-1)/2)
		self.loc.append(y_index)

	def get_button_string(self):
		row = self.keys[self.loc[1]]
		self.button = row[self.loc[0]]
		return self.button

	def move(self,direction):
		original_location = self.loc[:]
		original_button = self.get_button_string()
		
		if direction == "U":
			self.loc[1] -= 1
		elif direction == "D":
			self.loc[1] += 1
		elif direction == "R":
			self.loc[0] += 1
		elif direction == "L":
			self.loc[0] -= 1

		new_button = self.get_button_string()
		if new_button == " ":
			# print("Out of bounds",original_location,self.loc)
			self.loc = original_location
			new_button = self.get_button_string()
		print("Moving ",direction," to ",new_button)