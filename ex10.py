#break사용법
# for i in range(10):
#     print(i)
#     if i ==2 :
#         break

##break의 리스트에서의 활용법
# for i in ['a','b','c','d','e']:
#     print(i)
#     if i == 'd':
#         break

##continue의 기능과 break와 동시 사용
# for i in ['a','b','c','d','e']:
#     if i =='a':
#         continue
#     if i =='d':
#         break
#     print(i)

#while사용해서 1~10까지 출력
# i=1
# while i<11:
#     print(i)
#     i+=1

##리스트에 넣은 수들 0입력하면 전부 합하기
# li = []
# while True :
#     a = int(input())
#     li.append(a)
#     if a==0:
#         print(sum(li))
#         break

#리스트에 입력한 수 평균 구하기
# li = []
# while True :
#     a = float(input())
#     if a==0:
#         print(sum(li)/len(li))
#         break
#     li.append(a)

# #입력한 수들의 평균 구하고 평균 이하인수 출력
# li =[]
# while True:
#     a = int(input())
#     if a == 0 :
#         c =sum(li)/len(li)
#         print(c)
#         for k in li:
#             if c<k:
#                 print(k,"平均以上")
#         break
#     li.append(a)

# #키오스크 프로그램 업그레이드 버전
# import os
# import time
# su = 0
# while True:
#     #메뉴출력
#     print('-'*4,"MENU",'-'*4)
#     print("1.コーラ/300")
#     print("2.サイダー/300")
#     print("3.コーヒー/200")
#     print("4.お金投入")
#     print("5.お釣り返還")
#     print("6.終了")
#     print("-"*12)
#      #선택받음
#     print(su)
#     a = int(input("入力 : "))
    
#     #선택에따라 처리
#     if a ==1:
#         if  su >= 300:
#             print("コーラ、ありがとうこざいます")
#             su -= 300
#         else:
#             print("金額不足")
#     elif a ==2:
#         if  su >= 300:
#             print("サイダー、ありがとうこざいます")
#             su -= 300
#         else:
#             print("金額不足")
#     elif a ==3:
#         if  su >= 200:
#             print("コーヒー、ありがとうこざいます")
#             su -= 200
#         else:
#             print("金額不足")       
#     elif a ==4:
#         b = int(input(" 入力: "))
#         su += b
#     elif a ==5:
#         su = 0
#         print("お釣りが返還されました")
#     elif a ==6:
#         print("終了")
#         break
#     else :
#         print("エラー!")
#     time.sleep(0.6)
#     os.system("clear")

