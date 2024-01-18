import pygame


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


if __name__ != "__main__":
    exit(0)

back = (200, 255, 255)
win_width = 600
win_height = 500
window = pygame.display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = pygame.time.Clock()
FPS = 60

racket1 = Player('676256_nc.png', 30, 200, 4, 50, 150)
racket2 = Player('676256_nc.png', 520, 200, 4, 50, 150)
ball = GameSprite('BALL.png', 200, 200, 4, 50, 50)

pygame.font.init()
font = pygame.font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

speed_x = 3
speed_y = 3

while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    if finish:
        continue

    window.fill(back)
    racket1.update_l()
    racket2.update_r()
    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if pygame.sprite.collide_rect(racket1, ball) or pygame.sprite.collide_rect(racket2, ball):
        speed_x *= -1
        speed_y *= 1

    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1

    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))
        game_over = True

    if ball.rect.x > win_width:
        finish = True
        window.blit(lose2, (200, 200))
        game_over = True

    racket1.reset()
    racket2.reset()
    ball.reset()

    pygame.display.update()
    clock.tick(FPS)
