class ListDivideException(Exception):
	pass

def listDivide(numbers = [], divide = 2):
	retVal = 0
	for n in numbers:
		if not(n % divide):
			retVal = retVal + 1
	
	return retVal
	

def testListDivide():
	try:
		print listDivide([1,2,3,4,5])
		print listDivide([2,4,6,8,10])
		print listDivide([30, 54, 63,98, 100], divide=10)
		print listDivide([])
		print listDivide([1,2,3,4,5], 0)
	except:
		#print "Error Dividing List"
		raise ListDivideException('Error dividing list')
		
			
testListDivide()
