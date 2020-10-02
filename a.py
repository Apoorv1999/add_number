#taking user input
first_num=int(input("enter First number"))
second_num=int(input("enter second number"))
#sum function
def sum(first_num, second_num):
  return first_num + second_num
#driver code
x=sum(first_num, second_num)
print('sum of two number is {}'.format(x))
