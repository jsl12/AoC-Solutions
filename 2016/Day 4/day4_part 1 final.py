f = open('input.txt')
input = f.read()
input = input.splitlines()
# input = [input[i].split() for i,row in enumerate(input)]
print("Number of inputs:".ljust(20),len(input))
# print(input)
# print("".center(100,"="))

# input = input[0:5]

import room

rl = room.room_list(input,True)
print(rl.valid_room_count)