import sqlite3

def show_all():
	#connect to database and create cursor
	conn = sqlite3.connect('ContactManager.db')
	c = conn.cursor()

	#Query database
	c.execute("SELECT rowid, * FROM contacts")
	items = c.fetchall()

	print(" ID" + "\t Full Name " + "\t\t Phone Number" + "\tEmail")
	for item in items:
		outp = " {0} \t {1} {2}\t\t {3} \t{4}   ". format(item[0], item[1], item[2], item[3], item[4])
		print(outp)

	#Apply changes/Close connection
	conn.commit()
	conn.close()

def add_one(first,last,phone,email):
	conn = sqlite3.connect('ContactManager.db')
	c = conn.cursor()
	c.execute("INSERT INTO contacts VALUES (?,?,?,?)", (first, last, phone, email))
	conn.commit()
	conn.close()

def delete_one(id):
	conn = sqlite3.connect('ContactManager.db')
	c = conn.cursor()
	c.execute("DELETE FROM contacts WHERE rowid = (?)", (id,))
	conn.commit()
	conn.close()

def update_one():
	conn = sqlite3.connect('ContactManager.db')
	c = conn.cursor()

	print(" Please Enter the ID number of the record you wish to update")
	idnumber = int(input())
	print(" Choose which row to update (name, last name, phone, email)")
	column = input()
	print(" Type new value")
	value = input()

	#update name
	if column == "name":
		c.execute("""UPDATE contacts 
				 	SET name = (?)
				 	WHERE rowid = (?)
				""", (value, idnumber))
		conn.commit()
		conn.close()

	#update last name
	if column == "last name":
		c.execute("""UPDATE contacts 
				 	SET last_name = (?)
				 	WHERE rowid = (?)
				""", (value, idnumber))
		conn.commit()
		conn.close()

	#update phone number
	if column == "phone":
		c.execute("""UPDATE contacts 
				 	SET phone_number = (?)
				 	WHERE rowid = (?)
				""", (value, idnumber))
		conn.commit()
		conn.close()

	#update email
	if column == "email":
		c.execute("""UPDATE contacts 
				 	SET email = (?)
				 	WHERE rowid = (?)
				""", (value, idnumber))
		conn.commit()
		conn.close()

def search_one_name(name):
	conn = sqlite3.connect('ContactManager.db')
	c = conn.cursor()
	print("")
	c.execute("SELECT rowid, * FROM contacts WHERE name = (?)", (name,))
	items = c.fetchall()

	print(" ID" + "\t Full Name " + "\t\t Phone Number" + "\tEmail")
	for item in items:
		outp = " {0} \t {1} {2}\t\t {3} \t{4}   ". format(item[0], item[1], item[2], item[3], item[4])
		print(outp)

def search_one_last(last):
	conn = sqlite3.connect('ContactManager.db')
	c = conn.cursor()
	print("")
	c.execute("SELECT rowid, * FROM contacts WHERE last_name = (?)", (last,))
	items = c.fetchall()

	print(" ID" + "\t Full Name " + "\t\t Phone Number" + "\tEmail")
	for item in items:
		outp = " {0} \t {1} {2}\t\t {3} \t{4}   ". format(item[0], item[1], item[2], item[3], item[4])
		print(outp)




''' Columns: name, last_name, phone_number, email'''