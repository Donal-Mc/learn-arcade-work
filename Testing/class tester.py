"""
class
    attributes - adjectives - instance variables
    methods - verbs - functions

inheritance
parent/child - you can inherit from a parent code
super class is parent
parent class is more generic

--Kitchen is a room--


class -- child class or arcade.Window
    on_mouse_motion
    set_mouse_visible
    on_mouse_press

keyboard:
    need starting position
    need move speed

game controller
"""
import random
import arcade

import self as self

#do this above the game itself
class Coin(arcade.sprite):
    def update(self):
        self.center_y -= 1
        if self.top <= 0:
            self.bottom = random.randrange((-SCREEN_HEIGHT, 0))
            self.center_x = random.randrange(SCREEN_WIDTH)
MOVEMENT_SPEED = 5
#for utilising a console
def update(self, delta_time):
    if self.joystick:
        print(self.joystick.x, self.joystick.y)
        self.ball.change_x = self.joystick.y * MOVEMENT_SPEED
        self.ball.change_y = -self.joystick.y * MOVEMENT_SPEED
    self.ball.update()
# For putting sounds in
import arcade
arcade.open_window(600, 600, "Sound Demo")
laser_sound = arcade.load_sound(("laser.ogg"))
arcade.play_sound(laser_sound)

def __init__(self):
    self.player_list = None
    self.coin_list = None

    self.player_sprite = None
    self.score = 0

    self.set_mouse_visible(False)

    arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.sprite_list()

    self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)
    self.player_sprite.center_x = 50
    self.player_sprite.center_y = 50
    self.player_list.append(self.player_sprite)

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.coin_list.draw()
        output = "Score" + str(self.score)
        arcade.draw_text("Score:", 10, 20, arcade.color.WHITE, 28)

for i in range(COIN_COUNT):
    coin = arcade.sprite("coin.png", SPRITE_SCALING_COIN)
    coin.center_x = random.randrange(SCREEN_WIDTH)
    coin.center_y = random.randrange(SCREEN_HEIGHT)
    self.coin_list.append(coin)

def on_mouse_motion(self, x, y, dx, dy)
    self.player_sprite.center_x = x
    self.player_sprite.center_y = y

def on_update(self, delta_time):

    self.coin_list.update()

    arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
    coin_hit_list = arcade.check_for_collision_with_list(self.player, self.coin_list)
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1


#code to chamge how the coins move
def __init__(self):
    super().__init__(filename, scale)
    self.change_x = 0
    self.change_y = 0

if self.left < 0:
    self.change_ x *= -1

if: i % 2
    coin.change_x = -1
else:
    coin.change_x = 1

