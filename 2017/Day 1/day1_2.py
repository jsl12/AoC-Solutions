#! python
input = "R4, R3, R5, L3, L5, R2, L2, R5, L2, R5, R5, R5, R1, R3, L2, L2, L1, R5, L3, R1, L2, R1, L3, L5, L1, R3, L4, R2, R4, L3, L1, R4, L4, R3, L5, L3, R188, R4, L1, R48, L5, R4, R71, R3, L2, R188, L3, R2, L3, R3, L5, L1, R1, L2, L4, L2, R5, L3, R3, R3, R4, L3, L4, R5, L4, L4, R3, R4, L4, R1, L3, L1, L1, R4, R1, L4, R1, L1, L3, R2, L2, R2, L1, R5, R3, R4, L5, R2, R5, L5, R1, R2, L1, L3, R3, R1, R3, L4, R4, L4, L1, R1, L2, L2, L4, R1, L3, R4, L2, R3, L1, L5, R4, R5, R2, R5, R1, R5, R1, R3, L3, L2, L2, L5, R2, L2, R5, R5, L2, R3, L5, R5, L2, R4, R2, L1, R3, L5, R3, R2, R5, L1, R3, L2, R2, R1"

num_op = input.count(",")
#print(num_op)
op_set = input.split(", ")
#print(op_set)

x = 0
y = 0
direction = 0
# 1 = North
# 2 = East
# 3 = South
# 4 = West

def step(op,direction):
	# Changes the direction based on the first letter of the operation
	if op[0] == 'R':
		direction += 1
	else:
		direction -= 1

	# Accounts for the rollover in either direction
	if direction == 5:
		direction = 1
	elif direction == 0:
		direction = 4

	return direction
	
for i in op_set:
	direction = step(i,direction)
	print("New direction: ",direction)
	distance = int(i[1::])
	print("Distance: ", distance)


	if direction == 1:
		y += distance
	elif direction == 2:
		x += distance
	elif direction == 3:
		y -= distance
	elif direction == 4:
		x -= distance
	print(x, ", ", y)
	print(abs(x)+abs(y))
	print("====================================")
