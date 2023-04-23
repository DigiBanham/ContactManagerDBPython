import database

#add a record
def add_contact():
	print(" ")
	print("Enter the contact information or press E to exit")
	name = input(f"Name: ")
	if name == 'E' or name == 'e':
			exit()
	last = input(f"Last name: ")
	phone = int(input(f"Phone number: "))
	email = input(f"Email: ")

	database.add_one(name, last, phone, email)

#delete one record
def delete_contact():
	print("Enter the ID number of the contact you wish to delete")
	deleteID = int(input())
	database.delete_one(deleteID)

#Update record
def update_contact():
	database.update_one()

#search record
def search_contact():
	print(" You wish to look by name or last name?")
	choice = input()
	if choice == "name":
		print(" Type in the name of the contact you wish to find (case sensitive)")
		name = input()
		database.search_one_name(name)

	if choice == "last name":
		print(" Type in the last name of the contact yo wish to find (case sensitive)")
		last = input()
		database.search_one_last(last)

def welcome():
	print(" ")
	print("*+*+*+*+*+ Contact Manager +*+*+*+*+*")
	print(" ")
	print(" Please choose the corresponding number for the following contact options:  ")
	print(" 1 to Add a new entry")
	print(" 2 to delete")
	print(" 3 to update")
	print(" 4 to show contacts")
	print(" 5 to search for a contact")
	print(" 6 to exit")
	print(" ")
	choice = int(input())

	if choice == 1:
		add_contact()

	if choice == 2:
		delete_contact()
	
	if choice == 3:
		update_contact()

	if choice == 4:
		show_all()

	if choice == 5:
		search_contact()

	if choice == 6:
		exit()


#show records
database.show_all()
welcome()
#update_contact()
#search_contact()
