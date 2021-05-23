# 06. 다음의 결과와 같이 입력된 영어 알파벳 문자에 대해 대소문자를 구분하는 코드를 작성하십시오.
# 입력
# b
# 출력
# b 는 소문자 입니다.
# a = input()
# if a>='a' and a <='z':
#     print("소문자")

# 07. 1~200 사이의 정수 가운데 7의 배수이면서 5의 배수는 아닌 모든 숫자들을 찾아
# 콤마(,)로 구분된 문자열을 구성해 출력하는 프로그램을 작성하십시오.
# 출력
# 7,14,21,28,42,49,56,63,77,84,91,98,112,119,126,133,147,154,161,168,182,189,196
# ----------------------------------------
# answer = ""
# for i in range(1,201):
#     if i%7 == 0 and i%5 !=0:
#         answer += (str(i)+",")
# print(answer)
# print(answer[:-1]) 
# print(answer[:-7])

# a = [88, 30, 61, 55, 95]
# print(len(a)) #a.length()
# print(a[1])
# print(a[5])

# for문의 range()쓰는 방법
# for i in range(len(a)): #range(len(a)) #range(0, len(a)),  #for (int i=0; i<a.length(); i++)

# 09. 1부터 100사이의 숫자 중 홀수를 for 문을 이용해 다음과 같이 출력하십시오.
# 출력
# 1, 3, 5, 7, 9, ... 95, 97, 99
# answer = ""
# for i in range(1,101):
#     if i%2==1:
#         answer += (str(i) +", ")
# print(answer[:-1]) # answer[: -1]

# 11. 다음은 학생의 점수를 나타내는 리스트입니다.
# [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
# while 문과 리스트 객체의 pop()을 이용해 80점 이상의 점수들의 총합을 구하시오.
# 출력
# 454
# ----------------------------------------
# a = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
# while 
# pop() # 하나씩 뽑아내는거.
# sum = 0
# while len(a) >0:
#     b = a.pop()
#     if b >=80:
#         sum += b
#     print(a)
# print(sum)

# answer = ""
# for i in range(5):
#     for j in range(5-i):
#         answer +="*"
#     answer += "\n"
# print(answer[:-1])

# 15. 다음의 결과와 같이 반목문을 이용해 단어의 순서를 거꾸로 해 반환하는 함수를 작성하고
# 그 함수를 이용해 회문(앞뒤 어느 쪽에서도 같은 단어, 말) 여부를 판단하는 코드를 작성하십시오.
# 입력
# eye
# 출력
# eye
# 입력하신 단어는 회문(Palindrome)입니다.
def palindrome(a): # public int function(int a, int c){} #eyed
    word = a[::-1]
    print(word)
    if word == a:
        print(a)
        print("입력하신 단어는 회문(Palindrome)입니다.")
a = input()
palindrome(a)