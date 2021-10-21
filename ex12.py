# 関数を利用しaとbの積を求める
# 入力値:a,b
# 返還値:두수곱
# def 두수곱(a,b):
#     곱 = a*b
#     return 곱
# print(두수곱(10,20))

#aとbのうち、大きい数を表わす
# 入力値 : a,b
# 返還値 : 큰수
# def 크기비교(a,b):
#     if a > b:
#         큼 = a
#     elif b >a :
#         큼 = b
#     return 큼
# print(크기비교(10,30))

#aとbの間の差を求める
#入力値 : a,b
#返還値: 두수차이
# def 두수(a,b):
#     if a>b:
#         두수차이 = a-b
#     else :
#         두수차이 = b-a

#     return 두수차이
# print(두수(10,20))

#aの約数を求める関数
# 入力値 : a
# 返還値　: 약수
# def 두수(a):
#     약수 = []
#     for i in range(1,a+1):
#         if a % i == 0:
#             약수.append(i)
#     return 약수
# for k in range(1,20):
#     print(두수(k))

#aのfactorialを求める
#入力値 : a
#返還値 : factorial
# def factorial(a):
#     fact = 1
#     for i in range(1,a+1):
#         fact *= i
#     return fact
# print(factorial(5))

#素数を判別する関数
#入力値:a
#返還値 :약수
# def 판별수(a):
#     약수 = 0
#     for i in range(1,a+1):
#         if a % i == 0:
#             약수 += 1 
#     if 약수 ==2:
#         print("素数")
#     else:
#         print("素数 x")
# print(판별수(12))

#地域変数の性質
# def plus_A(A):
#     A += 1
#     return A
# A=10
# A=plus_A(A)
# print(A)

#地域変数の性質
# def plus_A2():
#     global A
#     A += 1
# A =10
# plus_A2()
# print(A)

#関数の使い目的
#簡潔で可読性が上がる
#再使用しやすいため、他人と共有するときに混線がない