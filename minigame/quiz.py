import pygame
import random
###########################################################
# 기본 초기화

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("My game")

#FPS
clock = pygame.time.Clock()
###########################################################

# 1. 사용자 게임 초기화(배경 화면, 게임 이미지, 좌표, 폰트 등)

# 배경 화면 지정
back_img = pygame.image.load("minigame/back_img.png")

# 캐릭터 위치와 크기 지정
dog = pygame.image.load("minigame/dog.png")
dog_size = dog.get_rect().size
dog_width = dog_size[0]
dog_height = dog_size[1]
dog_x_pos = (screen_width - dog_width) / 2
dog_y_pos = screen_height - dog_height

ddong = pygame.image.load("minigame/ddong.png")
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = 0
ddong_y_pos = 0

# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)

# 총 시간
total_time = 15

# 시작 시간
start_ticks = pygame.time.get_ticks() # 시작 tick을 받아옴


#캐릭터 이동 속도 및 이동 좌표
dog_speed = 0.5
to_char_x = 0
to_char_y = 0

# 장애물 낙하 속도
to_ddong_y = 0.5

running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(30) # 게임화면의 초당 프레임 수를 설정
    
    # 2. 이벤트 처리

    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임 진행중이 아님

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_char_x -= dog_speed
            elif event.key == pygame.K_RIGHT:
                to_char_x += dog_speed
        
        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_char_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_char_y = 0
    
    
    # 3. 게임 캐릭터 위치 정의
    # 캐릭터 이동
    dog_x_pos = dog_x_pos + to_char_x * dt
    dog_y_pos = dog_y_pos + to_char_y * dt
    
    if dog_x_pos < 0: #가로
        dog_x_pos = 0
    elif dog_x_pos > screen_width - dog_width:
        dog_x_pos = screen_width - dog_width
    
    # 장애물 이동
    ddong_y_pos = ddong_y_pos + to_ddong_y * dt

    if ddong_y_pos >= screen_height:
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0, screen_width - ddong_width)
   
    # 4. 충돌 처리
    dog_rect = dog.get_rect()
    dog_rect.left = dog_x_pos
    dog_rect.top = dog_y_pos

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    # 충돌 체크
    if dog_rect.colliderect(ddong_rect):
        print("충돌")
        running = False     


    # 5. 화면에 그리기
    screen.blit(back_img, (0,0)) # 배경 그리기

    screen.blit(dog, (dog_x_pos, dog_y_pos))

    screen.blit(ddong, (ddong_x_pos, ddong_y_pos))

    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 초로 나타내기 위해 1000을 곱함

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (0, 0, 0))
    # 출력할 글자, True, 글자 색상
    screen.blit(timer, (10, 10))

    # 만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False

    pygame.display.update() # 게임 화면 다시 그리기(중요)

#프로그램 종료
pygame.quit()