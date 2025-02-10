#Consider the following code:
x = 'awesome'
def myfunc():
  global x
  x = 'fantastic'
myfunc()
print('Python is ' + x)
#What will be the printed result?
#Python is fantastic