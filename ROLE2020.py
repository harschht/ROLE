#!/usr/bin python3

import mysql.connector
import sys
import requests
import visa

# These variables are passed to python from the php page using the shell_exec command.
prompt = str(sys.argv[1]);
impo = str(sys.argv[2]);
name = str(sys.argv[3]);

# For troubleshooting purposes, prints variables passed by sys (from php page).
#print (prompt)
#print ("<br>")
#print (impo)
#print ("<br>")
#print (name)
#print ("<br> <br>")

# Adds single quotes to 'name':
name = "'%s'" % (name,)

# USe this block of code to check that your imports and network host have been successful.
# Type ?IDN into "Enter Command:", you should see "LSG Serial #1234".
# Comment out the lines of code immediately following the comment "Co" when you are ready to switch to Keysight Agilent IO Library Suite.

# Opens Resource Manager, using the simulation backend PyVISA-sim ('@sim').
# Co
rm = visa.ResourceManager('@sim')
# Prints list of available instruments.
# Co
print ("Simulated Instruments: ", rm.list_resources())
# Opens connection to Instrument. Can specify parameters like read_termination and write_termination. May get timeout error if leftout or incorrect for the instrument you are trying to connect to...
# Co
inst = rm.open_resource('ASRL1::INSTR', read_termination='\n')
print ("<br> <br>")

# Connects ROLE2020.py to MySQL database: your_database.
mydb = mysql.connector.connect(
	host="localhost",
	user="your_username",
	password="your_password",
	database="your_database"
)

mycursor = mydb.cursor()

# Inserts 'prompt' and 'impo' into table 'commands' in: your_database.
sql_c = "INSERT INTO commands (entry, importance) VALUES (%s, %s)"
val_c = (prompt, impo)
mycursor.execute(sql_c, val_c)
mydb.commit()

# Queries Device:
# Co
answer = str(inst.query(prompt))
# Uncomment the line below to see the value being passed to answer before it is sent to hold_answer.php.
#print ("answer is: ", answer, "<br><br>")


# For Keysight Agilent IO Library Suite:
# Uncomment the lines following the comment "Uc" once you know your imports and host have been correctly setup and the instrument has been setup and configured according to the Users Guide instructions. See REAMDE.txt.
# GPIB Instruments use SCPI commands, for whatever you want to query, find the corresponding SCPI command and put it into 'prompt'.

# Uc
#VISA_ADDRESS = name
# Uc
#rm = visa.ResourceManager()
# Uc
#inst = rm.open_resource(VISA_ADDRESS)
# Reset the instrument:
# Uc
#rm.write('*rst')
# Write 'command' (prompt) to instrument:
# Uc
#rm.write(prompt)
# Read the result from the output buffer:
# Uc
#answer = rm.read()

# This is an unused variable at this point in the project but could be used to store the GPIB error code responses...
impo_r = "Level ..."

# Inserts device response into MYSQL table 'responses' in: your_database.
sql_r = "INSERT INTO responses (entry, importance) VALUES (%s, %s)"
val_r = (answer, impo_r)
mycursor.execute(sql_r, val_r)
mydb.commit()

# Establishes a key-value pair holding the devices response:
payload = {'answer': answer}
# Uses python requests to send 'payload' to the specified url:
r = requests.post("http://localhost/ROLE/hold_answer.php", data=payload)

# Prints the output of the url specified in requests.post() to 'talk_to_me.php'.
print (r.text, "<br>")
# Uncomment the line below to see the status code of request.post(). If successful you will see '200', if unsuccessful you will see '400'.
#print ("Status: ", r.status_code)

# Need to find out the python commands for the Oscilloscope setup...
# Page 59 of the programmers guide has the instructions for Visual Basic...
