# This Program will give approximate values for Pi


import math 
def main():
    n = int(input("Enter the number of terms to approximate Pi:"))

    pi = 0
    sign = 1
    for i in range(1, n * 2 + 1, 2):
        term = 4/i * sign
        pi = pi + term
        sign = sign * -1

    print("The approximate value of Pi is:", pi)
    print("The difference of the approximation from the math module", math.pi - pi)

main()

 
