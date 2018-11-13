import keypad3

f = open('input.txt')
input = f.read()
input = input.splitlines()
print(input)

krs = ["1","234","56789","ABC","D"]

k = keypad3.keypad(krs)

print(k.original_keypad)
print(k.keys)

seq = []
for i,row in enumerate(input):
	for x in row:
		k.move(x)
	seq.append(k.button)
	print("Pressing button: ",k.button)
	print("===================================")

print(seq)