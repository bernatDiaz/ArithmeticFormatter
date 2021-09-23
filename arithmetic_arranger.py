class NotNumber(Exception):
  pass

class LongNumber(Exception):
  pass

class WrongOperator(Exception):
  pass

class Problem:
  def __init__(self, operator, n1, n2):
    self.operator = operator
    self.n1 = n1
    self.n2 = n2
    self.calcLen()

  def calcLen(self):
    self.len = max(len(self.n1), len(self.n2)) + 2

  def firstLine(self):
    return " "*(self.len - len(self.n1)) + self.n1
  
  def secondLine(self):
    return self.operator+" "*(self.len - len(self.n2) - 1) + self.n2

  def thirdLine(self):
    return "-"*self.len

  def result(self):
    n1 = int(self.n1)
    n2 = int(self.n2)
    if self.operator == "+":
      r = n1 + n2
    else:
      r = n1 - n2
    rs = str(r)
    return " "*(self.len - len(rs)) + rs


def extract(p):
  l = p.split()
  if not l[0].isnumeric() or not l[2].isnumeric():
    raise NotNumber
  if len(l[0]) > 4 or len(l[2]) > 4:
    raise LongNumber
  if l[1] != "+" and l[1] != "-":
    raise WrongOperator
  return Problem(l[1], l[0], l[2])


def arithmetic_arranger(problems, result = False):
  if(len(problems) > 5):
    return "Error: Too many problems."
  
  problems_format = []
  for p in problems:
    try:
      problems_format.append(extract(p))
    except NotNumber:
      return "Error: Numbers must only contain digits."
    except LongNumber:
      return "Error: Numbers cannot be more than four digits."
    except WrongOperator:
      return "Error: Operator must be '+' or '-'."
  
  r = ""
  for i in range(len(problems_format) - 1):
    r+= problems_format[i].firstLine() + " "*4
  r += problems_format[-1].firstLine() + "\n"

  for i in range(len(problems_format) - 1):
    r+= problems_format[i].secondLine() + " "*4
  r += problems_format[-1].secondLine() + "\n"

  for i in range(len(problems_format) - 1):
    r+= problems_format[i].thirdLine() + " "*4
  r += problems_format[-1].thirdLine()

  if result:
    r += "\n"
    for i in range(len(problems_format) - 1):
      r+= problems_format[i].result() + " "*4
    r += problems_format[-1].result()

  return r