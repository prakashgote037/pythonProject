nums = int(input("Please Enter a Number  "))

for i in range(2,nums):
     if nums % i == 0:
          print("Given Number is not Prime Number")

else:
     print("Given number is Prime Number")
