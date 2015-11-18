import liberatorlib


in_file = raw_input('Enter path of input ics file:')
out_file = raw_input('Enter path of todo.txt, enter for none:')
lines_to_add = liberatorlib.convert(in_file, out_file)

print "Add the following lines to your todo.txt:"
for line in lines_to_add:
    print line




