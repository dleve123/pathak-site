#!/usr/bin/env python
import cgi
form = cgi.FieldStorage()
name = form.getfirst('n1', '<NOT PROVIDED>')
email = form.getfirst('e1', '<NOT PROVIDED>')
comments = form.getfirst('t1', '<NOT PROVIDED>')

# Avoid script injection escaping the user input
name = cgi.escape(name)
email = cgi.escape(email)
comments = cgi.escape(comments)

f1 = open("random_file.txt",'a')
if name!="&lt;NOT PROVIDED&gt;" or email!="&lt;NOT PROVIDED&gt;" or comments!="&lt;NOT PROVIDED&gt;":
	f1.write("<b>Name: </b>"+name+"\n<b>Email: </b>"+email+"\n<b>Comments: </b>"+comments)
	f1.write("\n--------------------------------------\n")
f1.close()

print """\
Content-Type: text/html\n
<html><body>
<p>The comments were submitted </p>
Click <a href="pathak.html">here</a> to go to Home page.
<br>
Click <a href="contacts.py">here</a> to view your comments.
</body></html>
"""
