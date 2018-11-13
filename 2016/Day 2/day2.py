import keypad_class
import keypad_class2

f = open('input.txt')
input = f.read()
#print(input)

k = keypad_class.keypad(input)
k.enter_all_keys()
print("Day1 solution:")
print(k.number_string())
print("------------")


#input = 'ULL\nRRDDD\nLURDL\nUUUUD'
k2 = keypad_class2.keypad2(input)
for row in k2.keys:
	print(row.replace("0"," "))
print(input)
for i,line in enumerate(k2.input):
	k2.enter_key(k2.input[i])
	print("Path",k2.path)
	print("------------------------------")
print("Sequence: ",k2.number_string())