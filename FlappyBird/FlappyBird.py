import pygame
from random import randint
# khởi tạo game
pygame.init()
# đặt kích thước cho màn hình game
screen = pygame.display.set_mode((400,600))
# đặt tiêu đề cho game
pygame.display.set_caption("plappyBird")
clock = pygame.time.Clock()
# quy định màu (r,g,b) -> (red, green, blue) = màu trắng
# seach google -> rgb color selector
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
#  biến pause
pausing = False
# đặt tọa độ vị trí cho con chim
x_bird = 50
y_bird = 350
# đặt vị trí các ống 
tube1_x = 400
tube2_x = 600
tube3_x = 800
tube_with = 50
tube1_height = randint(100,400)
tube2_height = randint(100,400)
tube3_height = randint(100,400)
d2_tube = 150
# biến đánh giá chim qua ống
tube1_pass = False
tube2_pass = False
tube3_pass = False
# biến khoảng các các ống
tube_velocity = 2
# tạo điểm, taoh font 
score = 0
font = pygame.font.SysFont('san', 20)
# tạo font kết thúc game
font1 = pygame.font.SysFont('san', 40)
# thêm vị trí rơi của chim
bird_drop_velocity = 0
# biến động lực khi chim rơi
gravity = 0.5
# thêm ảnh các ống vào 
tube_img = pygame.image.load("tube.png")
tube_op_img = pygame.image.load("tube_op.png")
# thêm ảnh nền cho game vị trí (0,0)
background_img = pygame.image.load("background.png")
# gán kích thước cho ảnh nền 
background_img = pygame.transform.scale(background_img,(400,600))
# gán ảnh con chim vào
bird_img = pygame.image.load("bird.png")
bird_img = pygame.transform.scale(bird_img, (35,35))
# thêm âm thanh vào game
sound = pygame.mixer.Sound('no6.wav')
#  thêm ảnh cát vào
sand_img = pygame.image.load("sand.png")
sand_img = pygame.transform.scale(sand_img, (400,30))
running = True
while running:
    # chơi nhạc
    pygame.mixer.Sound.play(sound)
    # nháy 60 lần trong 1 giây, nếu không có thì sẽ nháy với tốc độ bằng tốc độ lớn nhất của máy tính, sẽ làm tăng %CPU rất nhanh
    clock.tick(60)
    screen.fill(WHITE)
    # vẽ ảnh nền ra màn hình ở vị trí (0,0)
    screen.blit(background_img, (0,0))
    # ép ảnh ống và vẽ ống
    tube1_img = pygame.transform.scale(tube_img,(tube_with, tube1_height))
    tube1 = screen.blit(tube1_img, (tube1_x,0))
    tube2_img = pygame.transform.scale(tube_img,(tube_with, tube2_height))
    tube2 = screen.blit(tube2_img, (tube2_x,0))
    tube3_img = pygame.transform.scale(tube_img,(tube_with, tube3_height))
    tube3 = screen.blit(tube3_img, (tube3_x,0))
    # ép ảnh và vẽ ảnh ống đối diện 
    tube1_op_img = pygame.transform.scale(tube_op_img,(tube_with, 600 - tube1_height + d2_tube))
    tube1_op = screen.blit(tube1_op_img, (tube1_x,tube1_height + d2_tube))
    tube2_op_img = pygame.transform.scale(tube_op_img,(tube_with, 600 - tube2_height + d2_tube))
    tube2_op = screen.blit(tube2_op_img, (tube2_x,tube2_height + d2_tube))
    tube3_op_img = pygame.transform.scale(tube_op_img,(tube_with, 600 - tube3_height + d2_tube))
    tube3_op = screen.blit(tube3_op_img, (tube3_x,tube3_height + d2_tube))
    # ống di chuyển 
    tube1_x -= tube_velocity
    tube2_x -= tube_velocity
    tube3_x -= tube_velocity
    # vẽ lại ống sau khi di chuyển, đặt lại giá trị tube123_pass = False đẻ tính điểm
    if tube1_x < -tube_with:
        tube1_x = 550
        tube1_height = randint(100,400)
        tube1_pass = False
    if tube2_x < -tube_with:
        tube2_x = 550
        tube2_height = randint(100,400)
        tube2_pass = False
    if tube3_x < -tube_with:
        tube3_x = 550
        tube3_height = randint(100,400)
        tube3_pass = False
    
    # vẽ cát
    sand = screen.blit(sand_img, (0, 570))
    # vẽ ảnh con chim ra màn hình
    bird = screen.blit(bird_img, (x_bird, y_bird))
    # chim rơi
    y_bird = y_bird + bird_drop_velocity
    bird_drop_velocity = bird_drop_velocity + gravity
    # ghi điểm ra màn hình
    score_txt = font.render("Scroe : " + str(score), True, RED)
    screen.blit(score_txt,(5,5))
    # cộng điểm khi chim qua ống, 
    if tube1_x + tube_with <= x_bird and tube1_pass == False:
        score +=1
        tube1_pass = True
    if tube2_x + tube_with <= x_bird and tube2_pass == False:
        score +=1
        tube2_pass = True
    if tube3_x + tube_with <= x_bird and tube3_pass == False:
        score +=1
        tube3_pass = True
    # kiểm tra sự va chạm chim và ống 
    tubes = [tube1, tube2, tube3,tube1_op, tube2_op, tube3_op, sand]
    for tube in tubes:
         if bird.colliderect(tube): # colliderect() hàm kiểm tra va chạm giữa 2 vật thể
            #  dừng nhạc 
            pygame.mixer.pause()
            tube_velocity = 0 # tốc dộ ộng bằng 0
            bird_drop_velocity = 0  #tốc đọ chim = 0
            game_over_txt = font1.render("Game over, Score : " + str(score), True, RED)
            screen.blit(game_over_txt,(85,260))
            space_txt = font.render("Press Space to continue! " , True, BLUE)
            screen.blit(space_txt,(120,290))
            pausing = True

    # kiểm tra sự kiện nút bấm
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # chim bay lên
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_drop_velocity = 0
                bird_drop_velocity -= 7
                # if pausing:
                #     # chơi lại nhạc
                #     pygame.mixer.unpause()
                #     # đặt tọa độ vị trí cho con chim
                #     x_bird = 50
                #     y_bird = 350
                #     # đặt vị trí các ống 
                #     tube1_x = 400
                #     tube2_x = 600
                #     tube3_x = 800
                #     tube_velocity = 2
                #     score = 0
                #     pausing = False
            if event.key == pygame.K_q:
                if pausing:
                    # chơi lại nhạc
                    pygame.mixer.unpause()
                    # đặt tọa độ vị trí cho con chim
                    x_bird = 50
                    y_bird = 350
                    # đặt vị trí các ống 
                    tube1_x = 400
                    tube2_x = 600
                    tube3_x = 800
                    tube_velocity = 2
                    score = 0
                    pausing = False
    # lệnh hiển thị màn hình 
    pygame.display.flip()
# sau khi chạy xong chương trình sẽ xóa hết dữ liệu cho đỡ nặng máy
pygame.quit()
