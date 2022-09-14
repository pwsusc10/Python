# <span style = "color : ">클래스</span>
## <span style = "color : yellow">클래스 선언</span>
```python
class Unit :
    def __init__(self, name, hp, damage): # __init__ : 생성자
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 데미지 {1}".format(self.hp, self.damage))

marine = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
```
마린 유닛이 생성 되었습니다.  
체력 40, 데미지 5  
탱크 유닛이 생성 되었습니다.  
체력 150, 데미지 35
## <span style = "color : yellow">멤버 변수 접근</span>
```python
# 멤버 변수 접근
print("유닛 이름은 : {0}이며 공격력은 : {1}입니다".format(marine.name, marine.damage))
```
유닛 이름은 : 마린이며 공격력은 : 5입니다
## <span style = "color : yellow">멤버 변수 추가</span>
```python
# 멤버 변수 추가
marine.defense = 10
print("유닛 이름은 : {0}이며 방어력은 : {1}입니다".format(marine.name, marine.defense))
```
유닛 이름은 : 마린이며 방어력은 : 10입니다
## <span style = "color : yellow">상속</span>
```python
class Unit :
    def __init__(self, name, hp): # __init__ : 생성자
        self.name = name
        self.hp = hp

class AttackUnit(Unit) :
    def __init__(self, name, hp, damage): # __init__ : 생성자
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다.[공격력 : {2}]".format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp = self.hp - damage
        print("남은 체력은 {0} 입니다.".format(self.hp))
        if self.hp <= 0:
            print("유닛이 파괴되었습니다.")


#다중 상속

class Flyable():
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "5시")
```