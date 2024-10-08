import random

from pico2d import *

# Game object class here
class Grass:
    # 생성자 함수 : 객체의 초기 상태를 설정
    def __init__(self):
        # 모양 없는 납작한 붕어빵의 초기모습결정
        self.image = load_image('grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        self.big_x, self.big_y = random.randint(50, 750), 599
        self.small_x, self.small_y = random.randint(50, 750), 599
        self.small_big = random.randint(0, 1)
        self.small_image = load_image('ball21x21.png')
        self.big_image = load_image('ball41x41.png')

    def update(self):

        if self.small_y <= 60:
            pass
        else:
            self.small_y -= 5

        if self.big_y <= 70:
            pass
        else:
            self.big_y -= 5

    def draw(self):
        if self.small_big == 0:
            self.small_image.draw(self.small_x, self.small_y)
        else:
            self.big_image.draw(self.big_x, self.big_y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    global grass
    global team
    global ball
    global world


    running = True
    world = []

    grass = Grass() # 잔디를 생성한다
    world.append(grass)

    team = [Boy() for i in range(11)]
    world += team

    ball = [Ball() for i in range(20)]
    world += ball

def update_world():
    for o in world: # 객체의 상태를 업데이트
        o.update()
    pass

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

running = True

open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    # game logic
    handle_events()
    update_world()  # 상호작용을 시뮬레이션
    render_world()   # 그 결과를 보여준다.
    delay(0.05)

# finalization code

close_canvas()
