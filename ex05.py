#양수 음수 입력    
a = int(input("数字入力 : "))
if a<0:
    print("負数")
elif a>0:
    print("陽数")
else :
    print("0")

#평균점 불합 여부 구분
국 = float(input("日本語 : "))
수 = float(input("数学 : "))
평균 = (국+수)/2
if 평균>=80.0:
    print("合")
else : 
    print("不合")

#점수대 별로 등급 매기기
수 = float(input("数学 : "))
과 = float(input("科学 : "))
평 = (수+과)/2
if 평>=90:
    print("A")
elif 평>=80:
    print("B")
elif 평>=70:
    print("C")
else :
    print("D")

#사칙연산 실행 프로그램
a = int(input(" 数字入力 : "))
b = int(input(" 数字入力 : "))
c = int(input(" 演算者 +(1),-(2),/(3),*(4)입력 : "))
if c==1:
    print(a+b)
elif c==2:
    print(a-b)
elif c==3:
    print(round(a/b,2))
elif c==4:
    print(a*b)
else :
    print("演算者ではありません!")

#몇개월뒤 몇월인가 나오는 프로그램
a = int(input("今月 : "))
b = int(input("何月後？ : "))
c = (a+b)%12
if a >12:
    print("入力が間違っています")
elif 3<=c<=5:
    print(b,"ヶ月後は春です")
elif 6<=c<=8:
    print(b,"ヶ月後は夏です")
elif 9<=c<=11:
    print(b,"ヶ月後は秋です")
elif 12==c or c<=2:
    print(b,"ヶ月後は冬です")

#특정 아이디 패스워드 등록 프로그램
아이디 = input("アカウント入力 :")
if 아이디 == "admin":
    print("hello, admin :)")
    패스워드 = input("パスワード入力 : ")
    if 패스워드 == "admin":
        print("login success :)")
    else :
        print("login fail :(")
else :
    print("not user :(")

#절대값 구하는 프로그램
a = int(input("数字入力 : "))
if a>0:
    print("絶対値は",a)
else:
    print("絶対値は",(-a))

#과일 구매후 잔돈구하는 프로그램
돈 = int(input("保有金額 : "))
배 = int(input("希望するむナシ個数 : "))
사과 = int(input("希望するリンゴ個数 : "))
잔돈 = 돈-(배*2000+사과*3000)
if 돈<(배*2000+사과*3000):
    print("購入不可")
    print("購入のため",-잔돈,"必要")
else :
    print("お釣りは",잔돈)

#15,3,5 배수 구하는 프로그램
n = int(input("数字入力 : "))
if n%15==0:
    print("15 倍数")
elif n%3==0:
    print("3의 倍数")
elif n%5==0:
    print("5의 倍数")

#카페 키오스크 프로그램 (간략)
print("="*20)
print("1. アメリカーノ")
print("2. カフェラテ")
print("="*20)
a = int(input("メニュー選択 : "))
if a:
    print("="*20)
    print("1. ICE")
    print("2. HOT")
    print("="*20)
b = int(input("온도 선택 : "))
if a ==1:
    if b==1:
        print("アイスアメリカーノ")
    else:
        print("ホットアメリカーノ")
else :
    if b==1:
        print("アイスカフェラテ")
    else:
        print("ホットカフェラテ")

#윤달 구하는 프로그램
y = int(input("年度入力 : "))
if y%400==0:
    print("閏月")
elif y%100==0:
    print("閏月x")
elif y%4==0:
    print("閏月")
else:
    print("閏月x")
    