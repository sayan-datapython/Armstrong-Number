'''
  Calculating Armstrong Number
  By AbdealiB
  https://github.com/AbdealiB/Armstrong-Number
'''

import time

def armstrong(num):
    temp = num
    remainder = 0
    while temp > 0:
        remainder += (temp % 10) ** 3
        temp = temp // 10
    if num == remainder:
        return True
    return False

def main(num=1000):
    armstrong_number = int(input("Enter a number to find if it's an Armstrong Number or not: "))
    result = armstrong(armstrong_number)
    if result:
        print("{} is an Armstrong Number.".format(armstrong_number))
    else:
        print("{} is not an Armstrong Number.".format(armstrong_number))


main()


