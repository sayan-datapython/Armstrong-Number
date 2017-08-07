'''
  This program prints Armstrong numbers from 0-1000
  By AbdealiB
  https://github.com/AbdealiB/Armstrong-Number
'''

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
    nums = [i for i in range(num) if armstrong(i)]
    print("The Armstrong Numbers are: ",nums)
main()
