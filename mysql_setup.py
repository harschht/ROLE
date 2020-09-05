import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	database="your_database",
	user="your_username",
	password="your_password"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE commands (id INT AUTO_INCREMENT PRIMARY KEY, entry VARCHAR(255), importance VARCHAR(255))")
mycursor.execute("CREATE TABLE responses (id INT AUTO_INCREMENT PRIMARY KEY, entry VARCHAR(255), importance VARCHAR(255))")

# Uncomment to print all tables in your_database.
#mycursor.execute("SHOW TABLES")
#for x in mycursor:
#	print (x)

# Uncomment to print all items from table: 'commands'.
#mycursor.execute("SELECT * FROM commands")
#myresult = mycursor.fetchall()
#for x in myresult:
#	print (x)

# Uncomment to print all items from table: 'responses'.
#mycursor.execute("SELECT * FROM responses")
#myresult = mycursor.fetchall()
#for x in myresult:
#	print (x)
