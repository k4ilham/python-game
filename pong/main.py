import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
width = 800
height = 600

# Warna
white = (255, 255, 255)
black = (0, 0, 0)

# Pengaturan layar
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong')

# Kecepatan permainan
clock = pygame.time.Clock()
fps = 60

# Ukuran paddle
paddle_width = 10
paddle_height = 100

# Ukuran bola
ball_size = 10

# Posisi paddle
paddle1_x = 20
paddle1_y = height // 2 - paddle_height // 2
paddle2_x = width - paddle_width - 20
paddle2_y = height // 2 - paddle_height // 2

# Kecepatan paddle
paddle_speed = 10

# Posisi bola
ball_x = width // 2 - ball_size // 2
ball_y = height // 2 - ball_size // 2
ball_dx = 5 * random.choice((1, -1))
ball_dy = 5 * random.choice((1, -1))

# Skor
score1 = 0
score2 = 0

# Font
font = pygame.font.SysFont(None, 50)

# Fungsi untuk menggambar paddle
def draw_paddle(x, y):
    pygame.draw.rect(screen, white, [x, y, paddle_width, paddle_height])

# Fungsi untuk menggambar bola
def draw_ball(x, y):
    pygame.draw.rect(screen, white, [x, y, ball_size, ball_size])

# Fungsi untuk menggambar skor
def draw_score(score, x, y):
    text = font.render(str(score), True, white)
    screen.blit(text, (x, y))

# Fungsi utama
def game_loop():
    global paddle1_y, paddle2_y, ball_x, ball_y, ball_dx, ball_dy, score1, score2

    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and paddle1_y > 0:
            paddle1_y -= paddle_speed
        if keys[pygame.K_s] and paddle1_y < height - paddle_height:
            paddle1_y += paddle_speed
        if keys[pygame.K_UP] and paddle2_y > 0:
            paddle2_y -= paddle_speed
        if keys[pygame.K_DOWN] and paddle2_y < height - paddle_height:
            paddle2_y += paddle_speed

        ball_x += ball_dx
        ball_y += ball_dy

        if ball_y <= 0 or ball_y >= height - ball_size:
            ball_dy = -ball_dy

        if (ball_x <= paddle1_x + paddle_width and paddle1_y <= ball_y <= paddle1_y + paddle_height) or (ball_x >= paddle2_x - ball_size and paddle2_y <= ball_y <= paddle2_y + paddle_height):
            ball_dx = -ball_dx

        if ball_x <= 0:
            score2 += 1
            ball_x = width // 2 - ball_size // 2
            ball_y = height // 2 - ball_size // 2
            ball_dx = 5 * random.choice((1, -1))
            ball_dy = 5 * random.choice((1, -1))
        
        if ball_x >= width - ball_size:
            score1 += 1
            ball_x = width // 2 - ball_size // 2
            ball_y = height // 2 - ball_size // 2
            ball_dx = 5 * random.choice((1, -1))
            ball_dy = 5 * random.choice((1, -1))

        screen.fill(black)
        draw_paddle(paddle1_x, paddle1_y)
        draw_paddle(paddle2_x, paddle2_y)
        draw_ball(ball_x, ball_y)
        draw_score(score1, width // 4, 20)
        draw_score(score2, width * 3 // 4, 20)
        pygame.display.flip()

        clock.tick(fps)

    pygame.quit()
    quit()

# Mulai permainan
game_loop()
