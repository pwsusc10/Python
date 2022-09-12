# <span style = "color : ">집합</span>
### <span style = "color : yellow">중복이 안되며 순서가 없다</span>
### <span style = "color : orange">집합 선언</span>
```
my_set = {1, 2, 3, 3, 3, 4, 5}
print(my_set)
```
{1, 2, 3, 4, 5}
### <span style = "color : orange">합집합</span>
```
print(red_team | blue_team)
print(red_team.union(blue_team))
```
{'영희', '민석', '철수', '미희'}  
{'영희', '민석', '철수', '미희'}
### <span style = "color : orange">교집합</span>
```
red_team = {"철수", "영희", "민석"}
blue_team = {"민석", "미희"}

print(red_team & blue_team)
print(red_team.intersection(blue_team))
```
{'민석'}  
{'민석'}
### <span style = "color : orange">차집합</span>
```
print(red_team - blue_team)
print(red_team.difference(blue_team))
```
{'철수', '영희'}  
{'철수', '영희'}
### <span style = "color : orange">원소 추가</span>
```
red_team.add("정민")
print(red_team)
```
{'철수', '민석', '정민', '영희'}
### <span style = "color : orange">원소 제거</span>
```
red_team.remove("철수")
print(red_team)
```
{'민석', '정민', '영희'}