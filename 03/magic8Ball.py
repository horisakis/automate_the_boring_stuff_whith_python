import random

def get_answer(answer_number):
  if answer_number == 1:
    return '確かにそうだ'
  if answer_number == 2:
    return '間違いなくそうだ'
  if answer_number == 3:
    return 'はい'
  if answer_number == 4:
    return 'なんとも。もういちどやってみて'
  if answer_number == 5:
    return 'あとでもう一度きいてみて'
  if answer_number == 6:
    return '集中してもういちど聞いてみて'
  if answer_number == 7:
    return '私の答えはノーです'
  if answer_number == 8:
    return '見通しはそれほどよくない'
  if answer_number == 9:
    return 'とても疑わしい'

# r = random.randint(1, 9)
# fortune = get_answer(r)
# print(fortune)

print(get_answer(random.randint(1, 9)))
