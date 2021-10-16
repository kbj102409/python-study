# import random
# import os
# import time
# life = 5
# score = 0
# while True :
#     com = random.randint(1,10)
#     # print(random.randint(1,10))
#     if life == 0:
#         print("game over")
#         print("score",score)
#         break
#     print("="*20)
#     print(f"your life {'❤️'*life}")
#     print(f"your score {score}")
#     user = int(input("奇(1), 具(0)?"))
#     if com %2 ==0:
#         if user == 0:
#             score +=100
#             print("正解です")
#         else : 
#             life -=1
#             print("誤答です")
#     else:
#         if user == 1:
#             score +=100
#             print("正解です")
#         else:
#             life -=1
#             print("誤答です")
#     print(f"ランダムで引いた数 : {com}")
#     time.sleep(0.7)
#     os.system("clear")



# import random
# import time
# import os
# while True:
#     while True:
#         level = int(input("レベル選択 easy(1),nomal(2),hard(3) : "))
#         if level == 1:    
#             com = random.randint(1,9)
#         elif level ==2:
#             com = random.randint(10,99)
#         elif level ==3:
#             com = random.randint(100,999)
#         else:
#             print("もう一度選択してください")
#             continue
#         break
#     su = 0
#     while True :
#         su +=1
#         print("="*20)
#         print(f"{su}番目試し")
#         print("="*20) 
#         user = int(input("なんの数なのか?"))           
#         if com == user:
#             print("勝利")
#             print(f"コンピューターの数{com}")
#             print(f"{su}番目で正解")
#             break
#         elif com<user:
#             print("down")           
#         else:
#             print("up")
#         time.sleep(0.7)
#         os.system("clear")    
#     again = int(input("継続しますか はい(1) いいえ(2) : "))
#     if again == 2:
#         print("bye bye")
#         break




# import random
# import time
# import os
# while True :
#     level = int(input("レベル選択 1(easy) 2(normal) 3(hard) : "))
#     while True:
#         if level == 1 :
#             r1 = 1
#             r2 = 9
#         elif level == 2 :
#             r1 = 10
#             r2 = 99
#         elif level == 3 :
#             r1 = 100
#             r2 = 999
#         else :
#             print("もう一度選択してください")
#             continue
#         break
#     life = 5
#     score = 0
#     while True:    
#         A = random.randint(r1,r2)
#         B = random.randint(r1,r2)
#         R = random.randint(1,2)
#         s200 = random.randint(1,5)
#         l2 = random.randint(1,10)
#         if s200 == 1:
#             print("今回の問題スコア +200")
#             점수 =200
#         else :
#             점수 =100
#         if l2 == 1:
#             print("今回誤答ライフ -2")
#             목숨 = 2
#         else :
#             목숨 = 1
#         print("="*20)
#         print("life = ",life)
#         print("score = ",score)
#         print("="*20)
#         if R == 1:
#             user = int(input(f"{A} + {B} =  "))
#             C = A + B
#         elif R == 2:
#             if A > B :
#                 user = int(input(f"{A} - {B} =  "))
#                 C = A - B
#             elif B > A :
#                 user = int(input(f"{B} - {A} =  "))
#                 C = B - A       
#         if user == 9999:
#             print("システム終了")
#             break    
#         if C == user:
#             print("正解です")
#             score +=점수
#         else :
#             print("誤答です")
#             life -= 목숨
#         if life <= 0:
#             print("game over")
#             break
#         time.sleep(0.7)
#         os.system("clear")
#     again = int(input("継続しますか 1(yes) 2(no) ? "))
#     if again == 2:
#         print("good bye")
#         break
