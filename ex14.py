#setのtype
# s1 = {1,1.2,"hello"}
# s2 = {}
# print(type(s1))
# print(type(s2))

#set有無の違い
# li = [1,2,3,4,1,2,3,4,1,1,1,2,1,1]
# for i in li :
#     print(f"{i}의 등장 횟수 = {li.count(i)}")
# for i in set(li):
#     print(f"{i}의 등장횟수 = {li.count(i)}")

# #dynamiteの各単語の繰り返し回数を求める
# dy = """'Cause I-I-I'm in the stars tonight
# So watch me bring the fire and set the night alight
# Shoes on, get up in the morning
# Cup of milk, let's rock and roll
# King Kong, kick the drum, rolling on like a Rolling Stone
# Sing song when I'm walking home
# Jump up to the top, LeBron
# Ding dong, call me on my phone
# Ice tea and a game of ping pong, huh
# This is getting heavy
# Can you hear the bass boom? I'm ready (woo hoo)
# Life is sweet as honey
# Yeah, this beat cha-ching like money, huh
# Disco overload, I'm into that, I'm good to go
# I'm diamond, you know I glow up
# Hey, so let's go
# 'Cause I-I-I'm in the stars tonight
# So watch me bring the fire and set the night alight (hey)
# Shining through the city with a little funk and soul
# So I'ma light it up like dynamite, whoa oh oh
# Bring a friend, join the crowd
# Whoever wanna come along
# Word up, talk the talk
# Just move like we off the wall
# Day or night, the sky is  alight
# So we dance to the break of dawn
# Ladies and gentlemen, I got the medicine
# So you should keep ya eyes on the ball, huh
# This is getting heavy
# Can you hear the bass boom? I'm ready (woo hoo)
# Life is sweet as honey
# Yeah, this beat cha-ching like money
# Disco overload, I'm into that, I'm good to go
# I'm diamond, you know I glow up
# Let's go
# 'Cause I-I-I'm in the stars tonight
# So watch me bring the fire and set the night alight (hey)
# Shining through the city with a little funk and soul
# So I'ma light it up like dynamite, whoa oh oh
# Dy-na-na-na, na-na, na-na-na, na-na-na, life is dynamite
# Dy-na-na-na, na-na, na-na-na, na-na-na, life is dynamite
# Shining through the city with a little funk and soul
# So I'ma light it up like dynamite, whoa oh oh
# Dy-na-na-na, na-na, na-na, ayy
# Dy-na-na-na, na-na, na-na, ayy
# Dy-na-na-na, na-na, na-na, ayy
# Light it up like dynamite
# Dy-na-na-na, na-na, na-na, ayy
# Dy-na-na-na, na-na, na-na, ayy
# Dy-na-na-na, na-na, na-na, ayy
# Light it up like dynamite
# 'Cause I-I-I'm in the stars tonight
# So watch me bring the fire and set the night alight
# Shining through the city with a little funk and soul
# So I'ma light it up like dynamite (this is ah)
# 'Cause I-I-I'm in the stars tonight
# So watch me bring the fire and set the night alight (alight, oh)
# Shining through the city with a little funk and soul
# So I'ma light it up like dynamite, whoa (light it up like dynamite)
# Dy-na-na-na, na-na, na-na-na, na-na-na, life is dynamite
# Dy-na-na-na, na-na, na-na-na, na-na-na, life is dynamite
# Shining through the city with a little funk and soul
# So I'ma light it up like dynamite, whoa oh oh"""
# 제거 = "()?!-,\""
# for i in 제거:
#     dy = dy.replace(i, " ")
# dy = dy.replace("'m", " am ")
# dy = dy.replace("t's", "t us ")
# dy = dy.lower()
# 단어 = dy.split()
# for i in set(단어):
#     print(f"{i}の登場回数 = {단어.count(i)}")
# #dictionaryを利用し、dynamiteの各単語の繰り返し回数を入れる
# # 사전 = {}
# # #key : 単語, value : 頻度数
# # for i in set(단어):
# #     사전[i] = 단어.count(i)
# # print(사전)



#dictionaryの仕組み
# di = {1:"one",2:"two",3:"three"}
# di[4] = "four"
# di[5] = "five"
# del di[1]
# print(di)

# #dictionaryの活用
# d = {1:"one",2:"two",3:"three"}
# for i in d :
#     print(f"key 値:{i}, value 値:{d[i]}")

##turtleを用いて図形や使用者の絵を描く
# import turtle as t
# from random import randint
# t.shape("turtle")
# t.pensize(7)
# t.speed(0)
# t.colormode(255)
# t.setup(1200,600)
###3〜n図形を自動で作る
# # n = int(t.numinput("입력창","3에서 30까지 입력",minval=3,maxval=30))
# # for k in range(3,n+1):
# #     for i in range(k):
# #         t.fd(100)
# #         t.lt(360/k)
# #t.mainloop()
# t.listen()
# def 위로이동():
#     t.seth(90)
#     t.fd(50)
# t.onkey(위로이동,"Up")
# def 아래로이동():
#     t.seth(270)
#     t.fd(50)
# t.onkey(아래로이동,"Down")
# def 좌로이동():
#     t.seth(180)
#     t.fd(50)
# t.onkey(좌로이동,"Left")
# def 우로이동():
#     t.seth(0)
#     t.fd(50)
# t.onkey(우로이동,"Right")
# def 원점이동():
#     t.pu()
#     t.goto(0,0)
#     t.pd()
# t.onkey(원점이동,"space")
# def 색바꾸기():
#     t.color(randint(0,255),randint(0,255),randint(0,255))
# t.onkey(색바꾸기,"c")
# def 펜상태바꾸기():
#     if t.isdown():
#         t.pu()
#     else:
#         t.pd()
# t.onkey(펜상태바꾸기,"p")
# t.mainloop()


#Dynamite歌詞の繰り返し回数が多い単語をGUIで大きく表し、単語がランダムで出力
# import turtle as t
# from random import randint
# import dyna
# t.speed(0)
# t.colormode(255)
# t.setup(1200,600)
# t.pu()
# t.ht()
# 사전 = dyna.사전
# for i in 사전:
#     t.goto(randint(-500,400),randint(-280,250))
#     t.write(i,font=("맑은 고딕", (사전[i]+5)*2, "bold"))
#     t.color(randint(0,255),randint(0,255),randint(0,255))

# t.mainloop()