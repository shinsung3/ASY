# 4. 변수
# 01. 1~9 사이의 정수 a를 입력받아 
# a + aa + aaa + aaaa 의 값을 계산하는 프로그램을 작성하십시오.
# 입력 : 9
# 출력 : 11106 
# ----------------------------------------
# a = input()
# b = int(a)
# sum = 0
# sum += b
# sum += (b*10 + b)
# sum += (b*100 + b*10 +b)
# sum += (b*1000 + b*100 + b*10 + b)
# print(sum)
##############################

# 5. 연산자
# 02. 인치(inch)를 센티미터(cm)으로 변환하는 프로그램을 작성하십시오.
# 이 때 1 인치는 2.54 센티미터입니다.
# 입력
# 3
# 출력
# 3.00 inch => 7.62 cm
# ----------------------------------------
# a = int(input())
# b = a*2.54
# print("%.2f inch => %.2f cm" %(a,b))
##############################

# 5. 연산자
# 03. 킬로그램(kg)를 파운드(lb)으로 변환하는 프로그램을 작성하십시오.
# 이 때 1 킬로그램은 2.2046 파운드입니다.
# 입력
# 90
# 출력
# 90.00 kg =>  198.41 lb
# ----------------------------------------
# a = int(input())
# b = a*2.2046
# print("%.2f kg => %.2f lb" %(a,b))
##############################

# 6. if 흐름제어
# 04. 다음의 결과와 같이 임의의 양의 정수를 입력받아 그 정수의 모든 약수를 구하십시오
# 입력
# 9
# 출력
# 1(은)는 9의 약수입니다.
# 3(은)는 9의 약수입니다.
# 9(은)는 9의 약수입니다.
# ----------------------------------------
# a = int(input())
# for i in range(1, a+1):
#     if a % i == 0:
#         print("%d(은)는 %d의 약수입니다." %(i, a))
##############################

# 6. if 흐름제어
# 05. 다음의 결과와 같이 임의의 양의 정수를 입력받아 그 정수의 모든 약수를 구하십시오
# (단, 약수가 2개일 경우 소수임을 나타내십시오)
# 입력
# 5
# 출력
# 1(은)는 5의 약수입니다.
# 5(은)는 5의 약수입니다.
# 5(은)는 1과 5로만 나눌 수 있는 소수입니다.
# ----------------------------------------
# a = int(input())
# cnt = 0
# for i in range(1, a+1):
#     if a % i == 0:
#         cnt+=1
#         print("%d(은)는 %d의 약수입니다." %(i, a))
# if cnt == 2:
#     print("%d(은)는 1과 %d로만 나눌 수 있는 소수입니다." %(a, a))
##############################

# 6. if 흐름제어
# 06. 다음의 결과와 같이 입력된 영어 알파벳 문자에 대해 대소문자를 구분하는 코드를 작성하십시오.
# 입력
# b
# 출력
# b 는 소문자 입니다.
# ----------------------------------------
# a = input()
# if a>='a' and a<='z':
#     print("%s는 소문자입니다." %(a))
# if a>='A' and a<='Z':
#     print("%s는 대문자입니다." %(a))
##############################

# 6. if 흐름제어
# 07. 1~200 사이의 정수 가운데 7의 배수이면서 5의 배수는 아닌 모든 숫자들을 찾아
# 콤마(,)로 구분된 문자열을 구성해 출력하는 프로그램을 작성하십시오.
# 출력
# 7,14,21,28,42,49,56,63,77,84,91,98,112,119,126,133,147,154,161,168,182,189,196
# ----------------------------------------
# answer = ""
# for i in range(1,201):
#     if i%7 == 0 and i%5 !=0:
#         answer += (str(i)+",")
# print(answer[:-1]) 
##############################

# 7. for - 반복
# 08. 다음의 결과와 같이 5명의 학생의 점수에 대해 60 이상일 때 합격 메시지를 출력하고,
# 60미만일 때 불합격 메시지를 출력하는 프로그램을 만드십시오.
# 출력
# 1번 학생은 88점으로 합격입니다.
# 2번 학생은 30점으로 불합격입니다.
# 3번 학생은 61점으로 합격입니다.
# 4번 학생은 55점으로 불합격입니다.
# 5번 학생은 95점으로 합격입니다.
# ----------------------------------------
# a = [88, 30, 61, 55, 95]
# for i in range(len(a)):
#     if a[i] >= 60 :
#         print("%d번 학생은 %d점으로 합격입니다." %((i+1), a[i]))
#     else :
#         print("%d번 학생은 %d점으로 불합격입니다." %((i+1), a[i]))
##############################

# 7. for - 반복
# 09. 1부터 100사이의 숫자 중 홀수를 for 문을 이용해 다음과 같이 출력하십시오.
# 출력
# 1, 3, 5, 7, 9, ... 95, 97, 99
# ----------------------------------------
# answer = ""
# for i in range(1, 101):
#     if i%2!=0:
#         answer += (str(i)+", ")
# print(answer[:-2])
##############################

# 7. for - 반복
# 10. 다음은 10명의 학생들의 혈액형(A, B, AB, O) 데이터입니다.
# ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
# for 문을 이용하여 각 혈액형 별 학생수를 구하십시오.
# 출력
# {'A': 3, 'O': 3, 'B': 2, 'AB': 2}
# ----------------------------------------
# a = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
# A = 0
# B = 0
# C = 0
# O = 0
# for i in a:
#     if i == 'A':
#         A+=1
#     elif i == 'B':
#         B+=1
#     elif i == 'O':
#         O+=1
#     elif i == 'AB':
#         C+=1
# print("{'A': %d, 'O': %d, 'B': %d, 'AB': %d}" %(A, O, B, C))
##############################

# 7. for - 반복
# 11. 다음은 학생의 점수를 나타내는 리스트입니다.
# [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
# while 문과 리스트 객체의 pop()을 이용해 80점 이상의 점수들의 총합을 구하시오.
# 출력
# 454
# ----------------------------------------
# a = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
# sum = 0
# while len(a)>0:
#     b = a.pop()
#     if b>=80:
#         sum += b
# print(sum)
##############################

# 7. for - 반복
# 12. 별(*)을 표시하는 프로그램을 만드십시오.
# 출력
# *****
# ****
# ***
# **
# *
# ----------------------------------------
# answer = ""
# for i in range(5):
#     for j in range(5-i):
#         answer+="*"
#     answer+="\n"
# print(answer[:-1])
##############################

# 7. for - 반복
# 13. 다음의 결과와 같이 어떤 한 양의 정수를 입력하여 그 숫자에 0~9가 몇 번 사용되었는지 표시하십시오.
# 입력
# 11
# 출력
# 0 1 2 3 4 5 6 7 8 9
# 0 2 0 0 0 0 0 0 0 0
# ----------------------------------------
# a = input()
# cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# for i in range(len(a)):
#     b = int(a[i])
#     cnt[b]+=1
# answer = ""
# for i in range(len(cnt)):
#     answer += str(i)+" "
# answer +="\n"
# for i in cnt:
#     answer += str(i)+" "
# print(answer[:-1])
##############################

# 7. for - 반복
# 14. for문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.
# 출력
#     *
#    **
#   ***
#  ****
# *****
# ----------------------------------------
# answer = ""
# for i in range(5):
#     for j in range(5-i-1):
#         answer += " "
#     for j in range(i+1):
#         answer += "*"
#     answer += "\n"
# print(answer[:-1])
##############################

# 8. def - 함수
# 15. 다음의 결과와 같이 반목문을 이용해 단어의 순서를 거꾸로 해 반환하는 함수를 작성하고
# 그 함수를 이용해 회문(앞뒤 어느 쪽에서도 같은 단어, 말) 여부를 판단하는 코드를 작성하십시오.
# 입력
# eye
# 출력
# eye
# 입력하신 단어는 회문(Palindrome)입니다.
# ----------------------------------------
# def palindrome(word):
#     a = word[::-1]
#     if a==word:
#         print(word)
#         print("입력하신 단어는 회문(Palindrome)입니다.")
# word = input()
# palindrome(word)
##############################

# 8. def - 함수
# 16. 다음과 같이 사용자 2명으로부터 가위, 바위, 보를 입력 받아
# 가위, 바위, 보 규칙이 정의된 함수를 이용해 승패를 결정하는 코드를 작성하십시오.
# 입력
# 홍길동
# 이순신
# 가위
# 바위
# 출력
# 이순신(이)가 이겼습니다!
# ----------------------------------------
# def game(name1, name2, nameAttack1, nameAttack2):
#     if nameAttack1=="가위":
#         if nameAttack2 == "바위":
#             print("%s(이)가 이겼습니다!" %(name2))
#         elif nameAttack2 == "보":
#             print("%s(이)가 이겼습니다!" %(name1))
#         else:
#             print("비겼습니다!")
#     elif nameAttack1=="바위":
#         if nameAttack2 == "바위":
#             print("비겼습니다!")
#         elif nameAttack2 == "보":
#             print("%s(이)가 이겼습니다!" %(name2))
#         else:
#             print("%s(이)가 이겼습니다!" %(name1))
#     else:
#         if nameAttack2 == "바위":
#             print("%s(이)가 이겼습니다!" %(name1))
#         elif nameAttack2 == "보":
#             print("비겼습니다!")
#         else:
#             print("%s(이)가 이겼습니다!" %(name2))
# name1 = input()
# name2 = input()
# nameAttack1 = input()
# nameAttack2 = input()
# game(name1, name2, nameAttack1, nameAttack2)
##############################

# 8. def - 함수
# 17. 다음의 결과와 같이 피보나치 수열의 결과를 생성하는 프로그램을 작성하십시오.
# 입력
# 10
# # 출력
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# ----------------------------------------
# def fibo(a):
#     curr, next = 0,1
#     answer = []
#     for i in range(a):
#         curr, next = next, curr+next
#         answer.append(curr)
#     return answer
# a = int(input())
# print(fibo(a))
##############################

# 8. def - 함수
# 18. 리스트의 항목 중 유일한 값으로만 구성된 리스트를 반환하는 함수를 정의하고
# 이 함수를 이용해 리스트의 중복 항목을 제거하는 프로그램을 작성하십시오.
# 출력
# [1, 2, 3, 4, 3, 2, 1]
# [1, 2, 3, 4]
# ----------------------------------------
# def findList():
#     a = [1, 2, 3, 4, 3, 2, 1]
#     answer = []
#     for i in a:
#         flag = False
#         for j in answer:
#             if i == j:
#                 flag = True
#         if flag == False:
#             answer.append(i)
#     print(answer)
# findList()
##############################

# 8. def - 함수
# 19. 다음과 같이 팩토리얼을 구하는 함수를 정의해 입력된 숫자에 대한
# 팩토리얼 값을 구하는 프로그램을 작성하십시오.
# 입력
# 5
# 출력
# 120
# ----------------------------------------
# def fact(a):
#     answer = 1
#     for i in range(1,a+1):
#         answer *= i
#     return answer
# a = int(input())
# print(fact(a))
##############################

# 9. 내장함수
# 20. -3.14의 절댓값 구하기. abs()
# 입력
# -3.14
# 출력
# 3.14
# ----------------------------------------
# a = float(input())
# print(abs(a))
##############################

# 9. 내장함수
# 21. - 2개의 숫자가 입력되었을 때, 몫과 나머지 구하기
# divmod() - 첫번째 인자와 두번째 인자를 나눴을 때의 몫과 나머지를 튜플 객체로 반환하는 함수
# 입력
# 9 5
# 출력
# (1, 4)
# 몫: 1 나머지: 4
# ----------------------------------------
# a, b = input().split()
# a = int(a)
# b = int(b)
# result_tuple = divmod(a,b)
# print(result_tuple)
# print("몫: %d 나머지: %d" %(result_tuple[0], result_tuple[1]))
##############################

# 9. 내장함수
# 22. - list의 제곱 [1,2,3,4,5]
# pow()
# 출력
# [1, 4, 9, 16, 25]
# ----------------------------------------
# a = [1,2,3,4,5]
# answer = []
# for i in range(len(a)):
#     answer.append(pow(a[i],2))
# print(answer)
##############################

# 9. 내장함수
# 22. 
# all() - 반복 가능한 자료형인 List, Tuple, Set, dictionary, 문자열 등을 인자로 전달하여
# 항목 모두가 True로 평가되면 True로 반환. False가 하나라도 있으면 False
# [10, 20, 0] -> False
# [10, 10, 20] -> True;
# ----------------------------------------
# a = [10, 20, 0]
# print(all(a))
# b = [10, 20, 30]
# print(all(b))
# c = [10, 20, '']
# print(all(c))
##############################

# 9. 내장함수
# 23.
# any() - 반복 가능한 자료형인 List, Tuple, Set, dictionary, 문자열 등을 인자로 전달하여
# 항목 모두가 False로 평가되면 False로 반환. True가 하나라도 있으면 True
# [10, 20, 0] -> True
# [10, 10, 20] -> True;
# ['', 0, False] -> False
# ----------------------------------------
# a = [10, 20, 0]
# print(any(a))
# b = [10, 10, 20]
# print(any(b))
# c = ['', 0, False]
# print(any(c))
##############################

# 9. 내장함수
# 24. 
# enumerate() - List, Tuple, 문자열과 같은 시퀀스형을 입력받아 
# 인덱스를 포함하는 튜플 객체를 항목으로 구성하는 enumerate 객체를 반환하는 함수
# 출력
# 0 10
# 1 20
# 2 30
# 3 40
# 4 50
# ----------------------------------------
# a = [10,20,30,40,50]
# for idx, val in enumerate(a):
#     print(idx, val)
##############################

# 9. 내장함수
# 24. 짝수를 찾아내기. 
# [1,2,3,4,5,6,7,8,9,10]
# filter() - 조건에 해당하는 항목을 걸러내는 함수
# 출력
# #1  [2, 4, 6, 8, 10]
# <class 'filter'>
# #2  [2, 4, 6, 8, 10]
# ----------------------------------------
# def even(a):
#     return a%2==0
# a = [1,2,3,4,5,6,7,8,9,10]
# answer = filter(even, a) #even 함수가 True를 반환한 짝수 값을 항목으로 하는 리스트 생성 후 반환
# print("#1 ", list(answer))
# print(type(answer))
# print("#2 ", list(filter(lambda n: n%2==0, a)))
##############################

# 9. 내장함수
# 25. "Hello" list(), set(), dict(), tuple()만들기 
#1  ['H', 'e', 'l', 'l', 'o']
#2  ('H', 'e', 'l', 'l', 'o')
#3  {'H', 'o', 'l', 'e'}
#4  {0: 'H', 1: 'e', 2: 'l', 3: 'l', 4: 'o'}
# ----------------------------------------
# data = "Hello"
# dataList = list(data)
# print("#1 ", dataList)
# dataTuple = tuple(data)
# print("#2 ", dataTuple)
# dataSet = set(data)
# print("#3 ", dataSet)
# dataDict = dict(enumerate(data))
# print("#4 ", dataDict)
##############################

# 9. 내장함수
# 26. 모든 문자를 대문자로 만들기
# map() - 두 번째 인자로 반복 가능한 자료형을 입력 받아
# 자료형의 각 항목에 대해 첫 번째 인자로 전달 받은 함수를 적용한 결과를 맵 객체로 반환
# 출력
# ['A', 'B', 'C', 'D', 'E', 'F']
# ----------------------------------------
# data = list("abcdef")
# answer = list(map(lambda x: x.upper(), data))
# print(answer)
##############################

# 9. 내장함수
# 27. 가장 큰 수와 가장 작은 수 구하기.
# max(), min()
# [10,25,30,45,50]
# 출력
# 50
# 10
# ----------------------------------------
# data = [10,25,30,45,50]
# print(max(data))
# print(min(data))
##############################

# 9. 내장함수
# 27. 2씩 늘어나기
# range()
# 출력
# [0, 2, 4, 6, 8]
# ----------------------------------------
# print(list(range(0, 10, 2)))
##############################

# 9. 내장함수
# 28. [3,8,12,2,5,11] 오름차순, 내림차순 정렬하기
# sorted() - 반복 가능한 자료형을 인자로 전달받아 항목들로부터
# 정렬된 리스트를 반환하는 함수
# 출력
# [2, 3, 5, 8, 11, 12]
# [12, 11, 8, 5, 3, 2]
# ----------------------------------------
# a = [3,8,12,2,5,11]
# print(sorted(a))
# print(list(reversed(sorted(a))))
##############################

# 9. 내장함수
# 29. 
# zip() - 둘 이상의 반복 가능한 자료형을 인자로 전달받아,
# 동일 위치의 항목을 묶어 튜플을 항목으로 구성하는 zip객체를 생성하는 함수
# 출력
# [(1, 4), (2, 5), (3, 6)]
# [(1, 4, 'a'), (2, 5, 'b'), (3, 6, 'c')]
# ----------------------------------------
# a = [1,2,3]
# b = [4,5,6]
# c= ["a", "b", "c"]
# answer = list(zip(a,b))
# print(answer)
# answer = list(zip(a,b,c))
# print(answer)
##############################