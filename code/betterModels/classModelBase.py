class modelBase:
  def __init__(self, b, i, s):
    self.b = b
    self.i = i
    self.s = s
    
  def printAll(self):
    print("Boolean:'{}', Integer:'{}', String:'{}'".format(self.b, self.i, self.s)
