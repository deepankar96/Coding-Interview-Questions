test = "   "
'''if len(test)==0:
            print(0)
split_arr = test.split(" ")
if split_arr == None:
	print(len(test))
while(len(split_arr[-1])<=0):
	split_arr.pop()
print(len(split_arr[-1]))'''
print(test.split(" ")[-1])