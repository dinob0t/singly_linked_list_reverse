""" 
Algorithm to reverse a singly linked list
"""

class Node:
	def __init__(self, init_data):
		self.data = init_data
		self.next = None

	
	def get_data(self):
		return self.data

	def set_data(self, new_data):
		self.data = new_data

	def get_next(self):
		return self.next

	def set_next(self, new_next):
		self.next = new_next

class Singly_Linked_List:
	def __init__(self):
		self.head = None

	def add(self, item):
		temp = Node(item)
		temp.set_next(self.head)
		self.head = temp

	def size(self):
		current = self.head
		count = 0
		while current != None:
			count = count + 1
			current = current.get_next()
		return count

	def print_list(self):
		current = self.head
		while current != None:
			print current.get_data()
			current = current.get_next()

	def reverse(self):
		current = self.head
		count = 0
		while current != None:
			temp = current.get_next()
			if temp == None:
				self.head = current

			if count == 0:
				current.set_next(None)
			else:
				current.set_next(last)	
			last = current
			current = temp
			count = count + 1

sll = Singly_Linked_List()
#Build the list
sll.add(1)
sll.add(2)
sll.add(3)
sll.add(4)
sll.add(5)
sll.add(6)
sll.add(7)
sll.add(8)
sll.add(9)
sll.add(10)

print "List"
sll.print_list()

#Reverse it
sll.reverse()
print "Reversed list"
sll.print_list()




