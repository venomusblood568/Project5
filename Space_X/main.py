import pygame
import time
import random

pygame.font.init()

WIDTH, HEIGHT = 1000, 800

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SPACE_X")

BG = pygame.transform.scale(pygame.image.load("new.jpeg"), (WIDTH, HEIGHT))

PLAYER_WIDTH, PLAYER_HEIGHT = 40, 60
PLAYER_VEL = 5

BALL_RADIUS = 15
BALL_VEL = 3

FONT = pygame.font.SysFont("comicsans", 30)

# Load player image
player_img = pygame.image.load("spaceship2.png").convert_alpha()
player_img = pygame.transform.scale(player_img, (PLAYER_WIDTH, PLAYER_HEIGHT))

def draw(player, elapsed_time, balls):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    WIN.blit(player_img, player.topleft)  # Draw player image

    for ball_pos in balls:
        pygame.draw.circle(WIN, (169, 169, 169), ball_pos, BALL_RADIUS)  # Grey balls

    pygame.display.update()

def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    ball_add_increment = 2000
    ball_count = 0
    balls = []

    hit = False

    while run:
        ball_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if ball_count > ball_add_increment:
            for _ in range(3):
                ball_x = random.randint(BALL_RADIUS, WIDTH - BALL_RADIUS)
                ball_y = -BALL_RADIUS
                balls.append([ball_x, ball_y])

            ball_add_increment = max(200, ball_add_increment - 50)
            ball_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        for ball_pos in balls[:]:
            ball_pos[1] += BALL_VEL
            if ball_pos[1] > HEIGHT:
                balls.remove(ball_pos)
            elif player.colliderect(pygame.Rect(ball_pos[0] - BALL_RADIUS, ball_pos[1] - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)):
                balls.remove(ball_pos)
                hit = True
                break

        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH // 2 - lost_text.get_width() // 2, HEIGHT // 2 - lost_text.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, balls)

    pygame.quit()

if __name__ == "__main__":
    main()
