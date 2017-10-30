
# \t stands for a tap
tabby_cat = "\tI'm tabbed in."
# \n stands for a new line(remember C)
persian_cat = "I'm split\non a line."
# \\ let us print a slash as a string \
backslash_cat = "I'm \\ a \\ cat."

# this is a complex string with all the above
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat




while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,

