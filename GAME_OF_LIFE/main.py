import pygame
import random

pygame.init()

# color scheme of the frame 
black = (0, 0, 0)
grey = (128, 128, 128)
yellow = (255, 255, 0)

# basic setting of the frame 
width, height = 800, 800
tile_size = 20
grid_width = width // tile_size 
grid_height = height // tile_size
FPS = 60

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

def gen(num):
    return set([(random.randrange(0, grid_height), random.randrange(0, grid_width)) for i in range(num)])

def draw_grid(positions):
    # for creating boxes when we click 
    for position in positions:
        col, row = position
        top_left = (col * tile_size, row * tile_size)
        pygame.draw.rect(screen, yellow, (*top_left, tile_size, tile_size))
    # rows divider
    for row in range(grid_height):
        pygame.draw.line(screen, black, (0, row * tile_size), (width, row * tile_size))
    # col divider
    for col in range(grid_width):
        pygame.draw.line(screen, black, (col * tile_size, 0), (col * tile_size, height))

def adjust_grid(positions):
    all_neighbour = set()
    new_positions = set()

    for position in positions:
        neighbour = get_neighbours(position, positions)
        all_neighbour.update(neighbour)

        neighbour = list(filter(lambda x: x in positions, neighbour))

        if len(neighbour) in [2, 3]:
            new_positions.add(position)
    
    for position in all_neighbour:
        neighbour = get_neighbours(position, positions)
        neighbour = list(filter(lambda x: x in positions, neighbour))

        if len(neighbour) == 3:
            new_positions.add(position)

    return new_positions

def get_neighbours(position, positions):
    x, y = position
    neighbour = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if x + dx < 0 or x + dx >= grid_width or y + dy < 0 or y + dy >= grid_height:
                continue
            if dx == 0 and dy == 0:
                continue
        
            neighbour.append((x + dx, y + dy))

    return neighbour

def main():
    running = True
    playing = False
    count = 0 
    update_freq = 120

    positions = set()
    while running: 
        clock.tick(FPS)

        if playing:
            count += 1
        
        if count >= update_freq:
            count = 0 
            positions = adjust_grid(positions)

        pygame.display.set_caption("playing" if playing else "paused")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // tile_size
                row = y // tile_size
                position = (col, row)

                if position in positions:
                    positions.remove(position)
                else:
                    positions.add(position)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing 

                if event.key == pygame.K_c:
                    positions = set()
                    playing = False
                    count = 0

                if event.key == pygame.K_g:
                    positions = gen(random.randrange(2, 5) * grid_width)  

        screen.fill(grey)
        draw_grid(positions)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
