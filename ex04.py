#1자리수 2자리수 제어 출력
a = int(input("数字入力 : "))
if 0<=a<10:
    print("1桁数入力!")
if 10<=a<100:
    print("2桁数入力")

#양수 음수 0 구분해서 출력
a = int(input("数字入力 : "))
if a<0:
    print("負数")
if a==0:
    print("0")
if a>0:
    print("陽数")

#두수 크기 비교
a= int(input("a値入力 : "))
b = int(input("b値入力 : "))
if a>b:
    print("aの方が大きい!")
if b>a:
    print("bの方が大きい!")

#홀수 짝수 구분
a = int(input("数字入力 : "))
if a%2==1:
    print("奇数")
if a%2==0:
    print("偶数")

#평균점수로 합격 불합격 구분
국 = float(input("日本語点数 : "))
수 = float(input("数学点数 : "))
평균 = (국+수)/2
if 평균>=80.0:
    print("合格")
if 평균<80.0: 
    print("不合格")

#올림 발생 유무 프로그램
a = int(input("数字入力 : "))
b = int(input("数字入力　: "))
c = a%10+b%10
if c >= 10:
    print("切上げ発生")
if c < 10 :
    print("切り上げ発生 x")

#연산자 입력후 실행
a = int(input("数字入力 : "))
b = int(input("数字入力 : "))
c = input("演算子入力 : ")
if c=="+":
    print(a,"と",b,"の合は",a+b)
if c=="-":
    print(a,"と",b,"の差は",a-b)
if c=="%":
    print(a,"と",b,"の割り算の余りは",a%b)
if c=="//":
    print(a,"と",b,"の割り算の商は",a//b)
if c=="*":
    print(a,"と",b,"の掛け算は",a*b)

#3의 배수 출력
a = int(input("数字入力 : "))
b = a%3
if b==0:
    print("３の倍数")
if b!=0:
    print("３の倍数 x")

#몇일뒤에 몇요일인지 출력
a = int(input(" 曜日入力 1(sun),2(mon),3(tus),4(wen),5(tur),6(fri),7(sat) : "))
b = int(input("何日後う? : "))
c = (a+b)%7
if c == 1:
    print("sun")
if c == 2:
    print("mon")
if c == 3:
    print("tus")
if c == 4:
    print("wen")
if c == 5:
    print("tur")
if c == 6:
    print("fri")
if c == 0:
    print("sat")