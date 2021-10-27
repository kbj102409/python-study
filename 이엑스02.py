# #他のファイルから要素もってくる
# import 이엑스01 as e1
# A = e1.모험가()
# B = e1.add(10,20)
# C = e1.B
# print(A,B,C)

# #from~import使用（ランダム、タイム）
# from time import sleep
# sleep(1)
# from random import randint
# randint(1,10)

#現ディレクトリからファイル生成
# f = open("hello.txt","w")
# f.close()

#ファイル生成後、内容入力
# f = open("mama.txt","w")
# f.write("Hello World")
# f.close()

# #現ファイルに英語以外の言語入力
# f = open("mama.txt","w",encoding="utf-8")
# for i in range(1,101):
#     f.write(f"파이썬 마스터 {i}\n")
# f.close()

# #read,readline,readlines性質
# f = open("mama.txt","r",encoding="utf-8")
# print(f.read())
# print(f.readline())
# print(f.readlines())
# f.close()

# #イメージ他の名前で写す
# f = open("리자몽.png","rb")
# g = open("수컷리자몽.png","wb")
# g.write(f.read())
# f.close()
# g.close()

#txtにある情報に追加情報（平均）入力
f = open("score.txt","r",encoding="utf-8")
g = open("average.txt","w",encoding="utf-8")
f.readline()
g.write("日本語\t数学\t科学\t平均\n")
for i in f.readlines():
    A = i.split()
    # kor = int(A[0])
    # math = int(A[1])
    # sci = int(A[2])
    kor,math,sci = map(int,i.split())
    ave = (kor+math+sci)/3
    print(ave)
    g.write(f"{kor}\t{math}\t{sci}\t{ave}\n")
f.close()
g.close()
