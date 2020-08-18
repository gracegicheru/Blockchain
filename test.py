def add_num(a,b):
    sum=a+b
    return sum
num1=2
num2=3
def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')
answer= convertToBinary(add_num(num1, num2))
# print(answer)
