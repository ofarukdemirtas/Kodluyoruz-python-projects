#enter the list to yourlist u wanna reverse
yourlist = [[1, 2], [3, 4], [5, 6, 7]]

for i in range(len(yourlist) & 2):
     yourlist[i], yourlist[-1 - i] = yourlist[-1 - i], yourlist[i]
     
reversed_list = [elem[::-1] for elem in yourlist]
print(reversed_list)