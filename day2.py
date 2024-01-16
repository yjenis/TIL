# print(bool(0))
# print(bool(5))
# print(bool(8))
# print(bool(-3))
# print(bool(3.8))

# print(bool(''))
# print(bool('1'))
# print(bool('a'))
# print(bool('2.3'))

# and -> 둘 다 참이면 참 -> 왼쪽 항이 True 더라도 오른쪽 항까지 확인
# or -> 둘 중 하나라도 참이면 참 -> 왼쪽 항이 True가 나오면 오른쪽 항까지 확인X

#복합 연산자의 예시 1부터 10까지
# sum_v = 0
# for i in range(1, 11):
#     sum_v+=i
    
# print(sum_v)

# 로또 6번호 추천 list tuple set 중 뭘써야 할까?
# set 중복 허용 안 하니까
# list 오름차순으로 정렬할 수 있음

# num1 = 1
# num2 = 2.3
# str1 = '1'
# n = input() -> 만약 정수 3을 입력했다. 이 경우 데이터 타입은 무엇일까? -> 문자
# 정수로 입력 받고 싶으면 
# n=int(input()) 혹은 map함수 활용


#리스트: 가변 시퀀스 자료형

MAP = []
Matrix = []
array = [[1, 2, 3], 
         [4, 5, 6], 
         [7, 8, 9]]

#실습1. 인덱싱하여 3을 출력해 보세요
print(array[0][2])

#실습2. 인덱싱하여 7을 출력해 보세요
print(array[2][0])

#실습3. 슬라이싱하여 [2,3]을 출력해 보세요.
print(array[0][1:3])


