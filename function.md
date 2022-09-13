# <span style = "color : ">함수</span>
## <span style = "color : orange">가변 인자</span>
매개 변수에 *를 붙여 사용  
end = " "는 다음 출력이 줄바꿈을 하지 않은 채 출력하도록 함
```python
def coffeeshop(name, location, *menu):
    print("가게 이름 : {0} 위치 : {1}" .format(name, location), end = " ")
    for coffee in menu :
        print(coffee, end = " ")
    print()

coffeeshop("cafe1", "대한민국", "아메리카노", "카페라떼")
coffeeshop("cafe2", "미국", "아이스티", "꿀물", "초코라떼")
```
가게 이름 : cafe1 위치 : 대한민국 아메리카노 카페라떼  
가게 이름 : cafe2 위치 : 미국 아이스티 꿀물 초코라떼 

## <span style = "color : orange">전역 변수</span>
global을 붙여 사용
```python
donut = 10

def leftover(children):
    global donut
    donut = donut - children
    return donut

print("도넛 총 갯수 : {0}" .format(donut))
leftover(3)
print("남은 도넛 수 : {0}" .format(donut))
```
도넛 총 갯수 : 10  
남은 도넛 수 : 7