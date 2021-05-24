# 518 
# a,b,c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)
# sum = (a+b+c)
# avg = (a+b+c)/3
# print("sum : %d" %(sum))
# print("avg : %d" %(avg))

# 525
# a,b,c = input().split()
# answer = ""
# if a>b and a>c:
#     answer += "1"
# else :
#     answer += "0"
# answer += " "
# if a==b and b==c:
#     answer += "1"
# else:
#     answer += "0"
# print(answer)

# 7. for - 반복
# 14. for문을 이용해 아래와 같이 별(*)을 표시하는 프로그램을 만드십시오.
# 출력
#     *
#    **
#   ***
#  ****
# *****
# answer = ""
# for i in range(5):
#     for j in range(5-i-1):
#         answer+=" "
#     for l in range(i+1):
#         answer += "*"
#     answer+= "\n"
# print(answer[:-1])

# 7. for - 반복
# 13. 다음의 결과와 같이 어떤 한 양의 정수를 입력하여 그 숫자에 0~9가 몇 번 사용되었는지 표시하십시오.
# 입력
# 11
# 출력
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 0 0 0 0 1 0 1
# a = input()
# answer =[0,0,0,0,0,0,0,0,0,0]
# for i in range(len(a)):
#     # if a[i] == 0:
#     #     answer[0] += 1
#     # elif a[i] == 1:
#     #     answer[1] += 1
#     # elif a[i] == 2:
#     #     answer[2] += 1
#     answer[int(a[i])] += 1
# for i in answer:
#     print(i)
# print(answer)

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
# def game(a, b, aA, bB):
#     if aA == '가위':
#         if bB == '가위':
#             print("비겼습니다.")
#         elif bB == '바위':
#             print("%s(이)가 이겼습니다."%(b)) 

# a = input()
# b = input()
# aA = input()
# bB = input()
# game(a,b,aA,bB)