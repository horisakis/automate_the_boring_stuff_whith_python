def spam():
  global eggs
  eggs = "spam"

def bacon():
  eggs = "bacon"

def hum():
  print(eggs)

eggs = 42
spam()
print(eggs)
