""""Star Wars shooter game."""

import pygame, sys, math, random, time

pygame.init()

display = pygame.display.set_mode((1024, 768))
clock = pygame.time.Clock()

player_walk_images = [pygame.image.load("clone0.png"), pygame.image.load("clone1.png"),
pygame.image.load("clone2.png"), pygame.image.load("clone3.png")]

player_weapon = pygame.image.load("blasted.png").convert()
player_weapon.set_colorkey((255,255,255))

class Clone:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.animation_count = 0
        self.moving_right = False
        self.moving_left = False
        
    def handle_weapons(self, display):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        rel_x, rel_y = mouse_x - player.x, mouse_y - player.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)

        player_weapon_copy = pygame.transform.rotate(player_weapon, angle)

        display.blit(player_weapon_copy, (self.x+15-int(player_weapon_copy.get_width()/2), self.y+25-int(player_weapon_copy.get_height()/2)))


    def main(self, display):
        if self.animation_count + 1 >= 16:
            self.animation_count = 0

        self.animation_count += 1

        if self.moving_right:
            display.blit(pygame.transform.scale(player_walk_images[self.animation_count//4], (32, 42)), (self.x, self.y))
        elif self.moving_left:
            display.blit(pygame.transform.scale(pygame.transform.flip(player_walk_images[self.animation_count//4], True, False), (32, 42)), (self.x, self.y))
        else:
            display.blit(pygame.transform.scale(player_walk_images[0], (32, 42)), (self.x, self.y))

        self.handle_weapons(display)

        self.moving_right = False
        self.moving_left = False

class PlayerBullet:
    def __init__(self, x, y, mouse_x, mouse_y):
        self.x = x
        self.y = y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.speed = 15
        self.angle = math.atan2(y-mouse_y, x-mouse_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed
        
    def main(self, display):
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)

        pygame.draw.circle(display, (0,0,255), (self.x+16, self.y+16), 5)

class Droid:
    is_shot: bool = False
    starters: int = 0

    def __init__(self, x, y, starters: int = 5):
        self.x = x
        self.y = y
        self.starters = starters
        self.animation_images = [pygame.image.load("droid00.png"), pygame.image.load("droid01.png"),
        pygame.image.load("droid00.png"), pygame.image.load("droid01.png")]
        self.animation_count = 0
        self.reset_offset = 0
        self.offset_x = random.randrange(-300, 300)
        self.offset_y = random.randrange(-300, 300)

    def main(self, display):
        if self.animation_count + 1 == 16:
            self.animation_count = 0
        self.animation_count += 1

        if self.reset_offset == 0:
            self.offset_x = random.randrange(-300, 300)
            self.offset_y = random.randrange(-300, 300)
            self.reset_offset = random.randrange(120, 150)
        else:
            self.reset_offset -= 1

        if player.x + self.offset_x > self.x-display_scroll[0]:
            self.x += 1
        elif player.x + self.offset_x < self.x-display_scroll[0]:
            self.x -= 1

        if player.y + self.offset_y > self.y-display_scroll[1]:
            self.y += 1
        elif player.y + self.offset_y < self.y-display_scroll[1]:
            self.y -= 1

        display.blit(pygame.transform.scale(self.animation_images[self.animation_count//4], (32, 52)), (self.x-display_scroll[0], self.y-display_scroll[1]))
    
    def main(self, display):
        if self.animation_count + 1 == 16:
            self.animation_count = 0
        self.animation_count += 1

        if self.reset_offset == 0:
            self.offset_x = random.randrange(-300, 300)
            self.offset_y = random.randrange(-300, 300)
            self.reset_offset = random.randrange(120, 150)
        else:
            self.reset_offset -= 1

        if player.x + self.offset_x > self.x-display_scroll[0]:
            self.x += 1
        elif player.x + self.offset_x < self.x-display_scroll[0]:
            self.x -= 1

        if player.y + self.offset_y > self.y-display_scroll[1]:
            self.y += 1
        elif player.y + self.offset_y < self.y-display_scroll[1]:
            self.y -= 1

        display.blit(pygame.transform.scale(self.animation_images[self.animation_count//4], (32, 52)), (self.x-display_scroll[0], self.y-display_scroll[1]))

# class DroidBullet:
#     def __init__(self, x, y, target_x, target_y):
#         self.x = x
#         self.y = y
#         self.target_x = player.x + random.randint(-40, 40)
#         self.target_y = player.y + random.randint(-40, 40)
#         self.speed = 15
#         self.angle = math.atan2(y-player.y, x-player.x)
#         self.x_vel = math.cos(self.angle) * self.speed
#         self.y_vel = math.sin(self.angle) * self.speed

#     def main(self, display):
#         self.x -= int(self.x_vel)
#         self.y -= int(self.y_vel)

#         pygame.draw.circle(display, (255,0,0), (self.x+16, self.y+16), 5)


player = Clone(400, 300, 32, 32)

display_scroll = [0,0]

player_bullets = []

droidy = Droid(400, 300)

droid_army = []

# enemies_bullets = []

while 1:
    display.fill((24,164,86))

    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    # target_x = mouse_x + random.randint(-40, 40)
    # target_y = mouse_y + random.randint(-40, 40)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player_bullets.append(PlayerBullet(player.x, player.y, mouse_x, mouse_y))
        
        # if Droid.is_shot == False:
        #     droid_bullets.append(DroidBullet(enemies.x, enemies.y, target_x, target_y))
               
    keys = pygame.key.get_pressed()

    pygame.draw.rect(display, (24,164,86), (100-display_scroll[0], 100-display_scroll[1], 16, 16))

    if keys[pygame.K_a]:
        display_scroll[0] -= 5

        player.moving_left = True

        for bullet in player_bullets:
            bullet.x += 5
    if keys[pygame.K_d]:
        display_scroll[0] += 5

        player.moving_right = True

        for bullet in player_bullets:
            bullet.x -= 5
    if keys[pygame.K_w]:
        display_scroll[1] -= 5

        for bullet in player_bullets:
            bullet.y += 5
    if keys[pygame.K_s]:
        display_scroll[1] += 5

        for bullet in player_bullets:
            bullet.y -= 5
    
    player.main(display)
    
    droidy.main(display)

    for bullet in player_bullets:
        bullet.main(display)


    pygame.mouse.set_visible(False)
    crosshair_image = pygame.image.load('crosshair.png') 
    crosshair_image_rect = crosshair_image.get_rect()
    crosshair_image_rect.center = pygame.mouse.get_pos()
    display.blit(crosshair_image, crosshair_image_rect.center)

    clock.tick(60)
    pygame.display.update()

    
#character ring

#music

#track time

#obstacles (vary within a fixed interval of size)


#background (separate file)

#enemies or droids (ben's stack) and colliding when shot (or escape)

#enemy movement

#winning screen + music

#losing screen + music