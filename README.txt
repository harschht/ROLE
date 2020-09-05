README.txt for R.O.L.E. (Remote Operation of Lab Equipment)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
In the Directory 'ROLE' you will find six program files:
-ROLE2020.php
-talk_to_me.php
-hold_answer.php
-ROLE2020.py
-mysql_setup.py
-iframe_test.html

The user starts out on ROLE2020.php, this was originally accomplished using apache and run on 'localhost' or equivalently '127.1.0.0'. You can use IIS if using Windows but make sure to give all files (including your python interpreter) full permissions. Also when using Windows and IIS look up how to alter PHP accordingly, there are some alternate steps to take when configuring the php.ini file. If using Linux just install PHP and Apache from terminal, you can find detailed instructions online.

ROLE2020.php is an HTML document that uses php functions to send three user input strings to talk_to_me.php. The first string is the 'command', the second is the 'importance' and the third is the 'name' (name of the instrument you are trying to connect to). These strings are passed through the shell_exec() function to the python file ROLE2020.py. This python script takes the strings and puts them into respective variables. The 'command' and 'importance' variables are then placed into a MySQL table in the specified database. Enter your host (if using apache locally use 'localhost'), username, password, and database name into the .py file where it says my_username, my_password etc... Make sure the MySQL user has full access to the database specified. The .py file then uses PyVISA to open a Resource Manager using the input 'name' as the instrument to connect to. The variable prompt ('command') is then fed to the Resource Manager and a query is sent to the instrument specified by 'name'. The response from the device is then input into a MySQL table and sent back to ROLE2020.php. This response can be displayed on talk_to_me.php using r.text(), a function of python requests that displays the resulting output of the url that was posted to using requests.post(). The response you see along with the button to return to ROLE2020.php is actually the resluting output after the response is posted to hold_answer.php, this holding page is used so that talk_to_me.php could be used for debugging and to display code output while R.O.L.E. is still being developed. If talk_to_me.php was used in place of hold_answer.php then the page would be reloaded a second time at the bottom of itself and you would see two talk_to_me.php pages stacked ontop of one another.

To setup the MySQL tables run the python file mysql_setup.py using sudo permissions. This will create two MySQL tables in the database specified where you see your_database. Just like with ROLE2020.py enter the hostname, username and password, making sure that the user specified has full permissions for that MySQL database. The file will create the tables: 'commands' and 'responses' and these tables will be used by ROLE2020.py to save the user input commands and device responses.
You can uncomment the corresponding blocks of code to display the contents of either table, the tables have been created with a primary key for indexing purposes and can be treated by python as an array.

To make sure you have setup imports correctly and to ensure that your server is up and running use the PyVISA-sim code block and send the command "?IDN" through the "Enter Command:" text input prompt. You should endup on talk_to_me.php, click the button that sends you back to ROLE2020.php, you should see "Query Response: LSG Serial #1234". If you see anything other than the aforementioned string use the various commented blocks of code in ROLE2020.py, look through the comments and uncomment the lines that specify they are there for debugging purposes or to print certain variables of interest. Also be certain to use mysql_setup.py to print the contents of the tables 'commands' and 'responses' to make certain that the variables were passed to your MySQL database. Make sure the directory ROLE (or all six files within it) has the filepath:
	/var/www/html/ROLE
If using Apache and localhost. (on Ubuntu Linux, if using Windows make sure all the files are in the same folder used by IIS, 'wwwroot')

Next, comment out the block of code you just used that is runing the PYVISA-sim backend and uncomment the block of code labeled: "Keysight Agilient IO Library Suite". You will use Keysights IO library to connect to the oscilloscope over GPIB. The lines to uncomment are marked with "Uc" while the lines to comment are marked with "Co".

PyVISA uses a backend and an IO library to communicate with GPIB instruments. Since the target instrument is a Keysight: Agilent InfiniiVision 2000 X-Series Oscilloscope, the Keysight Agilent IO Library Suite is the most viable option, there is a version for Windows and Linux that you can download here:
	https://www.keysight.com/en/pd-1985909/io-libraries-suite?pm=DL&nid=-33330.977662&cc=US&lc=eng

Click on the "Trials and Licenses" tab, then click "Details & Downloads". Select Windows or Linux based on your OS. Windows has a nice Installer GUI that will lead you through the steps necessary to setup the IO, while on Linux it is a bit more involved of an installation. (Note that ROLE2020.py was written on Ubuntu and may have to be altered slightly to work on Windows, or you can use a Virtual enviroment such as VirtualBox to simultaneously run a Linux enviroment on your Windows PC).

There are detailed installation instructions in the README.txt file associated with the package that can be found under "Supporting Documentation" located to the bottom left from the red "Download" button.

(Paste this link into your browser for the Linux version:)
	https://www.keysight.com/upload/cmc_upload/All/ReadMe_2020.htm?&cc=US&lc=eng

If using Ubuntu make sure you are running on one of the supported kernels, you can find a list of the supported kernels in the README.txt file specified above.

To find out what kernel you are running run the following code in terminal:
	uname -a

To run Linux on a kernel on Ubuntu other than the one you are currently running check out this tutorial:
	https://serverascode.com/2019/05/17/install-and-boot-older-kernel-ubuntu.html

Keysight also has detailed setup instructions for the PC that will be connected to the instrument that can be found in chapter 21: "Web Interface" on page 265 of the Oscilloscope User guide:
	http://web.sonoma.edu/esee/manuals/mso2002a_ug.pdf

To see a list of all the commands and ways to connect to the taget device, check out the Oscilloscope Programming Guide:
(Page 47: Setting up)
(Page 137: Common Commands)
	https://www.keysight.com/upload/cmc_upload/All/2000_series_prog_guide.pdf

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Keysight InfiniiVision 2000 X-Series Oscilloscope webpage:
	https://www.keysight.com/en/pcx-x205206/infiniivision-2000-x-series-oscilloscopes?nid=-32542.0&cc=US&lc=eng

I/O Libraries Example Programs:
	https://www.keysight.com/main/editorial.jspx?cc=US&lc=eng&ckey=2798637&nid=-35489.384515&id=2798637

(Note: Keysight was the electronics measurement division of Agilent before being spun-off. Similarly, Agilent was the electronics measurement division of HP before being spun-off.)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Next steps for R.O.L.E.

-Make php page to put in iframe on ROLE2020.php when button Display! is pressed, this page should be able to display the devices response when an SCPI command  to display the instrument screen is used. Check out page 271 of the programmers guide. (currently 'iframe_test.html', [ROLE2020.php line 13])
-Replace "?IDN" in Buttons one-three with SCPI commands.
-Style with CSS (make it look similar to SSU EE resources page?)
-Add chat box? (between Student user PC and SSU EE lab PC?)
-Add "head" tags to php pages ROLE2020.php and talk_to_me.php
-Find use for impo_r, the devices response 'importance'. (current value is "Level ...")
-Translate the Oscillocsope setup commands from page 59 of the programmers guide from Visual Basic to Python and add to ROLE2020.py.
