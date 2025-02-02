"""
Define a class which has at least two methods:
`getString`: to get a string from console input
`printString`: to print the string in upper case.

"""

class Statement:
  def __init__(self):
    self.statement = ""
  def getString(self):
    self.statement = input("Enter your statement: ")
  def printString(self):
    print(self.statement.upper())





s = Statement()
s.getString()
s.printString()

