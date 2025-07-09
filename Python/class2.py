class name:

    def __init__(self,x=None,y=None):

        self.x=x
        self.y=y

    def display(self):

        print('Name: ',self.x)
        print('Age: ',self.y)

obj1=name('Prash', 19)

#obj1.display()

class rec:

    def __init__(self,n):
        self.n=n
        print('Starts: ',n)

    def run(self, n=None):

        if n is None:
            n= self.n
        if n <=0:
            return

        print(n)
        self.run(n-1) 

    def __del__(self):
        print('Deleted')

#obj2=rec(5)
#obj2.run()

#del obj2

class Person(object):

	# Constructor
	def __init__(self, name):
		self.name = name

	# To get name
	def getName(self):
		return self.name

	# To check if this person is an employee
	def isEmployee(self):
		return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

	# Here we return true
	def isEmployee(self):
		return True


# Driver code
emp = Person("Geek1") # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Geek2") # An Object of Employee
print(emp.getName(), emp.isEmployee())

