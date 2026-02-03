
def add(a, b):
   """
   Returns the sum of a and b
   """
   return a + b


def subtract(a, b):
   """
   Returns the result of a minus b
   """
   return a - b


def divide(a, b):
   """
   Returns the result of a divided by b
   Raises an error if b is zero
   """
   if b == 0:
       raise ValueError("Cannot divide by zero")
   return a / b

