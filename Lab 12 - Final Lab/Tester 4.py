import arcade
import random

# --- Constants ---
SPRITE_SCALING = 0.45
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

# All image and sound credits to Kenny.nl unless otherwise stated


class InstructionView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.csscolor.CADET_BLUE)
        # Reset the viewport, this centers the screen on what we draw
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Welcome to Gem Hunt", self.window.width / 2, self.window.height / 2 + 100,
                         arcade.color.PLUM, font_size=30, anchor_x="center")
        arcade.draw_text("Instructions Screen", self.window.width / 2, self.window.height / 2 + 50,
                         arcade.color.BLACK, font_size=25, anchor_x="center")
        arcade.draw_text("Find all the gems", self.window.width / 2, self.window.height / 2,
                         arcade.color.BLACK, font_size=25, anchor_x="center")
        arcade.draw_text("Avoid the enemies", self.window.width / 2, self.window.height / 2 - 50,
                         arcade.color.BLACK, font_size=25, anchor_x="center")
        arcade.draw_text("Click to advance", self.window.width / 2, self.window.height / 2-120,
                         arcade.color.BLACK, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)


class VictoryView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.csscolor.BLACK)
        # Reset the viewport, this centers the screen on what we draw
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("YOU WIN!!!!", self.window.width / 2, self.window.height / 2 + 50,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Click to Play again and improve your score", self.window.width / 2, self.window.height / 2 -
                         50, arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, re-start the game. """
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)
        victory_sound = arcade.load_sound("arcade_resources_sounds_upgrade2.wav")
        arcade.play_sound(victory_sound)


class GameView(arcade.View):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__()

        # Will play sound on start up
        arcade.play_sound(opening_sound)

        # Will load sounds for later
        self.gem_sound = arcade.load_sound("arcade_resources_sounds_coin3.wav")
        self.game_over = arcade.load_sound("arcade_resources_sounds_gameover2.wav")
        self.laser_sound = arcade.load_sound("arcade_resources_sounds_laser2.wav")
        self.injury_sound = arcade.load_sound("arcade_resources_sounds_hurt4.wav")

        # For player targeted shooting
        self.frame_count = 0

        # Variables that will hold sprite lists
        self.player_list = None
        self.gem_list = None
        self.wall_list = None
        self.enemy_list = None
        self.bullet_list = None
        self.player = None

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
        self.window.set_mouse_visible(False)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.gem_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

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
        # Position the gem
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

        gem = arcade.Sprite("Gem.gif", scale=0.08)
        gem.center_x = 1150
        gem.center_y = 200
        self.gem_list.append(gem)

        gem = arcade.Sprite("Gem.gif", scale=0.08)
        gem.center_x = 1000
        gem.center_y = 800
        self.gem_list.append(gem)

        gem = arcade.Sprite("Gem.gif", scale=0.08)
        gem.center_x = 800
        gem.center_y = 400
        self.gem_list.append(gem)

        # Creating enemies
        # Add enemy robots
        enemy = arcade.Sprite("character_0008.png", scale=2)
        enemy.center_x = 200
        enemy.center_y = 750
        enemy.angle = 180
        self.enemy_list.append(enemy)

        enemy = arcade.Sprite("character_0008.png", scale=2)
        enemy.center_x = 300
        enemy.center_y = 1250
        enemy.angle = 180
        self.enemy_list.append(enemy)

        enemy = arcade.Sprite("character_0008.png", scale=2)
        enemy.center_x = 800
        enemy.center_y = 900
        enemy.angle = 180
        self.enemy_list.append(enemy)

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
        self.enemy_list.draw()
        self.bullet_list.draw()

        # Select the camera for our GUI
        self.camera_gui.use()

        # Draw the GUI
        output = f"Score: {self.score}"
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
        gem_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.gem_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for gem in gem_hit_list:
            gem.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.gem_sound)

            # Check length of coin list. If it is zero, flip to the victory view.
            if len(self.gem_list) == 0:
                view = VictoryView()
                self.window.show_view(view)

        # Loop through each enemy that we have
        for enemy in self.enemy_list:

            # Have a random 1 in 200 change of shooting each 1/60th of a second
            odds = 200

            # Adjust odds based on delta-time
            adj_odds = int(odds * (1 / 60) / delta_time)

            if random.randrange(adj_odds) == 0:
                bullet = arcade.Sprite("Redlaser.png")
                bullet.center_x = enemy.center_x
                bullet.angle = 90
                bullet.top = enemy.bottom
                bullet.change_y = -2
                self.bullet_list.append(bullet)
                arcade.play_sound(self.laser_sound)

            # Get rid of the bullet when it flies off-screen
        for bullet in self.bullet_list:
            if bullet.top < 0:
                bullet.remove_from_sprite_lists()

        bullet_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bullet_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for bullet in bullet_hit_list:
            self.score -= 1
            arcade.play_sound(self.injury_sound)

        self.bullet_list.update()

    def scroll_to_player(self):
        """
        Scroll the window to the player.
        """
        width = 800
        height = 600
        position = self.player_sprite.center_x - width / 2, \
            self.player_sprite.center_y - height / 2
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        """
        Resize window
        Handle the user grabbing the edge and resizing the window.
        """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()
    arcade.run()


if __name__ == "__main__":
    main()
