from pygame import *
class GameSprite(sprite.Sprite):
    #class constructor
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        #Call for the class (Sprite) constructor:
        super().__init__()


        #every sprite must store the image property
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed


        #every sprite must have the rect property that represents the rectangle it is fitted in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    #method drawing the character on the window
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    #method to control the sprite with arrow keys
    def updatel(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def updater(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_d] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    #method to "shoot" (use the player position to create a bullet there)
back = (69,69,69)
win_width = 500
window = display.set_mode((600,500))
window.fill(back)
game = True
finish = False
clock = time.Clock()
racketl = Player('left.png',50,50,50,150,10)
racketr = Player('right.png',500,50,50,150,10)
ball = GameSprite('ball.jpg',250,50,50,150,30)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        racketl.updatel()
        racketr.updater()
        racketl.reset()
        racketr.reset()
        ball.reset()
    display.update()
    clock.tick(69)