def collatz(number):
  if number % 2 == 0:
    return int(number / 2)
  else:
    return 3 * number + 1

print("整数を入力してください:")
while True:
  try:
    num = int(input())
    break
  except:
    print("整数を入力してください:")

while True:
  num = collatz(int(num))
  print(num)
  if num == 1:
    break

