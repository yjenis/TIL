# a1=1
# a2=2.3
# a3=2 + 3j
# a4='hello'
# a5=True
# a6=[1,2,3]
# a7=(1,2,3)
# a8=range(1,4)
# a9={1,2,3}
# a10={'apple':2, 'banana':3}
# a11=None
# a12=lambda x,y:x + y

# for i in range(1,13):
#     var=f'a{i}'
#     var=eval(var)
#     print(type(var))
    
# 7//3
# 7%3
# 7%2.3

# my_list=[1,2,3]
# sum=0

# for i in my_list:
#     sum +=i
#     print(sum)

# 변수X의 메모리 주소는 어떤 값을 할당하더라도 같을까?
# 1. 변수를 선언 -> 표현식을 평가 -> 메모리 주소를 생성 
# 2. 그 메모리 주소를 변수에 저장
    
# x=36.5
# print(id(x))

# x=22.1
# print(id(x))

# fruits={'apple':4,
#         'banana':3,
#         'melon':7}

# my_list=[[1.2,3,4,5],
#          [6,7,8,9,10],
#          [11,12,13,14,15]]

# def dfs_people():
    
    
# def a():
#     pass

# def b():
#     pass

# a = []

# for i in range(10):
#     a.append(i)
    
# print(a[10])

# int: 정수형
# decimal = 10
# binary = bin(decimal)
# print(binary)

# octal = oct(decimal)[2:]
# print(octal)

# hexa = hex(decimal)[2:]
# print(hexa)

#float: 실수형
#부동 소수점 -> 컴퓨터의 용량이 한정돼있음 : Floating point rounding error

# a = 3.2 - 3.1
# b = 1.2 - 1.1
# #print(a)
# #print(b)

# #print(abs(a-b)<-1e-10)
# # import math
# # #math.isclose(a, b): 두 숫자가 거의 같은지 여부를 판단하는 메서드
# # print(math.isclose(a,b))

# num_a = f'{a:.1f}'
# num_b = f'{b:.1f}'
# print(num_a)
# print(num_b)

#우리가 부동소수점을 출력할 때 f-string 포맷팅을 사용하여 정확도를 제어할 수 있다.

# print(314e-2)
# print(314*10**-2)

# f-string 포맷팅
# n=2/3
# print(f'{n:.2f}')
# n2=3
# print(f'{n2}')
# str1='hello'
# print(f'{str1}')

# print(2/3)

# Sequence type(시퀀스 자료형)
# str(문자열) : 불변 시퀀스 자료형
# 리스트: 가변 시퀀스 자료형
# -> sw역량 테스트 1. 문자열 파싱 vs 2. 방향 배열

# 변수[start:end:step] -> step은 생략 가능
# : start부터 end-1까지 step만큼 증감(step이 생략시 1씩 증가)

# greeting = 'hello world'

# # 실습1. 인덱싱 -> 알파벳 w를 출력해 보세요.
# print(greeting[6])

# # 실습2-1. 슬라이싱 -> hello를 출력해 보세요.
# print(greeting[:5])

# # 실습2-2. 슬라이싱 -> world를 출력해 보세요.
# print(greeting[6:])

# # 실습2-3. 슬라이싱 -> 문자열을 거꾸로 출력해 보세요.
# print(greeting[::-1])

# # 실습3. 내장함수(매서드)를 사용하여 문자열의 길이를 출력해 보세요.
# print(len(greeting))

# print('안녕하세요')
# print('랄랄라')

# print('안녕하세요\n랄랄라')
# print('안녕하세요\t랄랄라')

#입력 받는 법!!
# char = input()
# num = int(input())
# num = int(input('숫자 한개를 입력하세요.'))
# char1, char2 = input().split()
# num1, num2 = map(int, input().split())
# num_list = list(map(int, input().split()))

#리스트 컴프리헨션 -> 2차원 리스트를 한줄로 입력받는 법

#포맷팅 : 파이썬에서는 3가지 방법이 있다. -> 우리가 자주 쓰는 건 f-string
name = input()
age = int(input())
height = float(input())
print("저의 이름은 %s, 나이는 %d, 키는 %.2f 입니다." %(name, age, height))
print("저의 이름은 {}, 나이는 {}, 키는 {:.2f} 입니다." .format(name, age, height))
print(f"저의 이름은 {name},나이는{age},키는{height:.2f}입니다.")