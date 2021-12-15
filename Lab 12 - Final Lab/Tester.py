import random
import arcade
import math
import os

# --- Constants ---
SPRITE_SCALING = 0.5
TILE_SCALING = 0.34
GRID_PIXEL_SIZE = 128
GRAVITY = 0.4
SCREEN_TITLE = "Lab 12"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 220

# How fast the camera pans to the player.
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 7
JUMP_SPEED = 10

opening_sound = arcade.load_sound("arcade_resources_sounds_explosion2.wav")

# All image credits to Kenny.nl unless otherwise stated


class Gem(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        """ Constructor. """
        # Call the parent class (Sprite) constructor
        super().__init__(filename, sprite_scaling)

        # Current angle in radians
        self.circle_angle = 0

        # How far away from the center to orbit, in pixels
        self.circle_radius = 0

        # How fast to orbit, in radians per frame
        self.circle_speed = 0.008

        # Set the center of the point we will orbit around
        self.circle_center_x = 0
        self.circle_center_y = 0

    def update(self):
        self.angle += 1
        # If we rotate past 360, reset it back a turn.
        if self.angle > 359:
            self.angle -= 360


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=True)

        # Will play sound on start up
        arcade.play_sound(opening_sound)

        # Will load sounds for later
        self.gem_sound = arcade.load_sound("arcade_resources_sounds_coin3.wav")
        self.game_over = arcade.load_sound("arcade_resources_sounds_gameover2.wav")
        self.gun_sound = arcade.load_sound("arcade_resources_sounds_laser2.wav")



        # Variables that will hold sprite lists
        self.player_list = None
        self.gem_list = None
        self.wall_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        self.physics_engine = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False

        # Store our tile map
        self.tile_map = None

        # Create the cameras. One for the GUI, one for the sprites.
        self.camera_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Don't show the mouse cursor
        self.set_mouse_visible(False)



    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.gem_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("character_0002.png", scale=1.7)
        self.player_sprite.center_x = 200
        self.player_sprite.center_y = 200
        self.player_list.append(self.player_sprite)

        # --- Load our map

        # Read in the tiled map
        map_name = "LabMap.json"
        self.tile_map = arcade.load_tilemap(map_name, scaling=TILE_SCALING)

        # Set wall and coin SpriteLists
        self.wall_list = self.tile_map.sprite_lists["Walls"]

        # Create the gems
        # gem image from Giphy on Pinterest
        gem = arcade.Sprite("Gem.gif", scale=0.08)

        # Position the coin
        gem = arcade.Sprite("Gem.gif", scale=0.08)
        gem.center_x = 350
        gem.center_y = 300
        self.gem_list.append(gem)

        gem = arcade.Sprite("Gem.gif", scale=0.08)
        gem.center_x = 800
        gem.center_y = 150
        self.gem_list.append(gem)

        gem = arcade.Sprite("Gem.gif", scale=0.08)
        gem.center_x = 550
        gem.center_y = 680
        self.gem_list.append(gem)

        gem = arcade.Sprite("Gem.gif", scale=0.08)
        gem.center_x = 40
        gem.center_y = 800
        self.gem_list.append(gem)

        gem = arcade.Sprite("Gem.gif", scale=0.08)
        gem.center_x = 40
        gem.center_y = 1250
        self.gem_list.append(gem)

        gem = arcade.Sprite("Gem.gif", scale=0.08)
        gem.center_x = 800
        gem.center_y = 1050
        self.gem_list.append(gem)

        gem = arcade.Sprite("Gem.gif", scale=0.08)
        gem.center_x = 370
        gem.center_y = 1200
        self.gem_list.append(gem)

        gem = arcade.Sprite("Gem.gif", scale=0.08)
        gem.center_x = 500
        gem.center_y = 900
        self.gem_list.append(gem)

        gem = arcade.Sprite("Gem.gif", scale=0.08)
        gem.center_x = 950
        gem.center_y = 150
        self.gem_list.append(gem)

        gem = arcade.Sprite("Gem.gif", scale=0.08)
        gem.center_x = 800
        gem.center_y = 800
        self.gem_list.append(gem)


            # Set the background color
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

            # Keep player from running through the wall_list layer
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite,
            self.wall_list,
            gravity_constant=GRAVITY)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        # Select the camera we'll use to draw all our sprites
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.gem_list.draw()

        # Select the (unscrolled) camera for our GUI
        self.camera_gui.use()

        # Draw the GUI
        arcade.draw_rectangle_filled(self.width // 2,
                                     20,
                                     self.width,
                                     40,
                                     arcade.color.ALMOND)
        text = output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP_SPEED
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False


    def update(self, delta_time):
        """ Movement and game logic """
        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        # self.player_sprite.change_y = 0

        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # Scroll the screen to the player
        self.scroll_to_player()

        self.gem_list.update()
        # Generate a list of all sprites that collided with the player.
        gem_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.gem_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for gem in gem_hit_list:
            gem.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.gem_sound)


    def scroll_to_player(self):
        """
        Scroll the window to the player.
        """

        position = self.player_sprite.center_x - self.width / 2, \
            self.player_sprite.center_y - self.height / 2
        self.camera_sprites.move_to(position, CAMERA_SPEED)


    def on_resize(self, width, height):
        """
        Resize window
        Handle the user grabbing the edge and resizing the window.
        """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))



def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
