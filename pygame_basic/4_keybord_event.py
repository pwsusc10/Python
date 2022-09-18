import pygame

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("My game")

# 배경 이미지 불러오기
background = pygame.image.load("/Users/hongsungpyo/Desktop/Code/Python/pygame_1.py/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("/Users/hongsungpyo/Desktop/Code/Python/pygame_1.py/character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해온다
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = (screen_width - character_width) / 2 # 화면 가로의 절반에 위치
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임 진행중이 아님

        if event.type == pygame.KEYDOWN: # 키라 눌러졌는가?
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x = to_x - 5
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x = to_x + 5
            elif event.key == pygame.K_UP: # 캐릭터를 위쪽으로
                to_y = to_y - 5
            elif event.key == pygame.K_DOWN: # 캐릭터를 아래쪽으로
                to_y = to_y + 5

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    # 캐릭터 이동
    character_x_pos = character_x_pos + to_x
    character_y_pos = character_y_pos + to_y

    #캐릭터가 스크린 범위를 넘어가지 못하게 범위 제한
    if character_x_pos < 0: #가로
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0: # 세로
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    screen.blit(background, (0,0)) # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos))


    pygame.display.update() # 게임 화면 다시 그리기(중요)

#프로그램 종료
pygame.quit()