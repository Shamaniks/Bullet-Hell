import pygame


def main():
    """Инициализация физических величин"""
    gravity_acceleration = 10 # Ускорение свободного падения

    """Инициализация процесса"""
    TPS = 60 # Обновления (tick) в секунду
    pygame.init()
    pygame.display.set_caption("It's time for bullet hell")
    size = width, height = 1920, 1080
    screen = pygame.display.set_mode(size)
    running = True
    while running:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        pygame.display.flip()
    pygame.quit()


main()