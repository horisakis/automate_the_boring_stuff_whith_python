def comma(list):
  str = ""
  last = list[-1]
  work_list = list[0:len(list) - 1]
  for i in work_list:
    str += (i + ", ")
  return str + "and " + last

spam = ['apples', 'bananas', 'tofu', 'cats']
print(comma(spam))
