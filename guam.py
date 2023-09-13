import pygame
import random

class square:
    rect: pygame.Rect
    color: tuple

    def __init__(self, rect) -> None:
        self.rect = rect
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def fall(self):
        self.rect.move_ip(0, 1)
        if self.rect.bottom == 600:
            self.bottom = 0




def main():
    screen = width, height = 400, 600
    display = pygame.display.set_mode(screen)
    
    clock = pygame.time.Clock()
    pygame.init()

    player = square(pygame.Rect(10, 10, 10, 10))

    badhomies = [square(pygame.Rect(random.randint(0, 290), random.randint(-290, 0), random.randint(10, 25), random.randint(10, 40))) for i in range(10)]

    road = pygame.Rect(100, 0, 200, 600)


    while 1:
        display.fill((255,255,255))
        for i in pygame.event.get():
            player.rect.clamp_ip(road)
            if i.type == pygame.QUIT:
                pygame.quit()
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_k:
                    player.rect.move_ip(0, 10)
                if i.key == pygame.K_j:
                    player.rect.move_ip(-10, 0)
                if i.key == pygame.K_l:
                    player.rect.move_ip(10, 0)
                if i.key == pygame.K_i:
                    player.rect.move_ip(0, -10)
        
        pygame.draw.rect(display, (10,10,10), road)

        for i in badhomies:
            i.fall()
            if i.rect.colliderect(player.rect):
                pygame.quit()
            pygame.draw.rect(display, i.color, i.rect)

        pygame.draw.rect(display, player.color, player.rect)
        pygame.display.update()



if __name__ == "__main__":
    main()