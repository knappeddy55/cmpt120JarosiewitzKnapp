# This program will find out the nth number in the fibonacci sequence obtained by the user

def fib(n):
    if (n == 1):
        return 1
    if (n == 2):
        return 1
    return fib(n-1)+ fib(n-2)

def main():
    print("This program computes the nth Fibonacci number where n is a value input by the user")
    
    n = eval(input("Enter a value for n:"))
    print(fib(n))

    
    
main()

   
 
