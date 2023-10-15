import os
import pygame
from os import listdir
from os.path import isfile, join

pygame.init()

WIDTH, HEIGHT = 1350, 750
FPS = 60
player_velocity = 3
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rusher")


def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]


def load_sprite_sheets(dir1, dir2, width, height, direction=False):
    path = join("assets", dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        if direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "")] = sprites

    return all_sprites


def get_block(size):
    path = join("assets", "Terrain", "Terrain.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(96, 0, size, size)
    surface.blit(image, (0, 0), rect)
    return pygame.transform.scale2x(surface)


class Player(pygame.sprite.Sprite):
    GRAVITY = 1
    SPRITES = load_sprite_sheets("MainCharacters", "MaskDude", 32, 32, True)
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "right"
        self.animation_count = 0
        self.fall_count = 0
        self.jump_count = 0
        self.hit = False
        self.hit_count = 0

    def jump(self):
        self.y_vel = -self.GRAVITY * 8
        self.animation_count = 0
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def make_hit(self):
        self.hit = True

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def loop(self, fps):
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_vel, self.y_vel)

        if self.hit:
            self.hit_count += 1
        if self.hit_count > fps * 2:
            self.hit = False
            self.hit_count = 0

        self.fall_count += 1
        self.update_sprite()

    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0

    def hit_head(self):
        self.count = 0
        self.y_vel *= -1

    def update_sprite(self):
        sprite_sheet = "idle"
        if self.hit:
            sprite_sheet = "hit"
        elif self.y_vel < 0:
            if self.jump_count == 1:
                sprite_sheet = "jump"
            elif self.jump_count == 2:
                sprite_sheet = "double_jump"
        elif self.y_vel > self.GRAVITY * 2:
            sprite_sheet = "fall"
        elif self.x_vel != 0:
            sprite_sheet = "run"

        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.update()

    def update(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)

    def draw(self, win, offset_x):
        win.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))


class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name=None):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name

    def draw(self, win, offset_x):
        win.blit(self.image, (self.rect.x - offset_x, self.rect.y))


class Block(Object):
    def __init__(self, x, y, size, name="block"):
        super().__init__(x, y, size, size)
        block = get_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
        self.name = name


class Fire(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "fire")
        self.fire = load_sprite_sheets("Traps", "Fire", width, height)
        self.image = self.fire["off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "off"

    def on(self):
        self.animation_name = "on"

    def off(self):
        self.animation_name = "off"

    def loop(self):
        sprites = self.fire[self.animation_name]
        sprite_index = (self.animation_count //
                        self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0


def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image


def draw(window, background, bg_image, player, objects, offset_x):
    for tile in background:
        window.blit(bg_image, tile)

    for obj in objects:
        obj.draw(window, offset_x)

    player.draw(window, offset_x)

    pygame.display.update()


def handle_vertical_collision(player, objects, dy):
    collided_objects = []
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            if dy > 0:
                player.rect.bottom = obj.rect.top
                player.landed()
            elif dy < 0:
                player.rect.top = obj.rect.bottom
                player.hit_head()

            collided_objects.append(obj)

    return collided_objects

def collide(player, objects, dx):
    player.move(dx, 0)
    player.update()
    collided_object = None
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            collided_object = obj
            break

    player.move(-dx, 0)
    player.update()
    return collided_object


def handle_move(player, objects, left_wall):
    keys = pygame.key.get_pressed()

    player.x_vel = 0
    collide_left = collide(player, objects, -player_velocity * 2)
    collide_right = collide(player, objects, player_velocity * 2)
    
    # Check collision with the left wall
    for block in left_wall:
        if pygame.sprite.collide_mask(player, block):
            if player.x_vel > 0:  # Moving from right to left
                player.rect.right = block.rect.left  # Move player's right side to the left of the block
            elif player.x_vel < 0:  # Moving from left to right
                player.rect.left = block.rect.right  # Move player's left side to the right of the block
            collide_left = True

    if keys[pygame.K_LEFT] and not collide_left:
        player.move_left(player_velocity)
    if keys[pygame.K_RIGHT] and not collide_right:
        player.move_right(player_velocity)

    vertical_collide = handle_vertical_collision(player, objects, player.y_vel)
    to_check = [collide_left, collide_right, *vertical_collide]

    for obj in to_check:
        if obj and obj.name == "fire":
            player.make_hit()


def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Blue.png")

    block_size = 96

    player = Player(100, 100, 50, 50)
    fire = Fire(260, HEIGHT - block_size - 64, 16, 32)
    fire.on()

    # Create the floor
    floor = [Block(i * block_size, HEIGHT - block_size, block_size)
             for i in range(-WIDTH // block_size, (WIDTH * 10) // block_size)]

    # Create the left wall
    left_wall = [Block(-960, HEIGHT - block_size * (i + 1), block_size, "wall") for i in range(10)]

    # Combine objects including floor, left wall, and fire
    objects = [*floor, *left_wall, Block(0, HEIGHT - block_size * 2, block_size),
            Block(0, HEIGHT - block_size * 2, block_size),
            Block(300, HEIGHT - block_size * 3, block_size),
            Block(500, HEIGHT - block_size * 4, block_size),
            Block(800, HEIGHT - block_size * 5, block_size),
            Block(900, HEIGHT - block_size * 5, block_size),
            Block(1000, HEIGHT - block_size * 6, block_size),
            Block(1100, HEIGHT - block_size * 6, block_size),
            Block(1200, HEIGHT - block_size * 6, block_size),
            Block(1300, HEIGHT - block_size * 6, block_size),
            Block(1400, HEIGHT - block_size * 5, block_size),
            Block(1500, HEIGHT - block_size * 5, block_size),
            Block(1700, HEIGHT - block_size * 3, block_size),
            Block(1800, HEIGHT - block_size * 2, block_size),
            Block(1900, HEIGHT - block_size * 3, block_size),
            Block(2000, HEIGHT - block_size * 2, block_size),
            Block(2100, HEIGHT - block_size * 5, block_size),
            Block(2200, HEIGHT - block_size * 3, block_size),
            Block(2300, HEIGHT - block_size * 4, block_size),
            Block(2400, HEIGHT - block_size * 3, block_size),
            Block(2500, HEIGHT - block_size * 5, block_size),
            Block(2700, HEIGHT - block_size * 2, block_size),
            Block(2800, HEIGHT - block_size * 3, block_size),
            Block(3000, HEIGHT - block_size * 2, block_size),
            Block(3000, HEIGHT - block_size * 3, block_size),
            Block(3000, HEIGHT - block_size * 4, block_size),
            Block(3140, HEIGHT - block_size * 2, block_size),
            Block(3140, HEIGHT - block_size * 3, block_size),
            Block(3140, HEIGHT - block_size * 4, block_size),
            Block(3300, HEIGHT - block_size * 3, block_size),
            Block(3400, HEIGHT - block_size * 2, block_size),
            Block(3500, HEIGHT - block_size * 5, block_size),
            Block(3600, HEIGHT - block_size * 6, block_size),
            Block(3700, HEIGHT - block_size * 3, block_size),
            Block(3700, HEIGHT - block_size * 2, block_size),
            Block(3800, HEIGHT - block_size * 2, block_size),
            # stacking of the three block
            Block(4000, HEIGHT - block_size * 6, block_size),
            Block(4000, HEIGHT - block_size * 5, block_size),
            Block(4000, HEIGHT - block_size * 4, block_size), 
            Block(4100, HEIGHT - block_size * 3, block_size),
            Block(4300, HEIGHT - block_size * 2, block_size),
            Block(4400, HEIGHT - block_size * 3, block_size),
            Block(4500, HEIGHT - block_size * 2, block_size),
            Block(4600, HEIGHT - block_size * 6, block_size),
            Block(4800, HEIGHT - block_size * 5, block_size),
            Block(4900, HEIGHT - block_size * 4, block_size),
            Block(5000, HEIGHT - block_size * 3, block_size),
            Block(5100, HEIGHT - block_size * 3, block_size),  
            Block(5200, HEIGHT - block_size * 6, block_size),                           
            Block(5300, HEIGHT - block_size * 4, block_size),   
            Block(5400, HEIGHT - block_size * 2, block_size), 
            Block(5500, HEIGHT - block_size * 2, block_size),   
            Block(5600, HEIGHT - block_size * 3, block_size),     
            Block(5800, HEIGHT - block_size * 4, block_size),   
            Block(5900, HEIGHT - block_size * 4, block_size),   
            Block(6000, HEIGHT - block_size * 5, block_size),   
            Block(6100, HEIGHT - block_size * 2, block_size),  
            Block(6100, HEIGHT - block_size * 3, block_size), 
            Block(6200, HEIGHT - block_size * 6, block_size),   
            Block(6300, HEIGHT - block_size * 6, block_size),   
            Block(6400, HEIGHT - block_size * 6, block_size),   
            Block(6500, HEIGHT - block_size * 5, block_size),   
            Block(6600, HEIGHT - block_size * 5, block_size),   
            Block(6700, HEIGHT - block_size * 4, block_size),   
            Block(6800, HEIGHT - block_size * 4, block_size),   
            Block(6900, HEIGHT - block_size * 4, block_size),   
            Block(7000, HEIGHT - block_size * 3, block_size),   
            Block(7100, HEIGHT - block_size * 3, block_size),
            Block(7200, HEIGHT - block_size * 3, block_size),
            Block(7300, HEIGHT - block_size * 4, block_size),
            Block(7500, HEIGHT - block_size * 5, block_size),
            Block(7700, HEIGHT - block_size * 6, block_size),
            Block(7800, HEIGHT - block_size * 2, block_size),
            Block(7900, HEIGHT - block_size * 2, block_size),
            Block(7900, HEIGHT - block_size * 3, block_size),
            Block(7800, HEIGHT - block_size * 2, block_size),
            Block(8000, HEIGHT - block_size * 5, block_size),
            Block(8100, HEIGHT - block_size * 5, block_size),
            Block(8200, HEIGHT - block_size * 6, block_size),
            Block(8300, HEIGHT - block_size * 6, block_size),
            Block(8400, HEIGHT - block_size * 7, block_size),
            Block(8500, HEIGHT - block_size * 7, block_size),
            Block(8600, HEIGHT - block_size * 7, block_size),
            Block(8700, HEIGHT - block_size * 3, block_size),
            Block(8800, HEIGHT - block_size * 3, block_size),
            Block(9000, HEIGHT - block_size * 5, block_size),
            Block(9100, HEIGHT - block_size * 5, block_size),
            Block(9200, HEIGHT - block_size * 6, block_size),
            Block(9300, HEIGHT - block_size * 3, block_size),
            Block(9400, HEIGHT - block_size * 2, block_size),
            Block(9500, HEIGHT - block_size * 3, block_size),
            Block(9600, HEIGHT - block_size * 3, block_size),
            Block(9700, HEIGHT - block_size * 4, block_size),
            Block(9800, HEIGHT - block_size * 2, block_size),
            Block(9900, HEIGHT - block_size * 2, block_size),
            Block(10000, HEIGHT - block_size * 5, block_size),
            Block(10100, HEIGHT - block_size * 5, block_size),
            Block(10200, HEIGHT - block_size * 6, block_size),
            Block(10300, HEIGHT - block_size * 6, block_size),
            Block(10400, HEIGHT - block_size * 7, block_size),
            Block(10500, HEIGHT - block_size * 7, block_size),
            Block(10600, HEIGHT - block_size * 6, block_size),
            Block(10700, HEIGHT - block_size * 6, block_size),
            Block(10800, HEIGHT - block_size * 5, block_size),
            Block(10900, HEIGHT - block_size * 5, block_size),
            Block(11000, HEIGHT - block_size * 4, block_size),
            Block(11100, HEIGHT - block_size * 4, block_size),
            Block(11200, HEIGHT - block_size * 5, block_size),
            Block(11300, HEIGHT - block_size * 5, block_size),
            Block(11400, HEIGHT - block_size * 6, block_size),
            Block(11500, HEIGHT - block_size * 7, block_size),
            # everthing is good till here
            #mega_wall 
            Block(11800, HEIGHT - block_size * 6, block_size),
            Block(11800, HEIGHT - block_size * 5, block_size),
            Block(11800, HEIGHT - block_size * 4, block_size),
            Block(11800, HEIGHT - block_size * 3, block_size),
            Block(11800, HEIGHT - block_size * 2, block_size),
            #1
            Block(11900, HEIGHT - block_size * 2, block_size),
            #2
            Block(12000, HEIGHT - block_size * 2, block_size),   
            Block(12000, HEIGHT - block_size * 3, block_size),
            #3
            Block(12100, HEIGHT - block_size * 2, block_size),
            Block(12100, HEIGHT - block_size * 3, block_size),
            Block(12100, HEIGHT - block_size * 4, block_size),
            #4 
            Block(12200, HEIGHT - block_size * 2, block_size),
            Block(12200, HEIGHT - block_size * 3, block_size),
            Block(12200, HEIGHT - block_size * 4, block_size),
            Block(12200, HEIGHT - block_size * 5, block_size),
            #5
            Block(12300, HEIGHT - block_size * 2, block_size),
            Block(12300, HEIGHT - block_size * 3, block_size),
            Block(12300, HEIGHT - block_size * 4, block_size),
            Block(12300, HEIGHT - block_size * 5, block_size),
            Block(12300, HEIGHT - block_size * 6, block_size),
            #6
            Block(12400, HEIGHT - block_size * 2, block_size),
            Block(12400, HEIGHT - block_size * 3, block_size),
            Block(12400, HEIGHT - block_size * 4, block_size),
            Block(12400, HEIGHT - block_size * 5, block_size),
            Block(12400, HEIGHT - block_size * 6, block_size),
            Block(12400, HEIGHT - block_size * 7, block_size),
            #-5
            Block(12500, HEIGHT - block_size * 2, block_size),
            Block(12500, HEIGHT - block_size * 3, block_size),
            Block(12500, HEIGHT - block_size * 4, block_size),
            Block(12500, HEIGHT - block_size * 5, block_size),
            Block(12500, HEIGHT - block_size * 6, block_size),
            #-4
            Block(12600, HEIGHT - block_size * 2, block_size),
            Block(12600, HEIGHT - block_size * 3, block_size),
            Block(12600, HEIGHT - block_size * 4, block_size),
            Block(12600, HEIGHT - block_size * 5, block_size),
            #-3
            Block(12700, HEIGHT - block_size * 2, block_size),
            Block(12700, HEIGHT - block_size * 3, block_size),
            Block(12700, HEIGHT - block_size * 4, block_size),
            #-2
            Block(12800, HEIGHT - block_size * 2, block_size),   
            Block(12800, HEIGHT - block_size * 3, block_size),
            #-1
            Block(12900, HEIGHT - block_size * 2, block_size),
            fire  ]


    offset_x = 0
    scroll_area_width = 200

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.jump_count < 2:
                    player.jump()

        player.loop(FPS)
        fire.loop()
        handle_move(player, objects, left_wall)
        draw(window, background, bg_image, player, objects, offset_x)

        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)
