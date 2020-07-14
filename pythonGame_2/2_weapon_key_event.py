''' 간단한 똥피하기 게임 '''
import pygame
import random
import os

''' 게임 필수 세팅 '''
class NadoGame:
	def __init__(self):
		# 초기화
		pygame.init()
		# 화면 설정
		self.screen_width = 640
		self.screen_height = 480
		self.screen = pygame.display.set_mode(
			(self.screen_width, self.screen_height)
		)
		pygame.display.set_caption("Nado Pang")
		self.background = pygame.image.load("./image/background_1.png")
		self.stage = pygame.image.load("./image/stage.png")
		self.stage_size = self.stage.get_rect().size
		self.stage_height = self.stage_size[1]
		
		self.total_time = 150

class Unit:
	def __init__(self, image_path):
		self.image = pygame.image.load(image_path)	# 이미지 경로
		self.size = self.image.get_rect().size		# 이미지 크기
		self.width = self.size[0]						# 이미지 너비
		self.height = self.size[1]					# 이미지 높이

class Character(Unit):
	def __init__(self, image_path):
		# 이미지 설정
		Unit.__init__(self, image_path)
		# 시작위치 설정
		self.x_pos = myGame.screen_width/2 - self.width/2
		self.y_pos = myGame.screen_height - self.height - myGame.stage_height
		# 움직임 설정
		self.to_x = 0
		self.speed = 5
		
class Weapon(Unit):
	weapons = list()
	def __init__(self, image_path):
		Unit.__init__(self,image_path)
		self.speed = 13
		

myGame = NadoGame()
character = Character("./image/character.png")
weapon = Weapon("./image/weapon.png")



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
    eta_time = (int)(myGame.total_time - elapsed_time)
    if eta_time < 0 :
        running = False
        continue
    timer = game_font.render('eta : ' + (str)(eta_time), True, (255,255,255))
    

    ''' drawing '''
    # 배경 그리기
    myGame.screen.blit(myGame.background, (0,0)) #screen.fill((122,10,122))
    # 무기 그리기
    for weapon_x_pos, weapon_y_pos in weapons:
        myGame.screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    # stage 그리기
    myGame.screen.blit(myGame.stage, (0 , myGame.screen_height - myGame.stage_height))
    # 캐릭터 그리기
    myGame.screen.blit(character.image, (character.x_pos, character.y_pos))

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
                character.to_x = -character.speed
            elif event.key == pygame.K_RIGHT:      # 우이동
                kdown_right = True
                #kdown_left = False
                character.to_x = +character.speed
            elif event.key == pygame.K_SPACE:      # space
                weapon_x_pos = character.x_pos + character.width/2 - weapon_width/2
                weapon_y_pos = character.y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])
        # key up, setting flag
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                kdown_left = False
            elif event.key == pygame.K_RIGHT:
                kdown_right = False
        
        # char_pos setting with flag, 기존 코드 개선 부분
        if (kdown_left == False) and (kdown_right == False):
            character.to_x = 0
        elif (kdown_left == False) and (kdown_right == True):
            character.to_x = character.speed
        elif (kdown_left == True) and (kdown_right == False):
            character.to_x = -character.speed
        
    print((str)(kdown_left) + " " + (str)(kdown_right))
    # fps, fps별 속도 보정
    dt = clock.tick(60)

    ''' 캐릭터 위치 정보 업데이트 '''
    character.x_pos += character.to_x

    if character.x_pos < 0:
        character.x_pos = 0
    elif character.x_pos > myGame.screen_width - character.width:
        character.x_pos = myGame.screen_width - character.width

    ''' 무기 정보 업데이트 '''
    # 무기가 위로 날라감
    # w[1] --> weapon_y_pos
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons ]
    # 무기가 천장에 닿으면 사라짐
    # 조건에 맞는 것만 저장한다.
    weapons = [ [w[0], w[1]] for w in weapons if w[1]>0]


    ''' 특정 이벤트(똥과 충돌) 처리 '''
   


    
''' 게임 종료 '''
pygame.time.delay(200)
pygame.quit()
