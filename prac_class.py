from random import *


# 일반 유닛
class Unit:
    # 생성자, 객체 생성시 자동 실행
    def __init__(self, name, hp=10, speed=10):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))
        
    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다 [속도 {2}]"\
            .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
        self.hp -= damage
        if self.hp <= 0:
            print("{0} : 파괴되었습니다".format(self.name))

# 공격 유닛, Unit 클래스 상속
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage=damage
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"마린", 40, 1, 5)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용할 수 없습니다.".format(self.name))

class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self,"탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print("{0} : 시즈모드를 해제합니다".format(self.name))
            self.damage /= 2
            self.seize_mode = False          


class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2} ]"\
            .format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

     # Unit 클래스 메소드 오버라이딩
    def move(self, location):
        self.fly(self.name, location) # 오버라이딩

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False
    
    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹 모드를 해제합니다".format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹 모드로 설정 합니다".format(self.name))
            self.clocked = True


class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #pass # 아무것도 안하고 일단 넘어간다

        ''' 부모 클래스로 초기화 방법 두가지 '''
        #Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)   # 이 방법은 첫번째 상속 클라스 생성자 실행
        self.location = location
        

def game_start():
    print("Game Start")

def game_over():
    print("Player : gg")
    print("[Player]님이 게임에서 퇴장하셨습니다.")

game_start()

attack_units = list()
for i in range(3):
    attack_units.append(Marine())
    attack_units.append(Tank())
    attack_units.append(Wraith())

Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

for unit in attack_units:
    unit.move("1시")

for unit in attack_units:
    unit.attack("1시")

for unit in attack_units:
    unit.damaged(randint(5,21)) # 5~20의 데미지를 랜덤으로 받음

game_over()



''' 테스트 '''
wraith1 = Unit("종이비행기", 10, 10)
wraith2 = Unit("종이비행기")
wraith2.clocking = True
#print(wraith1.clocking) # 확장된 객체의 멤버는 그 객체에만 적용된다.
print(wraith2.clocking)
