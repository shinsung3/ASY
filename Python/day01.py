# 1. 6240
# 1부터 100사이의 숫자 중 3의 배수의 총합을 for 문을 이용해 출력하십시오.
# sum = 0
# for i in range(100):
#     if i%3==0:
#         sum+=i
# print(sum)


# 2. 다음은 10명의 학생들의 혈액형(A, B, AB, O) 데이터입니다.
# ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
# for 문을 이용하여 각 혈액형 별 학생수를 구하십시오.
# arr = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
# a = 0
# b = 0
# o = 0
# ab = 0
# for i in arr:
#     if i=='A':
#         a+=1
#     elif i=='B':
#         b+=1
#     elif i=='O':
#         o+=1
#     else:
#         ab+=1
# print("{'A': %d, 'O': %d, 'B': %d, 'AB': %d}" %(a,o,b,ab))

# 021 문자열 인덱싱
# letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
# letters = 'python'
# print(letters[0], letters[2])

# 022 문자열 슬라이싱
# 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
# license_plate = "24가 2210"
# print(license_plate[-4:])

# 023 문자열 인덱싱
# 아래의 문자열에서 '홀' 만 출력하세요.
# 슬라이싱할 때, 시작 인덱스 : 끝인덱스 : 오프셋
# offset index
# 에서 문자를 추출하는 것을 인덱싱이라 한다.
# string = "홀짝홀짝홀짝"
# print(string[::2]) 

# 024 문자열 슬라이싱
# 문자열을 거꾸로 뒤집어 출력하세요.
# string = "PYTHON"
# print(string[::-1])

# 025 문자열 치환
# 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
# phone_number = "010-1111-2222"
# print(phone_number.replace("-"," "))

# 026 문자열 다루기
# 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
# phone_number = "010-1111-2222"
# print(phone_number.replace("-",""))

# 027 문자열 다루기
# url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
# url = "http://sharebook.kr"
# print(url[-2:])

# 028 문자열은 immutable
# 아래 코드의 실행 결과를 예상해보세요.
# lang = 'python'
# lang[0] = 'P'
# print(lang)
# 문자열은 수정 X
# 실행 결과를 확인해보면 문자열이 할당(assignment) 메서드를 지원하지 않음을 알 수 있습니다.

# 029 replace 메서드
# 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
# string = 'abcdfe2a354a32a'
# print(string.replace("a","A"))

# 030 replace 메서드
# 아래 코드의 실행 결과를 예상해보세요.
# string = 'abcd'
# string.replace('b', 'B')
# print(string)