# When specifying a path containing backslashes, you can use a Python raw string
# Doubling up backslash characters will also work, e.g. # default open for reading
# need to have a folder specified to create directory
f = open('C:\\temp\\test.txt', 'w')
f = open('C:/temp/test.txt')
f = open(r'C:\temp\test.txt')
