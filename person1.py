users={}
def get_name(name):
        name=input("Name ?")
        users["name"]=name

def get_age():
	age=input("Age ?")
	users["age"]=age
 
get_name()
get_age()
users
print(users)
