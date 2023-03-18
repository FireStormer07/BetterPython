import time, os

print('Thanks for using BetterPython v1.0-Alpha0!')

def reverseString(input_string):
  result = ""
  for char in input_string:
    result = char + result
  return result
  
def type(txt, theTime=0.1):
  for x in str(txt):
    print(x, end='', flush=True)
    time.sleep(theTime)
  print()

class File:
  def __init__(self, file):
    self.file = file
  
  def readLines(self):
    list = open(self.file, "r").readlines()
    for item in list:
      list[list.index(item)] = item.rstrip().rstrip()
    return list
    
  def writeLines(self, list):
    open(self.file, "w").writelines(list)
    open(self.file, 'a').write('\n')

  def appendLines(self, list):
    open(self.file, "a").writelines(list)
    open(self.file, 'a').write('\n')

  def create(self):
    open(self.file, 'w')

  def delete(self):
    os.remove(self.file)
