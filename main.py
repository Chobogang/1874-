import sys

n = int(input())
stack = []
check = []
count = 1 
result = True

for i in range(n) :
    num = int(sys.stdin.readline())
    while count <= num  :
        stack.append(count)
        count += 1
        check.append("+")

    if stack[-1] == num :
        check.append("-")
        stack.pop()
    else :
        result = False
        break
      
if result == False :
    print("NO")
else :
    for i in check :
        print(i)
        
        
