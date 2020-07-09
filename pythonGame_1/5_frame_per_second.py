# pygame 패키지가 잘 설치됬는지 확인
import pygame

pygame.init()   # 반드시 해야함

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode(
        (screen_width, screen_height)
    )

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")

# 배경 이미지 불러오기
background = pygame.image.load("background.png")

# FPS
clock = pygame.time.Clock()

# 캐릭터(스프라이터) 불러오기
character = pygame.image.load("character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 세로크기 가장 아래에

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6


# 창이 꺼지지 않기 위해서 이벤트 루프
running = True # 게임이 진행 중인지 확인
while running :
    dt = clock.tick(60) # fps
    print(dt)
    print("fps : " + str(clock.get_fps()))
    # 10fps -> 1초에 10번 동작, 한번에 : x *10이동
    # 20fps -> 1초에 20번 동작, 한번에 : x *20이동
    # fps때문에 캐릭터의 속도가 달라지면 안된다.

    ## 배경 그리기
    screen.blit(background, (0,0)) #screen.fill((122,10,122))
    # 캐릭터 그리기
    screen.blit(character, (character_x_pos, character_y_pos))

    # 게임 화면을 다시 그리기( 계속 해야함 )
    pygame.display.update()

    # 어떤 이벤트가 발생?
    for event in pygame.event.get():
        # 창이 닫히는 이벤트가 발생?
        if event.type == pygame.QUIT:
            running = False

        # 키가 눌러 졌는지 확인
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        # 키를 때면
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
        
        # character_x_pos += to_x
        # character_y_pos += to_y

    # 캐릭터 이동, 프레임 별 속도 보정
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 화면 벗어남 방지
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    


    


# pygame 종료
pygame.quit()