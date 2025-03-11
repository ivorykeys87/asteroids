from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS

class Shot(CircleShape):

    def __init__(self, x, y, player_rotation, shoot_speed ):
        super().__init__(x,y,SHOT_RADIUS)
        self.velocity = pygame.Vector2(0,1).rotate(player_rotation)*shoot_speed
    
    def draw(self, screen):
        pygame.draw.circle(screen,(255,255,255),self.position,self.radius,2)

    def update(self, delta_time):
        self.position += self.velocity * delta_time