import os
for x in os.listdir('./data/'):
	print(x)
	if x[-1]=="_":
		os.rename('./data/'+x,'./data/'+x[:-1])
		print("->"+x[:-1])
print("done")