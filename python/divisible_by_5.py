def check_divisibility(num):
  # // Expected output is "TRUE" or "FALSE"
  re=None
  if num%5==0:
    re="TRUE"
  else:
    re="FALSE"
  return re

num = int(input("Enter a number: "))
print(check_divisibility(num))
