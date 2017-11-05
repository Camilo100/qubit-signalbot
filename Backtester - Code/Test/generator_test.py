def createGenerator():
	mylist = range(9)
	for i in mylist:
		yield tuple([i+i, i*i])

mygenerator = createGenerator() # create a generator
for i in range(9):
	print(mygenerator.next()) # mygenerator is an object!

#for i in mygenerator:
