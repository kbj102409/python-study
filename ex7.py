#tuple자료와 list자료의 유형
a = (1)
b = [1]
print(type(a))
print(type(b))

#list 자료형에서 평균구하기(sum,len의 활용)
li = [1,2,3,4,5,6]
print(sum(li))
print(len(li))
print(sum(li)/len(li))

#수입력후 리스트에 포함시키기(append사용)
li = []
print("既存のlist :[]")
a = int(input("入力 : "))
li.append(a)
print(li)

#리스트에 수 입력후 홀수일경우 출력
a = int(input("入力："))
li = []
if a%2 != 0:
    li.append(a)
print(li)

#세개의 숫자 리스트에 입력후 평균치 구하기
a = int(input("수 입력 : "))
b = int(input("수 입력 : "))
c = int(input("수 입력 : "))
li = []
li.append(a)
li.append(b)
li.append(c)
print(li)
print(sum(li)/len(li))

#for문의 사용법1. 2. 3. 4.
for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i)
for i in [1,"a",3,"@",23.1,4]:
    print(i, end=" ")
for i in range(1,1001):
    print(i)
for i in range(10):
    print(i)

#수를 입력하고 1~수까지 출력
n = int(input("入力 : "))
for i in range(1,n+1):
    print(i)
for i in range(n,0,-1):
    print(i)

#두수 입력하고 두수 사이에 수나열
a = int(input("入力 : "))
b = int(input("入力 : "))
if a<b :
    for i in range(a+1,b):
        print(i)
else :
    for i in range(a-1,b,-1):
        print(i)

#수 입력하고 입력한 1~수까지 합구하기
b = int(input("入力 : "))
su = 0
for i in range(1,b+1):
    su +=i
print("합은",su)

#factorial 
b = int(input("入力 : "))
su = 1
for i in range(b,0,-1):
    su *= i
print(b,"!","=",su)
