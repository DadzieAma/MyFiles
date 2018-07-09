def get_age(age):
	age = int(input("Enter your age: "))
	print(age)
def get_name(name):
	name = (input("Enter your name: "))
	print(name)	
name = 'ella'
get_age(name)
get_name(name)	

users={}
def get_name(name):
	users[name]=name

def get_age():
	age=input("Age ?")
	users["age"]=age
 
get_name("Mark")
get_age()
users
