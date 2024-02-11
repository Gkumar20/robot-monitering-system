
import pygame
import sys
import random
import math

def draw_grid(screen, width, height, grid_size):
    for x in range(0, width, grid_size):
        pygame.draw.line(screen, (200, 200, 200), (x, 0), (x, height))
    for y in range(0, height, grid_size):
        pygame.draw.line(screen, (200, 200, 200), (0, y), (width, y))

def draw_robot(screen, position, image):
    screen.blit(image, position)

def draw_random_object(screen, object_position, object_size, object_image):
    scaled_image = pygame.transform.scale(object_image, (object_size, object_size))
    screen.blit(scaled_image, object_position)

def calculate_displacement(robot_position, object_position):
    dx = object_position[0] - robot_position[0]
    dy = object_position[1] - robot_position[1]
    return math.sqrt(dx**2 + dy**2)

def main():
    pygame.init()
    width, height = 500, 500
    grid_size = 50
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Grid Display with Blinking Robot and Random Object")  
    robot_size = 50
    robot_position = [width // 2 - robot_size // 2, height // 2 - robot_size // 2] 
    robot_image = pygame.image.load("robot.png")
    robot_image = pygame.transform.scale(robot_image, (robot_size, robot_size)) 
    object_image = pygame.image.load("object.png")

    clock = pygame.time.Clock()
    blink_frequency = 1  
    random_object_frequency = 10  
    object_hold_duration = 3  
    time_since_last_object = 0
    object_hold_start_time = 0
    random_object_position = [0, 0]
    object_size = 30  

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))

        draw_grid(screen, width, height, grid_size)      
        if pygame.time.get_ticks() - object_hold_start_time < (object_hold_duration * 1000):
            draw_random_object(screen, random_object_position, object_size, object_image)
            draw_robot(screen, robot_position, robot_image)
        else:
            if pygame.time.get_ticks() % (blink_frequency * 1000) < (blink_frequency * 500):
                draw_robot(screen, robot_position, robot_image)
            else:
                pass
            if pygame.time.get_ticks() - time_since_last_object > (random_object_frequency * 1000):
                random_object_position = [random.randint(0, width - object_size), random.randint(0, height - object_size)]
                time_since_last_object = pygame.time.get_ticks()
                object_hold_start_time = time_since_last_object
                displacement = calculate_displacement(robot_position, random_object_position)
                print(f"Trace Intruder Detected at {random_object_position}. Displacement from robot: {displacement:.2f} units.")
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
