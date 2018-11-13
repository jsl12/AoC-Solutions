f = open('input.txt')
input = f.read()
input = input.splitlines()
input = [input[i].split() for i,row in enumerate(input)]
print("Number of inputs:".ljust(20),len(input))
	
print("".center(100,"="))

c0 = []
c1 = []
c2 = []
for i,t in enumerate(input):
	c0.append(t[0])
	c1.append(t[1])
	c2.append(t[2])

master_list = c0 + c1 + c2
print(len(master_list))
print(len(master_list) % 3)

for i in range(0,int(len(master_list)/3)):
	input[i] = master_list[i*3:i*3+3]

print(input)

valid = 0
invalid = 0
for i,t in enumerate(input):
	for j,l in enumerate(t):
		input[i][j] = int(l)
	input[i] = sorted(input[i])

	print("Triangle".ljust(10),str(input[i]).ljust(20), end="")

	if input[i][0]+input[i][1] > input[i][2]:
		valid += 1
		print("Triangle valid, total valid: ".ljust(25),str(valid).ljust(15))
	else:
		invalid += 1
		print()

print(valid)