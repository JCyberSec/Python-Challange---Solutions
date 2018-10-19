# a = [1, 11, 21, 1211]

# 111221,312211,13112221,1113213211


def nextNum(test):
	count=1
	length=""
	i = 0
	for i in range(1,len(test)):
	    if test[i-1]==test[i]:
	       count+=1
	    else :
	        length += str(count) + test[i-1]
	        count=1
	length += (str(count) + test[i])
	# length.apend(a)
	return length

#Main fun
val = "1"
for x in range(35):
	val = nextNum(val)
	print ("Loop: ", x, " length: ", len(val))

