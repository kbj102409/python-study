#b까지수를 짝수 홀수로 표현
b = int(input("入力 : "))
for i in range(1,b+1):
    if i%2 == 0:
        print(i,"偶数")
    else :
        print(i,"奇数")

#b까지수를 짝수 홀수갯수 표현
b = int(input("入力 : "))
su = 0
si = 0
for i in range(1,b+1):
    if i%2 == 0:
        su +=i
    else :
        si +=i
print(su,si)

#li.insert()이용
li = [1,2,3,4,5,6,]
print(li)
a = int(input("入れたい資料 : "))
c = int(input("何番目 : "))
li.insert(c,a)
print(li)

#li.appned()이용
a = int(input("入力: "))
li = []
li.append(a)
print(li)

#li.append()이용하여 a까지 수를 리스트로 출력
a = int(input("入力: "))
li = []
for i in range(1,a+1):
    li.append(i)
print(li)

#홀수인경우를 리스트에넣어 출력
a = int(input("入力: "))
li = []
for i in range(1,a+1):
    if i%2==1:
        li.append(i)
print(li)

#a까지 홀수의합과 짝수의합 출력
a = int(input("入力: "))
li1 = []
li2 = []
for i in range(1,a+1):
    if i%2==1:
        li1.append(i)
    else:
        li2.append(i)
print(sum(li1),sum(li2))

#a가 3의배수인지 아닌지 출력
a = int(input("入力: "))
if a%3!=0:
    print("3の倍数x")
else :
    print("3の倍数")

#a까지의 수중 3의배수인지 아닌지 출력
a = int(input("入力: "))
for i in range(1,a+1):
    if i%3!=0:
        print(i,"3の倍数x")
    else :
        print(i,"3の倍数")

#몇일뒤에 당번은 누구인지 출력
d = int(input("何日後 : "))
for i in range(d+1):
    당번 = i%4
    if 당번 == 0:
        print(i,"日後当番 A")
    elif 당번 == 1:
        print(i,"日後当番 B")
    elif 당번 == 2:
        print(i,"日後当番 C")
    elif 당번 == 3:
        print(i,"日後当番 D")

#몇년도까지의 윤달이 언제인지 나오도록 출력
y = int(input("年度入力 : "))
for i in range(1,y+1):
    if i%400==0:
        print(i,"閏月")
    elif i%100==0:
        pass
    elif i%4==0:
        print(i,"閏月")

#4번 입력후 홀수 짝수 판별
for i in range(4):
    a = int(input("入力 : "))
    if a%2 == 0:
        print("偶数")
    else:
        print("奇数")

#4번 입력후 홀수 짝수 판별 버전2
li = []
for i in range(4):
    a = int(input("入力 : "))
    li.append(a)
print(li)
for i in li:
    if i%2==0:
        print(i,"奇数")
    else:
        print(i,"偶数")

#두자리수 두개 입력후 올림 발생하는지를 5번 하기
for i in range(5):
    a = int(input("2桁数 : "))
    b = int(input("２桁数 : "))
    c = a%10+b%10
    if c >= 10:
        print("切上げあり")
    if c < 10 :
        print("切上げなし")

#점수를 5개 입력하고 평균출력한뒤 어떤점수가 평균이하인지 나타내기
li = []
for i in range(5):
    a = int(input("点数 : "))
    li.append(a)
    c=sum(li)/len(li)
print("5科目平均点数",c)
for k in li:
    if c>=k:
        print(k,"平均以下")
    else:
        pass