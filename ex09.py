#약수출력하는 프로그램
n = int(input("入力 : "))
for i in range(1,n+1):
    if n%i==0:
        print(i)

#두수의 공통약수 출력하는 프로그램
n = int(input("入力 : "))
m = int(input("入力 : "))
if n<m:
    for i in range(1,n+1):
        if n%i==0 and m%i==0:
            print(i)
else :
    for i in range(1,m+1):
        if n%i==0 and m%i==0:
            print(i)

#소수인지 아닌지 판별하는 프로그램
n = int(input("入力 : "))
cnt=0
for i in range(1,n+1):
    if n%i==0:
        cnt+=1
print(cnt)
if cnt ==2:
    print(n,"素数")
else :
    print(n,"素数x")

#완전수인지 아닌지 출력하는 프로그램
li = []
n = int(input("入力 : "))
for i in range(1,n+1):
    if n%i==0:
        li.append(i)
if sum(li)-n == n:
    print(n,"完全数")
else :
    print(n,"完全数x")

# 구구단 세로로 나오게 하는 프로그램 
n = int(input("1~9入力 : "))
for i in range(1,10):
    print(n,"x",i,"=",n*i)

#구구단 가로로 나오게 하는 프로그램
for f in range(2,10):
    print(f,"",end="\t")
print()
for k in range(1,10):
    for i in range(2,10):
        print(i,"x",k,"=",i*k,end="\t")
    print()

#n까지 나열했을때 총 몇자리수가 되는가
n = int(input("入力 : "))
st = ''
for i in range(1,n+1):
    st+=str(i)
print(len(st))


# n입력받고 n이하의 짝수 개수 구하기 
n = int(input("入力 : "))
su = 0
for i in range(1,n+1):
    if i%2 == 0:
        su += 1
print(su)


# 1~n까지 각각의 수 이하의 짝수의 개수를 구하는 프로그램
n = int(input("入力 : "))
for i in range(1,n+1): 
    su=0
    for k in range(1,i+1):
        if i%2 == 0:
            su+=1

# n을 입력받고 n의 약수를 구하는 프로그램
n = int(input("入力 : "))
for i in range(1,n+1):
    if n%i ==0:
        print(i)

# 3~n까지 각각의 약수를 구하는 프로그램
n = int(input("入力 : "))
for i in range(3,n+1):
    li =[]
    for k in range(1,i+1):
        if i%k==0:
            li.append(k)
    print(li)

#입력한수까지 완전수인수는 어떤거인지 출력
n = int(input("入力 : "))
for k in range(1,n+1):
    li = []
    for i in range(1,k+1):
        if k%i==0:
            li.append(i)
    if sum(li)-k == k:
        print(k,"完全数")
  
#입력한 수까지 소수를 전부 출력
n = int(input("入力 : "))
for k in range (3,n+1):
    cnt=0
    for i in range(1,k+1):
        if k%i==0:
            cnt+=1
    if cnt ==2:
        print(k,"素数")

#입력한 수까지 factorial구하기
b = int(input("入力 : "))
for k in range(1,b+1):
    su = 1
    for i in range(k,0,-1):
        su *= i
    print(k,"!","=",su) 