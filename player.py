from circleshape import *
from constants import *
from weapons import *
import sys

# this whole file is a fucking mess
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 0
        self.timer = 0
        self.lives = 3
        self.score = 0
        self.weapon = basic_laser
        self.invulnerable = False
        self.invulnerable_timer = 2
        self.color = "white"
        self.upgrade_triggered = False

    # draw the player's character as a triangle :D
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # some default behavior for player class
    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def collide(self, other):
        if not self.invulnerable:
            return super().collide(other)
        
    # we also respawn the player here, it's easier. + invuln period to stop instadeaths
    def death(self):
        self.lives -= 1

        if self.lives > 0:
            self.invulnerable = True
            self.timer = self.invulnerable_timer
            print(f"Lives: {self.lives}")
            self.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

        else:
            print("Game Over!")
            print(f"Final score: {self.score}")
            sys.exit()


    # shooting related methods
    def shoot(self):
        if self.timer <= 0:
            shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.timer = self.weapon.cooldown

    def updatepoints(self):
        self.score += 5
        print(f"Score: {self.score}")

    def upgrade_weapon(self):
        if weapons.index(self.weapon) < len(weapons) - 1:
            self.weapon = weapons[(weapons.index(self.weapon) + 1)]
            self.color = self.weapon.color
            self.upgrade_triggered = True
            print(f"Bonus! Upgraded weapon: {self.weapon}!")


    # this runs every frame
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * -1)
        if keys[pygame.K_SPACE]:
            self.shoot()

        # decrement shot cooldown
        if self.timer > 0:
            self.timer -= dt

        # decrement invulnerability frames
        if self.invulnerable:
            if self.invulnerable_timer > 0:
                self.invulnerable_timer -= dt
            else:
                self.invulnerable = False
                self.invulnerable_timer = 2  # Reset the timer for the next death

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        pygame.sprite.Sprite.__init__(self, self.containers)

    def draw(self, screen):
        # Draw the bullet as a circle
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)