#Assignment:1 - 1st problem
import json
employees = {
		'name': 'Ajay',
		"dob" : 120598,
		'height' : '155cm',
		'city' : 'xy',
		'state' : 'abc',

		'name': 'Naren',
		"dob" : 100689,
		'height' : '165cm',
		'city' : 'yz',
		'state' : 'def',

		'name': 'Thara',
		"dob" : 60891,
		'height' : '145cm',
		'city' : 'ab',
		'state' : 'xyz',

		'name': 'Sri',
		"dob" : 251193,
		'height' : '155cm',
		'city' : 'pq',
		'state' : 'rst',

		'name': 'Anika',
		"dob" : 240395,
		'height' : '157cm',
		'city' : 'st',
		'state' : 'mno',
		    }
with open("employe.json", "w") as write_file:
    json.dump(employees,write_file)


with open("employe.json","r") as file:
    data = json.load(file)
obj = []
for i in data:
    obj.append(i)
print(obj)

#Assignment:1 - 2nd problem
import json
dict = {'Tamilnadu':'Chennai', 'Karnataka':'Bengaluru', 'Maharashtra':'Mumbai', 'Rajasthan':'Jaipur', 'Assam':'Dispur', 'Telegana':'Hyderabad', 'Kerala':'Thiruvananthapuram'}
obj = json.dumps(dict, indent = 4)
print(obj)
with open('States.json', 'w') as file:
    file.write(obj)

#Assignment:2
class Dog:
	def __init__(self, name, age, color):
		self.name = name
		self.age = age
		self.color = color
	def Description(self):
		print("Name of Dog:", self.name)
		print("Age of dog:", self.age)
	def get_info(self):
		print("Color of dog:", self.color)
class JackRussell(Dog):
	def __init__(self, name, age, color):
		super().__init__(name, age, color)
	def height(self, val):
		print('Height of dog', val)
	def origin(self, country):
		print("Origin is", country)
class Bulldog(Dog):
	def __init__(self, name, age, color):
		super().__init__(name, age, color)
	def height(self, val):
		print('Height of dog', val)
	def origin(self, country):
		print("Origin is", country)

dog1 = JackRussell("JackRussell Terrier", "3yr", "white")		
dog1.Description()	
dog1.get_info()
dog1.height("10 inch")
dog2 = Bulldog("Bulldog", "2yr", "Brown")
dog2.Description()
dog2.get_info()
dog2.origin("USA")


