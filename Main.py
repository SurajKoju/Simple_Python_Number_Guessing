target_num = 10
num = int(input("Enter the number from (0-10):"))

while (num != target_num):
  print("Wrong guess\n ")
  num = int(input("Please Enter the number again:"))
print('Correct guessed. The Number is', target_num)
