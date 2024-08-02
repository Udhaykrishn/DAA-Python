def ton(n,source,temp,dest):
    global count
    if n > 0:
        ton(n-1,source,dest,temp)
        print(f"move disk {n} {source} -> {dest}")
        count + 1
        ton(n-1,temp,source,dest)
source = 'S'
temp = 'T'
dest = 'D'
count = 0
n = int(input("Enter the number of disks: "))
print("Squeence is: ")
ton(n,source,temp,dest)
print("The number of moves: ",count)