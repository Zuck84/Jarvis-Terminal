import os

print("")

jarvis = input("jarvis/UNIX-for-LINUX> ")

if jarvis == "jarvis":
	print ("")
	os.system("python3 jarvis.py")

elif jarvis == "exit":
	print("")

elif jarvis == "clear":
	os.system("clear")
	os.system("python3 jarvis.py")

elif jarvis == "about":
	print("")
	print("_______________JARVIS [1.0 version for UNIX]_______________")
	print("")
	print("")
	print("Just A Rather Very Intelligent System")
	print("Developed by Charles in October 2019.")
	print("It's the simplest command language made to replace CMD and BASH")
	print("")
	print("")
	print("")
	os.system("python3 jarvis.py")

elif jarvis == "ip":
	os.system("ip addr show")
	print("")
	print("")
	print("")
	os.system("python3 jarvis.py")

elif jarvis == "commands":
	print("")
	print("CLEAR = to clear the screen")
	print("")
	print("EXIT = to stop jarvis")
	print("")
	print("IP = to configure network")
	print("")
	print("COLOR = choose the colors for jarvis")
	print("")
	print("PCNAME = to know your machine's name")
	print("")
	print("ABOUT = to know about the development of jarvis")
	print("")
	print("SAY = to make jarvis say something (press enter before typing what you want him to say")
	print("")
	print("PORT = to see opened ports")
	print("")
	print("SPEAK = to use JAI (Jarvis Artificial Intelligence) to help you.")
	print("")
	print("COMMANDS: to see the list of commands and the main rules to use Jarvis.")
	print("")
	print("DATE: change the date.")
	print("")
	print("PACKETS: send packets to a network host.")
	print("")
	print("BASIC: access to basic (cmd).")
	print("")
	print("LOOP: to test your RAM and your CPU by a loop with the size you want.")
	print("")
	print("INFINITY: to test your RAM and your CPU by an infinity size. (click on the cross to stop)")
	print("")
	print("DIRECTORY: list directory contents.")
	print("")
	print("NEWDIRECTORY: make a new directory (a file), rename it on your desktop")
	print("")
	print("REMOVEDIRECTORY: to remove a directory (please rename the directory/file you want to remove before you enter this command)")
	print("")
	print("TREE: to see your desktop tree.")
	print("")
	print("SHUTDOWN: to shutdown your computer.")
	print("")
	print("REBOOT: to reboot your computer.")
	print("")
	print("RENAME: to rename a file.")
	print("")
	print("OSVERSION: to see your OS version")
	print("")
	print("ROUTINGTABLE: to print routing table.")
	print("")
	print("SERVICE: to start the service. (on Linux or Mac OS)")
	print("")
	print("SHAREDSERVICES: to see shared services.")
	print("")
	print("STOPSERVICE: to stop the service (on Linux or Mac OS)")
	print("")
	print("REPEAT: to make Jarvis repeat something")
	print("")
	print("INTERNETSPEED: to check the speed of your internet (it will first download the packet speedtest-cli before executing the command)")
	print("")
	print("KNOCK KNOCK NEO: to see the matrix effect...")
	print("")
	print("")
	print("")
	print("__________3 RULES TO RESPECT IF YOU WANT IT TO WORK__________")
	print("")
	print("1. PLEASE DO NOT USE CAPITAL LETTERS ONLY USE THE SMALL ONES.")
	print("")
	print("2. TO MAKE JARVIS SAY SOMETHING: TYPE SAY, PRESS ENTER, TYPE WHAT YOU WANT JARVIS TO SAY")
	print("")
	print("3.TO CHOOSE A COLOR YOU CAN WRITE THE NAME OF THE COLOR (PICK ONE FROM THE COLOR LIST OF JARVIS)")
	print("")
	print("")
	print("")
	os.system("python3 jarvis.py")

elif jarvis == "speak":
	os.system("clear")
	print("Hello new user. I am JAI (Jarvis Artificial Intelligence) and I was developed to help you in your tasks on the internet.")
	print("")
	print("But first of all I'd like to learn more about you.(all the informations will be saved until you close Jarvis)")
	print("")

	infoornot = input("Do you want JAI to call you by your name or not ? (yes or no) ==> ")

	if infoornot == "yes":
		firstname = input("First Name: ")
		lastname = input("Last Name: ")

	else:
		firstname = "#anonymous"
		lastname = "user"
	def aboutyouandmore():
		print("")
		print("")
		print("")
		print("Ok new user I will now remember your name is {} {} until you'll close JAI.".format(firstname, lastname))

	aboutyouandmore()

	print("Please enter now your browser name (chrome, chromium, firefox, edge...)")
	browser = input("==> ")

	def JAI():
		print("")
		print("[", firstname, lastname, "]")
		JAICS = input ("to JAI: ")

		if JAICS == "commands":
			print("")
			print("Here are the commands of JAI:")
			print("")
			print("")
			print("EXIT: to exit JAI and go back on the basic Jarvis")
			print("")
			print("GMAIL, HOTMAIL, YAHOOMAIL, INBOX, ICLOUD: to connect to your mail account (type one of these services name to access)")
			print("")
			print("ABOUTME: to see what JAI knows about you")
			print("")
			print("HELLO: say hello to JAI")
			print("")
			print("HEYGOOGLE: to go on google.")
			print("")
			print("WEBSITE: to go directly on a website from JAI")
			JAI()

		elif JAICS == "exit":
			os.system("python3 jarvis.py")

		elif JAICS == "gmail":
			os.system("{} https://mail.google.com".format(browser))
			JAI()

		elif JAICS == "hotmail":
			os.system("{} https://outlook.live.com".format(browser))
			JAI()

		elif JAICS == "yahoomail":
			os.system("{} https://mail.yahoo.com".format(browser))
			JAI()

		elif JAICS == "inbox":
			os.system("{} www.inbox.com".format(browser))
			JAI()

		elif JAICS == "icloud":
			os.system("{} https://www.icloud.com".format(browser))
			JAI()

		elif JAICS == "aboutme":
			def aboutyouandmore():
				print("")
				print("")
				print("")
				print("I know that your name is {} {}.".format(firstname, lastname))	
			aboutyouandmore()
			JAI()

		elif JAICS == "clear":
			os.system("cls")
			JAI()

		elif JAICS == "hello":
			print("")
			print("Hello how can I help you", firstname, "? (enter a command)")
			JAI()

		elif JAICS == "heygoogle":
			os.system("{} www.google.com".format(browser))
			JAI()

		elif JAICS == "website":
			site=input("Which website ? (type NAMEOFTHEWEBSITE.com) ==> ")
			website = str("{} www.{}".format(browser, site))
			os.system(website)
			JAI()

		else:
			print("")
			print("")
			print("")
			print("Wrong Command")
			JAI()

	JAI()

elif jarvis == "say":
	say = input("==> ")
	print("")
	print("Jarvis: ", "¨", say, "¨")
	os.system("python3 jarvis.py")

elif jarvis == "internetspeed":
	os.system("sudo apt install speedtest-cli")
	os.system("speedtest")
	print("")
	os.system("python3 jarvis.py")

elif jarvis == "pcname":
	os.system("hostname")
	os.system("python3 jarvis.py")

elif jarvis == "date":
	os.system("date")
	print("")
	print("")
	print("")
	os.system("python3 jarvis.py")

elif jarvis == "packets":
	os.system("ping")
	print("")
	print("")
	print("")
	os.system("python3 jarvis.py")

elif jarvis == "basic":
	print("")
	print("You can now use the UNIX basic commands")



elif jarvis == "loop":
	loop = 0
	loop2 = input("loop size: ")
	loop2 = int (loop2)
	while loop < loop2:
		print("LOOP")
		loop += 1
	print("")
	print("")
	print("")
	os.system("python3 jarvis.py")

elif jarvis == "infinity":
	loop = 3
	while loop < 5:
		print("testing your CPU and your RAM...")

elif jarvis == "directory":
	os.system("dir")
	print("")
	print("")
	print("")
	os.system("python3 jarvis.py")

elif jarvis == "tree":
	os.system("ls")
	print("")
	print("")
	print("")
	os.system("python3 jarvis.py")

elif jarvis == "shutdown":
	os.system("shutdown")

elif jarvis == "reboot":
	os.system("reboot")

elif jarvis == "osversion":
	os.system("uname -a")
	os.system("python3 jarvis.py")

elif jarvis == "routingtable":
	os.system("route -n")
	os.system("python3 jarvis.py")

elif jarvis == "service":
	servname = input("name of the service: ")
	servname2 = str("service {} start".format(servname))
	os.system(servname2)
	os.system("python3 jarvis.py")

elif jarvis == "stopservice":
	servname = input("name of the service: ")
	servname2 = str("service {} start".format(servname))
	os.system(servname2)
	os.system("python3 jarvis.py")

elif jarvis == "sharedservices":
	os.system("df")
	os.system("python3 jarvis.py")

elif jarvis == "newdirectory":
	print("name of the new directory")
	newdir = input("==> ")
	os.system("mkdir {}".format(newdir))
	os.system("dir")
	os.system("python3 jarvis.py")

elif jarvis == "removedirectory":
	print("name of the directory you want to remove")
	remove = input("==> ")
	os.system("rmdir {}".format(remove))
	os.system("python3 jarvis.py")

elif jarvis == "rename":
	oldname = input ("name of the file: ")
	newname = input ("new name: ")
	rename = str("mv -iv {} {}".format(oldname, newname))
	os.system(rename)
	os.system("python3 jarvis.py")

elif jarvis == "repeat":
	print("What do you want jarvis to repeat?")
	rep = input("==> ")
	finalrep = str("say {}".format(rep))
	os.system(finalrep)
	os.system("python3 jarvis.py")

elif jarvis == "port":
	os.system("netstat -a")
	print("")
	print("")
	print("")
	os.system("python3 jarvis.py")

elif jarvis == "knock knock neo":
	print("launching the matrix... (if it doesn't work please type: sudo apt install cmatrix then type cmatrix")
	os.system("cmatrix")

elif jarvis == "color":
	print("Choose a Color for...")
	background = input("the background: ")
	foreground = input("and the foreground: ")
	color = str("urxvt -bg {} -fg {}".format(background, foreground))
	os.system(color)
	os.system("python3 jarvis.py")

else:
	print("")
	print("")
	print("")
	print("")
	print("Wrong Command")
	os.system("python3 jarvis.py")