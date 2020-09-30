'''
  This program takes any integer from 0-1000 as input and prints out if it's an Armstrong number or not.
  By AbdealiB
  https://github.com/AbdealiB/Armstrong-Number
'''

def armstrong(num,length):
    temp = num
    remainder = 0
    while temp > 0:
        remainder += (temp % 10) ** length
        temp = temp // 10
    if num == remainder:
        return True
    return False

def main(num=1000):
    armstrong_number = int(input("Enter a number to find if it's an Armstrong Number or not: "))
    len_num=len(armstrong_number)
    result = armstrong(armstrong_number,len_num)
    if result:
        print("{} is an Armstrong Number.".format(armstrong_number))
    else:
        print("{} is not an Armstrong Number.".format(armstrong_number))

if__name__=='__main__':
  main()

