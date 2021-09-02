# Enter the list to yourlist u want to make flatten
yourlist = [[1,'a',['cat'],2],[[[3]],'dog'],4,5] 
flat_list = []

def flatten_list(yourlist):
    for element in yourlist:
        if type(element) == list:
            # calling the same function 
            flatten_list(element)
        else:
            flat_list.append(element)

flatten_list(yourlist)
print(flat_list)