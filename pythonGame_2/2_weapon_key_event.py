''' 간단한 똥피하기 게임 '''
import pygame
import random
import os

''' 게임 필수 세팅 '''
# 반드시 해야함
pygame.init()
# 화면 크기 설정
screen_width = 640 
screen_height = 480
screen = pygame.display.set_mode(
        (screen_width, screen_height)
    )


''' 게임 기본 세팅 '''
# 화면 타이틀 설정
pygame.display.set_caption("Nado Pang")
# 배경 이미지 불러오기
background = pygame.image.load("./image/background.png")
# 스테이지 이미지 불러오기
stage = pygame.image.load("./image/stage.png")
stage_size = stage.get_rect().size
stage_height = stage_size[1]    # stage 높이 계산

# 게임 시간 설정
total_time = 150


''' 주인공 캐릭터 설정 '''
# 캐릭터(스프라이터) 불러오기
character = pygame.image.load("./image/character.png")
character_size = character.get_rect().size # 이미지의 크기 구하기
character_width = character_size[0]
character_height = character_size[1]
# 시작 위치
character_x_pos = (screen_width / 2) - (character_width / 2) 
character_y_pos = screen_height - character_height  - stage_height
# 이동 조작
character_to_x = 0      # 좌우로만 이동
character_speed = 5     # 캐릭터 속도

''' 무기 설정 '''
weapon = pygame.image.load("./image/weapon.png")
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapon_speed = 10

weapons = list()


''' 게임 시작 전 세팅 '''
clock = pygame.time.Clock()             # FPS
game_font = pygame.font.Font(None, 40)  # 폰트 객체 설정 (폰트, 크기)

''' 게임 실행 '''
running = True                          # 게임 탈락 여부
start_ticks = pygame.time.get_ticks()   # 시작 시간
kdown_right = False
kdown_left = False
while running :
    # 남은 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000   # ms / 1000
    eta_time = (int)(total_time - elapsed_time)
    if eta_time < 0 :
        running = False
        continue
    timer = game_font.render('eta : ' + (str)(eta_time), True, (255,255,255))
    

    ''' drawing '''
    # 배경 그리기
    screen.blit(background, (0,0)) #screen.fill((122,10,122))
    # 무기 그리기
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    # stage 그리기
    screen.blit(stage, (0 , screen_height - stage_height))
    # 캐릭터 그리기
    screen.blit(character, (character_x_pos, character_y_pos))

    # 게임 화면을 다시 그리기( 계속 해야함 )
    pygame.display.update()



    ''' event 처리'''
    for event in pygame.event.get():
        # 창이 닫히는 이벤트가 발생
        if event.type == pygame.QUIT:
            running = False
            break
        
        # key down, char_pos setting
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:         # 좌이동
                kdown_left = True
                #kdown_right = False
                character_to_x = -character_speed
            elif event.key == pygame.K_RIGHT:      # 우이동
                kdown_right = True
                #kdown_left = False
                character_to_x = +character_speed
            elif event.key == pygame.K_SPACE:      # space
                weapon_x_pos = character_x_pos + character_width/2 - weapon_width/2
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])
        # key up, setting flag
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                kdown_left = False
            elif event.key == pygame.K_RIGHT:
                kdown_right = False
        # char_pos setting with flag
        if (kdown_left == False) and (kdown_right == False):
            character_to_x = 0
        elif (kdown_left == False) and (kdown_right == True):
            character_to_x = character_speed
        elif (kdown_left == True) and (kdown_right == False):
            character_to_x = -character_speed
        
    print((str)(kdown_left) + " " + (str)(kdown_right))
    # fps, fps별 속도 보정
    dt = clock.tick(60)

    ''' 캐릭터 위치 정보 업데이트 '''
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    ''' 무기 정보 업데이트 '''
    # 무기가 위로 날라감
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons ]
    # 무기가 천장에 닿으면 사라짐
    # 조건에 맞는 것만 저장한다.
    weapons = [ [w[0], w[1]] for w in weapons if w[1]>0]


    ''' 특정 이벤트(똥과 충돌) 처리 '''
   


    
''' 게임 종료 '''
pygame.time.delay(200)
pygame.quit()