import sys,commands
files = commands.getoutput('ls')
files = files.split()
for i in files:
	s = commands.getoutput('cat '+i)
	s = s.replace("contacts.html", "contacts.py")
	commands.getoutput("echo "+s+">"+i)
	
