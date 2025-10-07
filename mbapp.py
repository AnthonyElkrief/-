import pygame
import sys
import math
import random

pygame.init()
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mbappe Penalty - Super Realistic")
clock = pygame.time.Clock()
FPS = 60

# צבעים
GREEN = (34,139,34)
WHITE = (255,255,255)
BLUE = (0,0,255)
YELLOW = (255,255,0)
ORANGE = (255,165,0)
RED = (255,0,0)
BROWN = (139,69,19)

# מגרש ושער
goal_width, goal_height = 200, 100
goal_x, goal_y = WIDTH//2 - goal_width//2, 50

# כדור
ball_radius = 15
ball_x, ball_y = WIDTH//2, HEIGHT-120
ball_speed = 15
ball_moving = False

# חלקיקים
particles = []

def create_particle(x, y):
    particles.append({
        "x": x + random.randint(-15,15),
        "y": y + random.randint(-15,15),
        "radius": random.randint(3,6),
        "color": random.choice([YELLOW, ORANGE, RED]),
        "life": random.randint(20,40)
    })

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.kick_phase = 0  # 0=מוכן, 1=רגל עולה, 2=בעיטה
        self.kick_timer = 0
        self.kick_duration = 25  # frames of kick animation

    def start_kick(self):
        if self.kick_phase == 0:
            self.kick_phase = 1
            self.kick_timer = 0

    def update(self):
        if self.kick_phase > 0:
            self.kick_timer += 1
            if self.kick_timer < self.kick_duration/2:
                self.kick_phase = 1  # רגל עולה
            elif self.kick_timer < self.kick_duration:
                self.kick_phase = 2  # בעיטה
            else:
                self.kick_phase = 0
                global ball_moving
                ball_moving = True

    def draw(self):
        t = self.kick_timer / self.kick_duration
        # ראש
        pygame.draw.circle(screen, BROWN, (self.x, self.y-60), 15)
        # גוף
        body_shift = int(t*5)  # קצת נוטה קדימה
        pygame.draw.rect(screen, BLUE, (self.x-10+body_shift, self.y-50, 20, 40))
        # זרועות
        arm_angle = math.sin(t*math.pi)*25
        pygame.draw.line(screen, YELLOW, (self.x-15, self.y-45), (self.x-35, self.y-45+arm_angle), 4)
        pygame.draw.line(screen, YELLOW, (self.x+15, self.y-45), (self.x+35, self.y-45+arm_angle), 4)
        # רגליים
        pygame.draw.line(screen, BLUE, (self.x-5, self.y-10), (self.x-5, self.y+30), 5)  # רגל שמאל
        if self.kick_phase == 0:
            pygame.draw.line(screen, BLUE, (self.x+5, self.y-10), (self.x+5, self.y+30), 5)
        else:
            # רגל ימין נע קדימה עם קפיצה
            kick_dx = int(60*t)
            kick_dy = int(30*abs(math.sin(t*math.pi)))
            pygame.draw.line(screen, BLUE, (self.x+5, self.y-10), (self.x+5+kick_dx, self.y-10-kick_dy), 5)

player = Player(WIDTH//2, HEIGHT-120)

def draw_field():
    screen.fill(GREEN)
    pygame.draw.rect(screen, WHITE, (50,50,WIDTH-100,HEIGHT-100),5)
    pygame.draw.line(screen, WHITE, (WIDTH//2,50),(WIDTH//2, HEIGHT-50),3)
    pygame.draw.rect(screen, WHITE, (WIDTH//2-100, HEIGHT-150,200,100),3)

def draw_goal():
    pygame.draw.rect(screen, WHITE, (goal_x, goal_y, goal_width, goal_height),5)
    for i in range(10):
        pygame.draw.line(screen, WHITE, (goal_x + i*20, goal_y), (goal_x + i*20, goal_y+goal_height))
        pygame.draw.line(screen, WHITE, (goal_x, goal_y + i*10), (goal_x + goal_width, goal_y + i*10))

def draw_ball():
    global ball_x, ball_y, ball_moving
    if ball_moving:
        dx = WIDTH//2 - ball_x
        dy = goal_y + goal_height//2 - ball_y
        dist = math.hypot(dx, dy)
        if dist > 5:
            ball_x += dx/dist * ball_speed
            ball_y += dy/dist * ball_speed
        else:
            ball_moving = False
            for _ in range(30):
                create_particle(ball_x, ball_y)
    pygame.draw.circle(screen, WHITE, (int(ball_x), int(ball_y)), ball_radius)

def update_particles():
    for p in particles[:]:
        pygame.draw.circle(screen, p["color"], (int(p["x"]), int(p["y"])), p["radius"])
        p["life"] -= 1
        p["y"] -= 1
        if p["life"] <= 0:
            particles.remove(p)

running = True
while running:
    draw_field()
    draw_goal()
    draw_ball()
    player.update()
    player.draw()
    update_particles()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.start_kick()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()