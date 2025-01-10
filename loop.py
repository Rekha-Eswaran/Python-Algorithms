def another_func(n):
    i = 0
    while i < n:
        print(i**2)
        i+=1
        
if __name__ == '__main__':
    n = int(input())
    if 1<=n<=20:
        for i in range(n):
            print(i**2)

        another_func(n)         # using while loop
    else:
        print("Invalid input")

    

    