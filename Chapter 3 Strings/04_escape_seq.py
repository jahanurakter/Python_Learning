# An escape sequence represents a special character in a string using a backslash (\).

a = "Maya is a good girl\nbut not a bad girl"
print(a)
b = "Maya is a \"kid\""         #
print(b)
c = "He is a\t'bad'\tboy"
print(c)
print(c.replace("bad","good"))          
d = " She is a brave girl with sharp mind\rMaya "  
print(d)                # \r means it replace the first text with last

#Important string functions/methods
# \n	New line	    "Hello\nWorld"	Hello
# World
# \t	Tab space	    "Hello\tWorld"	Hello World
# \\	Backslash	    "C:\\Users"	C:\Users
# \'	Single quote	'It\'s good'	It's good
# \"	Double quote	"He said \"Hi\""	He said "Hi"