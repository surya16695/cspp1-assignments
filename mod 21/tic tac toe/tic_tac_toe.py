''' Write a python program to announce the winner of a tic tac toe game.
  You can try playing the game here. ​https://www.google.com/search?q=tic+tac+toe'''
  #steps to be followed
def row_operation(tic_1):
	count_1 = 0
	a = 0
	for i in range (len(tic_1)):
		count = 0
		for j in range(len(tic_1[0])):
			if tic_1[i][i] == tic_1[i][j]:
				count += 1
			print(count)
		if count == 3:
			count_1 += 1
			a = i
		print(count_1)
	if count_1 == 1:
		return(tic_1[a])
	return None
	len_t = tic[i].count(tic[1][1])
def column_operation(tic_1):
	count_1 = 0
	a = 0
	b = 0
	for i in range (len(tic_1)):
		count = 0
		for j in range(1, len(tic_1[0])):
			if tic_1[j-1][i] == tic_1[j][i]:
				count += 1
			print(count)
		if count == 2:
			count_1 += 1
			a = j-1
			b = i
		print(count_1)
	if count_1 == 1:
		return(tic_1[a][b])
	return None
# def diagonal_operation(tic_1):
# 	count_1 = 0










n = 3
tic_1 = []
tic_2 = []
tic_3 = []
tic_4 = []
for i in range(0, n, 1):
	line = input().split()
	tic_1.append(line)
print (tic_1)
# tic_2.append(row_operation(tic_1))
# print(tic_2)
# if tic_2 != None:
# 	print ("winner is:", tic_2[0][0])
tic_3.append(column_operation(tic_1))
print(tic_3)
if tic_3 != None:
	print ("winner is:", tic_3[0])



