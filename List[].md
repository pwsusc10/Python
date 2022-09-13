# <span style = "color : ">리스트</span>

## <span style = "color : orange">리스트에 데이터 추가</span>
```python
number = [10, 20, 30]
alpabet = ["Aa", "Cc", "Dd"]
print(number)
print(alpabet)
```
[10, 20, 30]  
['Aa', 'Cc', 'Dd']
## <span style = "color : orange">"Cc"가 몇번째 index인가?</span>
```python
print(alpabet.index("Cc"))
```
1
## <span style = "color : orange">"Bb"를 "Cc"와 "Dd"사이에 추가하기</span>
```python
alpabet.insert(1, "Bb")
print(alpabet)
```
['Aa', 'Bb', 'Cc', 'Dd']
## <span style = "color : orange">"Dd" 뒤에 "Aa" 추가하기</span>
```python
alpabet.append("Aa")
print(alpabet)
```
['Aa','Bb', 'Cc', 'Dd', 'Aa']
## <span style = "color : orange">"Aa" index가 몇개나 있는가?</span>
```python
print(alpabet.count("Aa"))
```
2
## <span style = "color : orange">뒤에 index 빼기</span>
```python
print(alpabet.pop())
print(alpabet)
```
Aa  
['Aa', 'Bb', 'Cc', 'Dd']

## <span style = "color : orange">정렬하기</span>
```python
num_list = [5, 2, 4, 1, 3]
num_list.sort()
print(num_list)
```
[1, 2, 3, 4, 5]
## <span style = "color : orange">역순으로 정렬할기</span>
```python
num_list.reverse()
print(num_list)
```
[5, 4, 3, 2, 1]
## <span style = "color : orange">리스트 비우기</span>
```python
num_list.clear()
print(num_list)
```
[]
## <span style = "color : orange">다양한 자료형과 함께 사용하기</span>
```python
mix_list = ["Aa", 10, True]
print(mix_list)
```
['Aa', 10, True]
## <span style = "color : orange">리스트 확장</span>
```python
mix_list = ["Aa", 10, True]
num_list = [11, 22, 33]

num_list.extend(mix_list)
print(num_list)
```
[11, 22, 33, 'Aa', 10, True]