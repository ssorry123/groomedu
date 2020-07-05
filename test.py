class Unit:
    # 생성자, 객체 생성시 자동 실행
    def __init__(self, name, hp=10, damage=10):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine = Unit("마린")
goast = Unit("고스트", 30)
tank = Unit("탱크", 50, 250)