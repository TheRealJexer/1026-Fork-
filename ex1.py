print('Opening a txt file for writing')
f_obj = open('test.txt', mode='w')
f_obj.write("hi")
print('Opening a txt file for reading')
f_obj = open('test.txt', mode='r')

# uncomment below, will result in error
# move .write function above the mode = r function and it will work
# Remember. Python reads form top to bottom!
