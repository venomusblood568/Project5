import pygame
import random
from enum import Enum
from collections import namedtuple
import numpy as np

# Pygame initialization and font setup
pygame.init()
font = pygame.font.Font('arial.ttf', 25)

# Enum for snake movement directions
class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

# Named tuple to represent a point in 2D space
Point = namedtuple("Point", "x, y")

# RGB colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0, 0, 0)

# Constants for block size and game speed
BLOCK_SIZE = 20
SPEED = 20

# SnakeGameAI class represents the game state and logic
class SnakeGameAI:
    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h
        # Initialize display and game properties
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('snake')
        self.clock = pygame.time.Clock()
        self.reset()

    # Reset the game state
    def reset(self):
        # Initialize game state variables
        self.direction = Direction.RIGHT
        self.head = Point(self.w / 2, self.h / 2)
        self.snake = [self.head,
                      Point(self.head.x - BLOCK_SIZE, self.head.y),
                      Point(self.head.x - (2 * BLOCK_SIZE), self.head.y)]
        self.score = 0
        self.food = None
        self._place_food()  # Place initial food
        self.frame_iteration = 0

    # Place food at a random location
    def _place_food(self):
        # Randomly place food, ensuring it is not on the snake
        x = random.randint(0, (self.w - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.h - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake:
            self._place_food()

    # Execute one step of the game given an action (movement direction)
    def play_step(self, action):
        self.frame_iteration += 1

        # Handle quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Move the snake based on the given action
        self._move(action)
        self.snake.insert(0, self.head)

        # Check for game over conditions
        reward = 0
        game_over = False
        if self.is_collision() or self.frame_iteration > 100 * len(self.snake):
            game_over = True
            reward = -10
            return reward, game_over, self.score

        # Place new food or just move the snake
        if self.head == self.food:
            self.score += 1
            reward = 10
            self._place_food()
        else:
            self.snake.pop()

        # Update the game UI and clock
        self._update_ui()
        self.clock.tick(SPEED)

        # Return reward, game over status, and current score
        return reward, game_over, self.score

    # Check if there is a collision with the snake
    def is_collision(self, pt=None):
        if pt is None:
            pt = self.head
        # Check if the point is out of bounds or collides with the snake body
        if pt.x > self.w - BLOCK_SIZE or pt.x < 0 or pt.y > self.h - BLOCK_SIZE or pt.y < 0:
            return True
        if pt in self.snake[1:]:
            return True
        return False

    # Update the game UI with snake, food, and score
    def _update_ui(self):
        # Clear the display and draw snake, food, and score
        self.display.fill(BLACK)
        for pt in self.snake:
            pygame.draw.rect(self.display, BLUE1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, BLUE2, pygame.Rect(pt.x + 4, pt.y + 4, 12, 12))
        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))
        text = font.render("Score: " + str(self.score), True, WHITE)
        self.display.blit(text, [0, 0])
        pygame.display.flip()

    # Move the snake in the given direction
    def _move(self, action):
        # Convert action vector to new direction
        clockwise = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
        idx = clockwise.index(self.direction)
        if np.array_equal(action, [1, 0, 0]):
            new_dir = clockwise[idx]  # No change in direction
        elif np.array_equal(action, [0, 1, 0]):
            next_idx = (idx + 1) % 4
            new_dir = clockwise[next_idx]  # Turn right (clockwise)
        else:  # [0, 0, 1]
            next_idx = (idx - 1) % 4
            new_dir = clockwise[next_idx]  # Turn left (counterclockwise)
        self.direction = new_dir

        # Move the snake's head in the updated direction
        x = self.head.x
        y = self.head.y
        if self.direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif self.direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif self.direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif self.direction == Direction.UP:
            y -= BLOCK_SIZE
        self.head = Point(x, y)
