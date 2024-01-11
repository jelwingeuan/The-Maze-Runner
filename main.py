import pygame

pygame.init()

WIDTH, HEIGHT = 1920, 1080

scr = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animal Run")

# list
WHITE = (255, 255, 255)
FPS = 60


def main():
    # game loop
    run = True
    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        scr.fill(WHITE)
        pygame.display.flip()

    # quit game
    pygame.quit()


# only to run this "main" func
if __name__ == "__main__":
    main()
