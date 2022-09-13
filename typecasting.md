# <span style = "color : ">자료구조 변경</span>
## <span style = "color : orange">자료형 확인</span>
```python
menu = {"떡볶이", "라면", "김밥"}
print(menu, type(menu))
```
{'라면', '김밥', '떡볶이'} <class 'set'>
## <span style = "color : orange">자료형 변환</span>
```python
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))
```
{'떡볶이', '라면', '김밥'} <class 'set'>  
['떡볶이', '라면', '김밥'] <class 'list'>  
('떡볶이', '라면', '김밥') <class 'tuple'>  