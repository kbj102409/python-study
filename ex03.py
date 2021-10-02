# "input"명령어 사용법1
input("入力 : ")
print(input("入力 : "))

# "input"명령어 사용법2
a = input("入力 : ")
print("aは", a)

# "input"명령어 예제1
A = input("あなたのお名前は : ")
B = input("あなたの年齢は : ")
C = input("メールアドレス : ")
print("あなたの名前は",A)
print("年齢は",B)
print("メールアドレスは",C)

# "input"명령어 예제2
q = input("入力 : ")
w = input("入力 : ")
print(int(q)+int(w))

# 성적 평균 출력
A = int(input("英語点数 : "))
B = int(input("数学点数 : "))
print("平均値は", int((A+b)/2))

# 과일 가격 출력 (1)
aw = int(input("リンゴの値段 : "))*int(input("リンゴの個数 : "))
pw = int(input("ナシの値段 : "))*int(input("ナシの個数 : "))
총금액 = aw+pw
print("果物の総金額は", 총금액)

# 과일 가격 출력 (보기 좋은 버전)
A = 3000
B = 2000
print("="*13)
print("リンゴ",":",A)
print("ナシ",":",B)
print("="*13)
print()
ap = int(input("リンゴ個数 : "))
pp = int(input("ナシ個数　: "))
C = ap*A+pp*B
print("総値段は", C)

# 시간,분,초를 총몇초로나타내는가
시 = int(input("時 : "))
분 = int(input("分 : "))
초 = int(input("秒 : "))
총몇초 = 초+분*60+시*60*60
print(시,"時",분,"分",초,"秒","=",총몇초)

# 섭씨를 화씨로 바꿔주는 프로그램
섭씨 = float(input("セルシウス度 : "))
화씨 = (섭씨*1.8)+float(32)
print("セルシウス度",섭씨,"は華氏温度", float(화씨))

# bmi측정해주는 프로그램
체중 = float(input("あなたの体重は? : "))
키 = float(input("あなたの身長は? : "))
bmi = 체중/(키**2)
print("あなたのbmiは", round(bmi,2))

# 각 자리수 출력
원하는수 = int(input("３桁の数字 : "))
h = 원하는수//100
t = (원하는수//10)%10
o = 원하는수%10
print("1桁目",h,"2桁目",t,"3桁目",o)

# 초를 시간 분 초로 출력
ts = int(input("全部何秒? : "))
h = ts//3600
m = (ts%3600)//60
s = (ts%3600)%60
print(h,"時間",m,"分",s,"秒")