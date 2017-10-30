from sys import argv
# arguments we are using on this program
script, filename = argv

# we are openning the file with this name
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()


