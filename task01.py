def print_multiplication_table(n,m):
    for i in range(1 , n+1):
        for j in range(1 , m+1):
            print(i * j, end="\t")
        print()

n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))

print_multiplication_table(n,m)