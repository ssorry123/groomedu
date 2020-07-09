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

# 캐릭터(스프라이터) 불러오기
character = pygame.image.load("character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 세로크기 가장 아래에


# 창이 꺼지지 않기 위해서 이벤트 루프
running = True # 게임이 진행 중인지 확인
while running :
    ## 배경 그리기
    screen.blit(background, (0,0))
    #screen.fill((122,10,122))
    
    # 캐릭터 그리기
    screen.blit(character, (character_x_pos, character_y_pos))


    # 게임 화면을 다시 그리기( 계속 해야함 )
    pygame.display.update()
    # 어떤 이벤트가 발생?
    for event in pygame.event.get():
        # 창이 닫히는 이벤트가 발생?
        if event.type == pygame.QUIT:
            running = False
    


# pygame 종료
pygame.quit()