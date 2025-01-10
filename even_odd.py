

def func(n):
    if (n%2 != 0):
        print("Weird")
    else:
        if (2 <= n <= 5):
            print("Not Weird")
        if (6 <= n <= 20):
            print("Weird")
        if (n > 20):
            print("Not Weird")
        
if __name__ == '__main__':
    n = int(input("Enter number: ").strip())
    if (1<= n <= 100):
        func(n)
    else:
        print("Number is out of range")