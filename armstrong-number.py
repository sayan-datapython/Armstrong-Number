'''
  This program takes any integer from 0-1000 as input and prints out if it's an Armstrong number or not.
  By AbdealiB
  https://github.com/AbdealiB/Armstrong-Number
'''

def armstrong(num):
    len_num=len(str(num))
    temp = num
    remainder = 0
    while temp > 0:
        remainder += (temp % 10) ** len_num
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
