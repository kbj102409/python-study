#세자리수 입력후 거꾸로 뒤집었을때 더큰수 출력
print("3桁の数字入力")
A = int(input("数字入力 : "))
if A<100 or A>999:
    print("3桁数 x")
else:
    B = int(input("数字入力 : "))
    if B<100 or B>999:
        print("3桁数 x")
    else:
        if A != B:
            print("1桁と3桁を逆にし、大きのは",end="")
        else:
            print(end="")
        if A%10>B%10:
            print(A)
        elif A%10==B%10 and (A//10)%10>(B//10)%10:
            print(A)
        elif A%10==B%10 and (A//10)%10<(B//10)%10:
            print(B)
        elif A%10==B%10 and (A//10)%10==(B//10)%10 and A//10>B//10:
            print(A)
        elif A==B:
            print("AとBは同じ")
        else :
            print(B)

#자신이 태어난 생년월일 적고 무슨띠인지 출력하는 프로그램
print("子丑寅卯辰巳午未申酉戌亥(ね・うし・とら・う・たつ・み・うま・ひつじ・さる・とり・いぬ・い)")
y = int(input("何年生 : "))
m = int(input("何月生 : "))
if m>12 or m<0 :
    print("잘못된 입력")
else :
    d = int(input("何日生 : "))
    if d>31 or d<0:
        print("잘못된 입력")
    else :
        무슨띠 = y%12
        print("あなたは",y,"年",m,"月",d,"日生であり,",end="") 
        if 무슨띠 == 0:
            print("さる申")
        elif 무슨띠 == 1 :
            print("とり酉")
        elif 무슨띠 == 2:
            print("いぬ亥")
        elif 무슨띠 == 3:
            print("い戌")
        elif 무슨띠 == 4:
            print("ね子")
        elif 무슨띠 == 5:
            print("うし丑")
        elif 무슨띠 == 6:
            print("とら寅")
        elif 무슨띠 == 7:
            print("う卯")
        elif 무슨띠 == 8:
            print("たつ辰")
        elif 무슨띠 == 9:
            print("み巳")
        elif 무슨띠 == 10:
            print("うま午")
        elif 무슨띠 == 11:
            print("ひつじ未")

#ABCD가 하루씩 당번 할떄 몇일뒤에 누가 당번인지 출력하는 프로그램
d = int(input("何日後？ : "))
당번 = d%4
if 당번 == 0:
    print(d,"日後当番は A")
elif 당번 == 1:
    print(d,"日後当番は B")
elif 당번 == 2:
    print(d,"日後当番は C")
elif 당번 == 3:
    print(d,"日後当番は D")

#두자리수 두개(앞의것이 커야 출력) 입력후 내림 발생하는지 나타내는 프로그램
a = int(input("１番目の数 : "))
if a>=100 or a<=9 :
    print("2桁ではありません.")
else :
    b = int(input("２番目の数 :"))
    if b>=100 or b<=9:
        print("2桁ではありません.")
    elif b>a:
        print("２番目の数の方が大きいです")
    else :
        if a%10 >b%10:
            print("切り下げ x")
        else:
            print("切り下げ発生")

#30분전 시간
h = int(input("何時なのか入力(午後、午前分け不可) : "))
if h >=24 or h<0 :
    print("入力エラー")
else:
    m = int(input("何分なのか入力 : "))
    if m>=60 or m<0:
        print("入力エラー")
    else:
        c = (60*h+m)-30
        if h==0 and m<30:
            print((1440+c)//60,"時",(1440+c)%60,"分")
        else:
            print(c//60,"時",c%60,"分")

#n분 전 시간
h = int(input("何時なのか入力(午後、午前分け不可) : "))
if h >=24 or h<0 :
    print("入力エラー")
else:
    m = int(input("何分なのか入力　: "))
    if m>=60 or m<0:
        print("入力エラー")
    else:
        n = int(input("何分前なのか入力 : "))
        c = (60*h+m)-n
        #c는 시간분을 분으로 나타냈을때
        if h==0 and m<n :
            print(n,"分前の時間は",(1440+c)//60%24,"時",(1440+c)%60,"分")
        else:
            print(n,"分前の時間は",c//60,"時",c%60,"分")

#n분 후 시간
h = int(input("何時なのか入力(午後、午前分け不可) : "))
if h >=24 or h<0 :
    print("入力エラー")
else:
    m = int(input("何分なのか入力 : "))
    if m>=60 or m<0:
        print("入力エラー")
    else:
        n = int(input("何分後なのか入力 : "))
        c = (60*h+m)+n
        if c>=1440 :
            print(n,"分後時間は",(c-1440)//60%24,"時",(c-1440)%60,"分")
        else:
            print(n,"分後時間は",c//60,"時",c%60,"分")

#ABCD가 당번 3일씩 돌아가면서 함 몇일뒤 누가 당번인가출력
d = int(input("何日後なのか？ : "))
당번 = d//3%4
if 당번 == 0:
    print(d,"日後当番は A")
elif 당번 == 1:
    print(d,"日後当番は B")
elif 당번 == 2:
    print(d,"日後当番は C")
elif 당번 == 3:
    print(d,"日後当番は D")