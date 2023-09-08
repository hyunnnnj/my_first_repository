#강의안 2-2 변수와 데이터 타입
""" my_var = 10
print(my_var)  

my_list = [1, 2, 3]
print(*my_list) #실제 값(주소에 들어있는 값) 접근(포인터 느낌) >> 1 2 3 출력
print(my_list) #[1, 2, 3] 출력
 """

#숫자
""" # 정수
my_int = 10 #int) 4byte

# 부동 소수점
my_float = 3.14 #float) 8byte

# 복소수
my_complex = 3 + 4j """

#문자
""" my_character = 'A'
my_char = "@"
print(my_character)
print(my_char) """

#문자열
""" my_string = 'Hello, World!'
str_name = "python" """

#불리언
""" my_bool = True
bFlag = False """

#--------------리스트--------------
""" my_list = [1, 2, 'three', True] #여러가지 데이터타입 저장 가능
lsElement = [3.14, "b", 'two', False] """

#리스트 활용
""" my_list = [10, 3, 8, 9, 42, "hello"]
print(*my_list)

print(my_list.__len__()) # ==len(my_list)

print(my_list[3]) #3번 인덱스에 있는 값 출력 >> 9 >> *(아스트릭크)붙이는 거랑 비슷(실제 값 가져오기)

#다른 리스트,변수에 원래 있던 리스트의 값 중 하나 넣기
list_el = my_list[2]
print(list_el) """

#요소변경
""" my_list[3] = 11
print(my_list) """

#연산
""" n_add = my_list[3] + my_list[2]
print(n_add)
print(my_list[3] - my_list[5]) #데이터 타입이 안 맞기때문에 오류남
 """
 
#슬라이싱
""" slice_ls = my_list[2:5]
print(slice_ls)
print(my_list[2:5]) #2번 인덱스에서 5번인덱스 전까지 출력(==2~4번 인덱스 출력)
print(my_list[:3]) # == [0:3]
print(my_list[4:]) """

#이중리스트 
""" my_list = [10, 3, 8, 9, 42, "hello", [5, 4, 2, "world"]]
print(my_list)
print(my_list[6][1]) #6번 인덱스의 1번 인덱스 출력 >> 4
print(my_list[6][2:]) #6번 인덱스의 2번 인덱스부터 끝까지 출력 >> [2, 'world]

print(my_list[5][2]) #5번 인덱스 hello의 2번째 글자 l 출력 """

#메소드
""" my_list = [10, 3, 8, 9, 42, 8, "hello"]
print(my_list) """

#.insert(n,a)
""" my_list = [10, 3, 8, 9, 42, 8, "hello"]
my_list.insert(2,4) #2번 인덱스에 4를 넣음 + 원래 2번 인덱스부터 한 칸 씩 뒤로 밀려남
print(*my_list) """

#.index(a)
""" my_list = [10, 3, 8, 9, 42, 8, "hello"]
print(my_list.index(3)) #해당 값이 몇번 인덱스인지  """

#.append(a)
""" my_list = [10, 3, 8, 9, 42, 8, "hello"]
my_list.append(22) #리스트 맨 뒤에 값 추가
print(*my_list) """

#.count(a)
""" my_list = [10, 3, 8, 9, 42, 8, "hello"]
print(my_list.count(8)) #list에 8이 몇개 있는지
print(my_list.count(5)) #5는 없어서 0이라고 뜸 """

#.pop() 마지막 요소 출력 후 삭제

""" my_list = [10, 3, 8, 9, 42, 8, "hello"]
print(my_list)
print(my_list.pop()) #데구개에서 배운 pop이랑 ==
print(*my_list) """

#.sort() 오름차순 정렬
""" my_list = [10, 3, 8, 9, 42, 8]

print(my_list)

my_list.sort()
print(*my_list)

my_list = [10, 3, 8, 9, 42, 8, "hello"]
print(my_list)

my_list.sort()
print(my_list) #데이터 타입 다른게 있어서 오류 """

#.reverse() 역순 정렬
""" my_list = [10, 3, 8, 9, 42, 8, "hello"]
print(my_list)

my_list.reverse()
print(*my_list) """

#extend(list) 두 리스트 결합
""" my_list = [10, 3, 8, 9, 42, 8, "hello"]
list_tmp = [5 ,7 , 'world']
print(my_list,list_tmp)

my_list.extend(list_tmp)
print(*my_list) """

#clear() 리스트 내 값 삭제
""" my_list = [10, 3, 8, 9, 42, 8, "hello"]
list_tmp = [5 , 7, 'world']
print(my_list,list_tmp)

my_list.extend(list_tmp) #두 리스트 합치기
print(*my_list)

list_tmp.clear() #전체 값 삭제
print(list_tmp) """

#remove(a) 해당 값(a) 삭제
""" my_list = [10, 3, 8, 9, 42, 8, "hello"]
print(my_list)

my_list.remove(3) #3 제거
print(*my_list) """

#del list[n] n번 인덱스 제거
""" my_list = [10, 3, 8, 9, 42, 8, "hello"]
print(my_list)

del my_list[2]
print(*my_list) """

#-----------튜플-----------
""" my_tup = (4, 2, 6, 1, "py", "w")
print(my_tup)
print(my_tup.__len__())

#my_tup[2] = 9 #튜플은 값 추가, 삭제 불가능

print(my_tup[2:5])
print(my_tup[1:4])
print(my_tup[:3])
print(my_tup[2:]) """

#이중 튜플
""" my_tup = (4, 2, 6, 1, "py", "w", ("h", 8, 7, 3))
print(my_tup)
print(my_tup[6][0]) """

#메소드
#.index(value, start, end) start부터 end인덱스까지에서 value값의 인덱스 출력
""" my_tup = (4, 2, 6, 1, "py", "w", ("h", 8, 7, 3))
print(my_tup.index(2, 0, 3)) 

print(my_tup.index('py', 3, 5)) 

#print(my_tup.index(1, 0, 3)) #값이 없어서 오류남

#.count(a) a와 같은 요소의 갯수 출력
print(my_tup.count(6)) """

#-------------딕셔너리--------------
""" my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict)
print(*my_dict)

my_item = my_dict.items()
print(my_item) """

#생성
""" idx = {'key1':'value1', 'key2':'value2'}
dicts = dict.fromkeys(idx,"0")
print(dicts) """

#인덱싱
""" my_dict = {'key1': 'value1', 'key2': 'value2'}
dicData = {"name" : "python", "number" : 23564897}
print(my_dict["key1"])

my_dict = {'key1': 'value1', 'key2': 'value2'}
my_str = my_dict.get("key2")
print(my_str)

my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict.pop("key1"))
print(my_dict) """

#복사
""" my_dict = {'key1': 'value1', 'key2': 'value2'}
dicts = my_dict.copy()
print(dicts)
print(my_dict) """

#추가/변경
""" my_dict = {'key1': 'value1', 'key2': 'value2'}
dicData = {"name" : "python", "number" : 23564897}

my_dict['key3'] = 'value3'

print(my_dict)

my_dict = {'key1': 'value1', 'key2': 'value2'}
my_dict.setdefault('key3')
print(my_dict)

my_dict = {'key1': 'value1', 'key2': 'value2'}
my_dict.update({'key1' : 'v4'})
print(my_dict) """

#삭제
""" my_dict = {'key1': 'value1', 'key2': 'value2'}
del my_dict["key2"]
print(my_dict) """

#검색
""" my_dict = {'key1': 'value1', 'key2': 'value2'}
print("key2" in my_dict)
print("key3" in my_dict) """

#변환   
""" my_dict = {'key1': 'value1', 'key2': 'value2'}
my_list = list(my_dict.keys())
print(my_list)

my_list = list(my_dict.values())
print(my_list)

my_dict = {'key1': 'value1', 'key2': 'value2'}
my_set = set(my_dict.keys())
print(my_set)

my_dict = {'key1': 'value1', 'key2': 'value2'}
my_dict.clear()
print(my_dict) """


