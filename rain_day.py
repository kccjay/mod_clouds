# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.


# Imports
import pygame
import random

# Initialize game engine
pygame.init()

# Window 
SIZE = (800, 600)
TITLE = "Sunny Day"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
GREEN = (0, 175, 0)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
YELLOW = (255, 255, 175)
GREY = (191, 191, 191)
RAIN = (51, 153, 255)
DGREEN = (0, 153, 51)
MOON = (230, 230, 230)
RAIN_CLOUD = (77, 77, 77)
CLOUD_C = RAIN_CLOUD

# Make clouds
num_clouds = 25
clouds = []
for i in range(num_clouds):
    x = random.randrange(0, 1600)
    y = random.randrange(-50, 200)
    s = random.randrange(2, 4)
    loc = [x, y, s]
    clouds.append(loc)

def draw_cloud(loc):
    x = loc[0]
    y = loc[1]
    
    pygame.draw.ellipse(screen, CLOUD_C, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, CLOUD_C, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, CLOUD_C, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, CLOUD_C, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, CLOUD_C, [x + 20, y + 20, 60, 40])

# Raindrops
num_rain = 500
rain = []
for i in range(num_rain):
    x = random.randrange(0, 800)
    y = random.randrange(0, 600)
    r = random.randrange(1,5)
    drops = [x, y, r, r]
    rain.append(drops)

   
# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    # Game logic
    for c in clouds:
        c[0] -= c[2]

        if c[0] < -100:
           c[0] = random.randrange(800, 1600)
           c[1] = random.randrange(-50, 200)

    for r in rain:
        r[0] -= 1
        r[1] += 5

        if r[1] > 620:
            r[0] = random.randrange(0, 1200)
            r[1] = random.randrange(-50, -1)
             
    # Drawing code
    ''' sky '''
    screen.fill(GREY)

    ''' sun '''
    pygame.draw.ellipse(screen, MOON, [575, 75, 100, 100])
    
    ''' grass '''
    pygame.draw.rect(screen, DGREEN, [0, 400, 800, 200])
    
    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)

    ''' rain '''
    for drops in rain:
        pygame.draw.ellipse(screen, RAIN, drops)

    ''' clouds '''
    for c in clouds:
        draw_cloud(c)

        
    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
