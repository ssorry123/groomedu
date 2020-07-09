# pygame 패키지가 잘 설치됬는지 확인
import pygame

pygame.init()   # 반드시 해야함

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode(
        (screen_width, screen_height)
    )

# 배경 이미지 불러오기
background = pygame.image.load("background.png")

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")

# 창이 꺼지지 않기 위해서 이벤트 루프
running = True # 게임이 진행 중인지 확인
while running :
    ## 배경 그리기
    screen.blit(background, (0,0))
    #screen.fill((122,10,122))
    
    # 게임 화면을 다시 그리기( 계속 해야함 )
    pygame.display.update()

    # 어떤 이벤트가 발생?
    for event in pygame.event.get():
        # 창이 닫히는 이벤트가 발생?
        if event.type == pygame.QUIT:
            running = False
    


# pygame 종료
pygame.quit()