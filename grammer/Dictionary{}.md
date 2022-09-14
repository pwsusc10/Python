# <span style = "color : ">사전</span>

## <span style = "color : orange">사전에 데이터 추가</span>
```python
dictionary = {1 : "철수", 2 : "영희", "Aa" : "Michael"}
print(dictionary)
print(dictionary[1])
print(dictionary[2])
print(dictionary["Aa"])
```
{1 : '철수', 2 : '영희', 'Aa' : 'Michael'}  
철수  
영희  
Micheal
## <span style = "color : orange">잘못된 index에 접근</span>
```python
print(dictionary[100])
```
KeyError : 100
## <span style = "color : orange">오류 메시지 수정</span>
```python
print(dictionary.get(100))
print(dictionary.get(100, "사전에 없습니다"))
```
None  
사전에 없습니다
## <span style = "color : orange">사전에 있는 지 확인</span>
```python
print(3 in dictionary)
print(1 in dictionary)
```
False  
True
## <span style = "color : orange">사전 update와 추가</span>
```python
dictionary[2] = "순자"
dictionary["Bb"] = "John"
print(dictionary)
```
{1 : '철수', 2 : '순자', 'Aa' : 'Michael', 'Bb' : 'John'}
## <span style = "color : orange">index 삭제</span>
```python
del dictionary["Bb"]
print(dictionary)
```
{1 : '철수', 2 : '순자', 'Aa' : 'Michael'}
## <span style = "color : orange">key들만 출력</span>
```python
print(dictionary.keys())
```
dict_keys([1, 2, 'Aa'])
## <span style = "color : orange">value들만 출력</span>
```python
print(dictionary.values())
```
dict_values(['철수', '순자', 'Michael'])
## <span style = "color : orange">key,value같이 출력</span>
```python
print(dictionary.items())
```
dict_items([(1, '철수'), (2, '순자'), ('Aa', 'Michael')])
## <span style = "color : orange">사전 초기화</span>
```python
dictionary.clear()
print(dictionary)
```
{}