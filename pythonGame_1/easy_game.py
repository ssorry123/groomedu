''' 간단한 똥피하기 게임 '''
import pygame
import random


''' 게임 필수 세팅 '''
# 반드시 해야함
pygame.init()
# 화면 크기 설정
screen_width = 1000
screen_height = 640
screen = pygame.display.set_mode(
        (screen_width, screen_height)
    )


''' 게임 기본 세팅 '''
# 화면 타이틀 설정
pygame.display.set_caption("똥피하기 Game")
# 배경 이미지 불러오기
background = pygame.image.load("background_easygame.png")
# 게임 시간 설정
total_time = 150


''' 주인공 캐릭터 설정 '''
# 캐릭터(스프라이터) 불러오기
character = pygame.image.load("character.png")
character_size = character.get_rect().size # 이미지의 크기 구하기
character_width = character_size[0]
character_height = character_size[1]
# 시작 위치
character_x_pos = (screen_width / 2) - (character_width / 2) 
character_y_pos = screen_height - character_height 

character_to_x = 0      # 이동할 좌표, 좌우로만 이동
character_speed = 0.5   # 이동 속도


''' 똥 캐릭터 설정 '''
# 똥이 여러개 떨어지게 만듬.
class DDong:
    ddong = list()

    def __init__(self, image_path):
        self.enemy = pygame.image.load("enemy.png")
        enemy_size = self.enemy.get_rect().size
        self.enemy_width = enemy_size[0]
        self.enemy_height = enemy_size[1]
        # 시작 x 위치는 랜덤
        self.enemy_x_pos = random.randint(0, screen_width - self.enemy_width)
        self.enemy_y_pos = 0
        self.enemy_to_y = 0
        self.enemy_speed = 0.13

    # 똥 생성
    @classmethod
    def make_ddongs(cls):
        for i in range(1):
            cls.ddong.append(DDong('enemy.png'))
        return cls.ddong

    # 똥 추가
    @classmethod
    def add_ddongs(cls):
        amount = random.randint(1,3)
        for i in range(amount):
            cls.ddong.append(DDong('enemy.png'))
        return cls.ddong

    @classmethod
    def get_ddong_ea(cls):
        return len(cls.ddong)
    

''' 게임 시작 전 세팅 '''
ddong_list = DDong.make_ddongs()        # 처음 똥 만들기
clock = pygame.time.Clock()             # FPS
game_font = pygame.font.Font(None, 40)  # 폰트 객체 설정 (폰트, 크기)


''' 게임 실행 '''
running = True                          # 게임 탈락 여부
boom = False                            # 똥과 충돌 여부
count = 0                               # 피한 똥 개수
start_ticks = pygame.time.get_ticks()   # 시작 시간
ex_character_to_x = 0                   # space로 멈춘 후 다시 움직일 방향
addDDong = 1                            # 난이도 증가 변수
while running :
    # 남은 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000   # ms / 1000
    eta_time = (int)(total_time - elapsed_time)
    if eta_time < 0 :
        running = False
        continue
    timer = game_font.render('eta : ' + (str)(eta_time), True, (255,255,255))
    
    # 피한 똥 개수 계산 
    counter = game_font.render((str)(count), True,(255,0,0))

    # 난이도 계산, 똥의 개수
    stage = game_font.render('stage'+ (str)(DDong.get_ddong_ea()), True, (0,255,0))

    ''' drawing '''
    # 배경 그리기
    screen.blit(background, (0,0)) #screen.fill((122,10,122))
    # 캐릭터 그리기
    screen.blit(character, (character_x_pos, character_y_pos))
    # 똥 그리기
    for ddong in ddong_list:
        screen.blit(ddong.enemy, (ddong.enemy_x_pos, ddong.enemy_y_pos))
    # 타이머 , 카운터 , 난이도그리기
    screen.blit(timer,(10, 10))
    screen.blit(counter,(500,10))
    screen.blit(stage,(900,10))
    # 게임 화면을 다시 그리기( 계속 해야함 )
    pygame.display.update()

    # 충돌 하였는가?
    if boom == True:
        running = False
        continue

    
    ''' event 처리'''
    for event in pygame.event.get():
        # 창이 닫히는 이벤트가 발생
        if event.type == pygame.QUIT:
            running = False
            break

        # key down
        # 한번 방향키를 누르면 그 방향으로 계속 움직인다.
        if event.type == pygame.KEYDOWN:
            # +=, -=이 아니므로 가속하지 않는다.
            if event.key == pygame.K_LEFT:                
                ex_character_to_x = character_to_x = -character_speed
            elif event.key == pygame.K_RIGHT:
                ex_character_to_x = character_to_x = +character_speed
            # space를 누르면 멈춘다
            elif event.key == pygame.K_SPACE:
                character_to_x = 0
        if event.type == pygame.KEYUP:
            # space를 때면 움직이던 방향으로 다시 움직인다
            if event.key == pygame.K_SPACE:
                character_to_x = ex_character_to_x
         
        # key up
        # 있으면 방향키를 때면 머춘다
        '''
        if event.type == pygame.KEYUP:
            # 왼쪽 또는오른쪽을 누르다가 때면 멈춘다.
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
        '''

    # fps, fps별 속도 보정
    dt = clock.tick(60)

    ''' 캐릭터 위치 정보 업데이트 '''
    # 한번 방향키를 눌렀으면 계속 그 방향으로 움직인다
    character_x_pos += character_to_x * dt
    # 캐릭터 화면 벗어남 방지
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width


    ''' 똥 위치 정보 업데이트 '''
    # 시간이 지날수록 난이도를 증가시킨다.
    # 특정 정수 남은 시간이 여러번 실행되므로 아래와 같이 처리
    if (int)(elapsed_time) / 5 == addDDong:
        ddong_list = DDong.add_ddongs()
        print(elapsed_time)
        addDDong += 1
    
    for ddong in ddong_list:
        # 똥마다 떨어지는 속도는 랜덤
        ddong.enemy_y_pos += ddong.enemy_speed * random.randint(1,4) * dt
        #ddong.enemy_y_pos += ddong.enemy_speed * dt
        
        # 똥이 바닥에 도착하면
        if ddong.enemy_y_pos > screen_height:
            # x위치는 랜덤으로 다시 정함
            ddong.enemy_x_pos = random.randint(0, screen_width - ddong.enemy_width)
            # y위치는 꼭대기로
            ddong.enemy_y_pos = 0
            # 피한 똥 회수 증가
            count += 1


    ''' 특정 이벤트(똥과 충돌) 처리 '''
    # 캐릭터, 적 충돌 처리를 위한 정보
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    for ddong in ddong_list:
        ddong.enemy_rect = ddong.enemy.get_rect()
        ddong.enemy_rect.left = ddong.enemy_x_pos
        ddong.enemy_rect.top = ddong.enemy_y_pos
    # 충돌 처리
    # 사각형 기준으로 충돌을 하였는가?
    for ddong in ddong_list:
        if character_rect.colliderect(ddong.enemy_rect):
            print("충돌")
            boom = True


    
''' 게임 종료 '''
pygame.time.delay(2000)
pygame.quit()