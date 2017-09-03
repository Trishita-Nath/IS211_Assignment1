
class Book():
	author = ''
	title = ''
	
	def __init__(self, author, title):
		self.author = author
		self.title = title
		
	def display(self):
		disp_str = self.title + ", written by " + self.author
		print disp_str
		

book1 = Book('Of Mice and Men', 'John Steinbeck')
book2 = Book('To Kill a Mochingbird', 'Harper Lee')

book1.display()
book2.display()
