# print('다음은 이형기 시인의 "낙화"의 한 구절이다.\n-1연\n\t가야할 때 언제인가를\n\t분명히 알고 가는 이의\n\t뒷모습은 얼마나 아름다운가.\n\n나는 이시를 보며 \'나는 내가 가야할 때가 언제일까?\'를 생각해 보았다.')

# book = 1
# total = 10
# guide = '현재 보유 중인 총 책의 수는 다음과 같습니다.'
# print(guide)
# print(int(book) * total)

# changes = '그 중, 대여중인 책을 제외한 책의 수는 다음과 같습니다.'
# rental = 3.0
# print(changes)
# print(total - int(rental))

# authors = {
#     '작자 미상',
#     '이항복',
#     '임제',
#     '임제',
#     '조성기',
#     '조성기',
#     '조성기',
#     '임제',
#     '허균',
#     '허균',
#     '허균',
#     '임제',
#     '임제',
#     '임제',
#     '임제',
#     '임제',
#     '임제',
#     '임제',
#     '임제',
#     '임제',
#     '임제',
#     '박지원',
#     '이항복',
#     '남영로',
#     '남영로',
#     '남영로',
#     '이항복',
#     '임제',
#     '임제',
# }

# print(authors)


# zero_list=[0]
# print(zero_list)
# many_zero_list=[0]*250000
# length=len(many_zero_list)
# print(length)
# numbers=list(range(1, 11))
# print(numbers)
# print(numbers[3:])

# author_1 = '권필'
# author_2 = '허균'
# book_1 = '주생전'
# book_2 = '홍길동전'

# print(f'{book_1}의 작가는 {author_1}이고,\n{author_2}은 {book_2}를 집필하였다.')

# data={'과목':'Python','구분':'실습','단계':int(2),'문제번호':int(3251),'이름':None,'일차':int(22)}
# print(data)
# data={'과목':'Python','구분':'실습','단계':'2'+'단계','문제번호':int(3251),'이름':'딕셔너리 활용하기','일차':int(22)}
# data['일차']-=20
# print(data)

# books = ['광문자전', '유연전', '심청전', '홍길동전', '수성지']
# authors = ['작자 미상', '허균', '박지원', '이항복', '임제']

# print(f'{authors[1]} : {books[3]}\n{authors[3]} : {books[1]}\n{authors[0]} : {books[2]}\n{authors[2]} : {books[0]}\n{authors[4]} : {books[4]}')

# books = ['광문자전', '유연전', '심청전', '홍길동전', '수성지']
# authors = ['작자 미상', '허균', '박지원', '이항복', '임제']

# print(f'{authors[1]} : {books[3]}\n{authors[3]} : {books[1]}\n{authors[0]} : {books[2]}\n{authors[2]} : {books[0]}\n{authors[4]} : {books[4]}')


# data = [{'has_more': False,
#   'next_cursor': None,
#   'object': 'list',
#   'page_or_database': {},
#   'request_id': 'a5163fff-758f-45ea-b6fb',
#   'results': [{'archived': False,
#                'cover': None,
#                'created_by': {'object': 'user'},
#                'created_time': '2023-06-15T04:29:00.000Z',
#                'icon': None,
#                'last_edited_by': {'object': 'user'},
#                'last_edited_time': '2023-12-12T09:19:00.000Z',
#                'object': 'page',
#                'parent': {'type': 'database_id'},
#                'properties': {'setNum': {'id': '%7DK%40%5C',
#                                          'number': 1,
#                                          'type': 'number'},
#                               '과목': {'id': 'YuIE',
#                                      'multi_select': [{'color': 'default',
#                                                        'name': 'Python'}],
#                                      'type': 'multi_select'},
#                               '구분': {'id': '%40%3EmR',
#                                      'select': {'color': 'purple',
#                                                 'name': '실습'},
#                                      'type': 'select'},
#                               '단계': {'id': 'T%7B%7BP',
#                                      'select': {'color': 'default',
#                                                 'name': '3'},
#                                      'type': 'select'},
#                               '문제번호': {'id': 'uEBt',
#                                        'number': 1431,
#                                        'type': 'number'},
#                               '제목': {'id': 'title',
#                                      'title': [{'annotations': {'bold': False,
#                                                                 'code': False,
#                                                                 'color': 'default',
#                                                                 'italic': False,
#                                                                 'strikethrough': False,
#                                                                 'underline': False},
#                                                 'href': None,
#                                                 'plain_text': '복잡한 자료구조',
#                                                 'text': {'content': '복잡한 자료구조',
#                                                          'link': None},
#                                                 'type': 'text'}],
#                                      'type': 'title'},
#                               '일차': {'id': 'nWnH',
#                                      'number': '2',
#                                      'type': 'number'},
#                               '커리큘럼': {'id': 'T%3AR_',
#                                        'multi_select': [{'color': 'default',
#                                                          'name': 'fundamentals-of-python'}],
#                                        'type': 'multi_select'}},
#                'public_url': None
#             }],
#   'type': 'page_or_database'}]


# # '일차', '단계', '과목' key에 해당하는 값을 찾아서 할당
# title_value = data[0]['results'][0]['properties']['제목']['title'][0]['plain_text']
# ilcha_value = data[0]['results'][0]['properties']['일차']['number']
# danha_value = data[0]['results'][0]['properties']['단계']['select']['name']
# gosoek_value = data[0]['results'][0]['properties']['과목']['multi_select'][0]['name']

# # 결과 출력
# first_data={'제목':title_value, '일차':ilcha_value,'단계':danha_value, '과목':gosoek_value}
# print(first_data)

# information = dict()
# authors = ['김시습', '허균', '남영로', '작자 미상', '임제', '박지원']
# books = [
#     ['장화홍련전', '가락국 신화', '온달 설화'],
#     ['금오신화', '이생규장전', '만복자서포기'],
#     ['수성지', '백호집', '원생몽유록'],
#     ['홍길동전', '장생전', '도문대작'],
#     ['옥루몽', '옥련몽'],
# ]

# information={
#     authors[1]:books[4],
#     authors[4]:books[2]
# }

# print(information)

# backup_catalog = [
#     ['시간의 틈', '반짝임의 어둠', '망각의 경계'],
#     ['연기의 수수께끼', '장면의 고백', '드라마의 그림자'],
#     ['황금의 칼날', '비열한 간신', '무명의 영웅'],
#     ['성공의 열쇠', '내면의 변화', '목표의 달성'],
# ]

# catalog = [
#     ['시간의 틈', '반짝임의 어둠', '망각의 경계'],
#     ['연기의 수수께끼', '장면의 고백', '드라마의 그림자'],
#     ['황금의 칼날', '비열한 간신', '무명의 영웅'],
#     ['성공을 향한 한 걸음', '내 삶의 변화', '목표의 달성의 비밀'],
# ]


# ''' 
# 도서 제목 '성공의 열쇠', '내면의 변화', '목표의 달성' 을 각각
# '성공을 향한 한 걸음', '내 삶의 변화', '목표 달성의 비밀' 가 되도록 변경하시오.
# '''

# print('catalog와 backup_catalog를 비교한 결과')
# # 식별 연산자로 catalog와 backup_catalog를 비교한 결과를 출력하시오.
# print(backup_catalog is catalog)

# print('backup_catalog : ')
# print(backup_catalog)
# print()

# print('catalog : ')
# print(catalog)


# authors = ['김시습', '허균', '남영로', '작자 미상', '임제', '박지원']
# books = [
#     ['장화홍련전', '가락국 신화', '온달 설화'],
#     ['금오신화', '이생규장전', '만복자서포기'],
#     ['수성지', '백호집', '원생몽유록'],
#     ['홍길동전', '장생전', '도문대작'],
#     ['옥루몽', '옥련몽'],
# ]

# information1={authors[0] : books[1]}
# information2={authors[1] : books[3]}
# information3={authors[2] : books[4]}
# information4={authors[3] : books[0]}
# information5={authors[4] : books[2]}

# print(information1)
# print(information2)
# print(information3)
# print(information4)
# print(information5)