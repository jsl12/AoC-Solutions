class room:
	def char_range(self,input):
		"""Generates the characters from `c1` to `c2`, inclusive."""
		for c in range(ord(input[0]), ord(input[1])+1):
			yield chr(c)

	def decrypt(self):
		self.decrypted = ""
		char_range = "az"
		range_start = ord(char_range[0])
		range_end = ord(char_range[1])
		number_range = range_end - range_start + 1

		for i,char in enumerate(self.words):
			original_number = ord(char)
			rotation = self.sectorID % number_range

			distance_to_end = range_end - original_number
			if rotation > distance_to_end:
				rotation -= distance_to_end

			new_number = original_number + rotation
			new_char = chr(new_number)

			self.decrypted += new_char

			print(self.sectorID,number_range,char,original_number,rotation,new_char)

	def __init__(self,input):

		self.input = input.strip()

		self.input_checksum = input[-6:-1]

		self.words = input[:-7]
		self.words = self.words.split("-")
		self.sectorID = int(self.words.pop())
		self.words = input[:-7]
		# self.words = self.words.upper()
		
		self.letter_counts = []
		self.chars = self.char_range('az')
		for c in self.chars:
			occurences = self.words.count(c)
			self.letter_counts.append((occurences,-ord(c),c))
			# negates the result of ord() so that it's effectively sorted in ascending order
		self.letter_counts.sort(reverse=True)
		self.checksum=""
		for i in range(0,5):
			self.checksum += chr(-self.letter_counts[i][1])

		self.valid = self.checksum == self.input_checksum

		self.decrypt()

	def print_letter_counts(self):
		print(self.letter_counts[:5])

class room_list:
	def __init__(self,input,output=False):
		self.room_list =[]
		self.valid_room_count = 0
		self.valid_rooms = []
		self.sector_sum = 0

		self.report_width = 20

		for line in input:
			r = room(line)
			self.room_list.append(r)

			if r.valid == True:
				self.valid_room_count += 1
				self.sector_sum += r.sectorID

				if output == True:
					print(str(r.words).ljust(70),
						r.checksum.ljust(6),
						str(self.valid_room_count).ljust(5),
						str(self.sector_sum).ljust(10),
						str(r.decrypted))