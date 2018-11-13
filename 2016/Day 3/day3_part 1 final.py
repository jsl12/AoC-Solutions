f = open('input.txt')
input = f.read()
input = input.splitlines()
input = [input[i].split() for i,row in enumerate(input)]
print("Number of inputs:".ljust(20),len(input))
valid = 0
for i,t in enumerate(input):
	for j,l in enumerate(t):
		input[i][j] = int(l)
	input[i] = sorted(input[i])

	print("Triangle".ljust(10),str(input[i]).ljust(20), end="")

	if input[i][0]+input[i][1] > input[i][2]:
		valid += 1
		print("Triangle valid, total valid: ".ljust(25),str(valid).ljust(15))
	else:
		print()
print("Total # of valid triangles:",valid)