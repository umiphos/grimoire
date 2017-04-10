def break_word(string):
    return string.split(' ')

def sort_word(string):
    return sorted(string)

def print_first_word(string):
	"""Only receives objects"""
    word = string.pop(0)
    print word

def print_last_word(string):
	"""Only receives objects"""
    print string.pop(-1)

def sort_sentence(string):
    return break_word(sort_word(string))

def print_first_and_last(string):
    print_first_word(break_word(string))
    print_last_word(break_word(string))
    
    

text="""Sorts the words then prints the first and last one."""
#print break_word(text)
#print sort_word(text)
#print_first_word(break_word(text))
#print_last_word(break_word(text))
print_first_and_last(text)

