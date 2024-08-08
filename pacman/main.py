import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pac-Man")

# Warna
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Ukuran blok
block_size = 20

# Labirin
maze = [
    "############################",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#.####.#####.##.#####.####.#",
    "#.####.#####.##.#####.####.#",
    "#..........................#",
    "#.####.##.########.##.####.#",
    "#.####.##.########.##.####.#",
    "#......##....##....##......#",
    "######.##### ## #####.######",
    "######.##### ## #####.######",
    "######.##          ##.######",
    "######.## ###  ### ##.######",
    "######.## ######## ##.######",
    "       ## ######## ##       ",
    "######.## ######## ##.######",
    "######.## ######## ##.######",
    "######.##          ##.######",
    "######.## ######## ##.######",
    "######.## ######## ##.######",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#.####.#####.##.#####.####.#",
    "#...##................##...#",
    "###.##.##.########.##.##.###",
    "###.##.##.########.##.##.###",
    "#......##....##....##......#",
    "#.##########.##.##########.#",
    "#.##########.##.##########.#",
    "#..........................#",
    "############################"
]

# Posisi awal Pac-Man
pacman_x = 1
pacman_y = 1

# Fungsi untuk menggambar labirin
def draw_maze():
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == "#":
                pygame.draw.rect(screen, BLUE, pygame.Rect(x * block_size, y * block_size, block_size, block_size))
            elif maze[y][x] == ".":
                pygame.draw.circle(screen, WHITE, (x * block_size + block_size // 2, y * block_size + block_size // 2), block_size // 4)

# Fungsi utama game
def main():
    global pacman_x, pacman_y

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if maze[pacman_y][pacman_x - 1] != "#":
                pacman_x -= 1
        if keys[pygame.K_RIGHT]:
            if maze[pacman_y][pacman_x + 1] != "#":
                pacman_x += 1
        if keys[pygame.K_UP]:
            if maze[pacman_y - 1][pacman_x] != "#":
                pacman_y -= 1
        if keys[pygame.K_DOWN]:
            if maze[pacman_y + 1][pacman_x] != "#":
                pacman_y += 1

        screen.fill(BLACK)
        draw_maze()
        pygame.draw.circle(screen, YELLOW, (pacman_x * block_size + block_size // 2, pacman_y * block_size + block_size // 2), block_size // 2)
        pygame.display.flip()
        clock.tick(10)

if __name__ == "__main__":
    main()
