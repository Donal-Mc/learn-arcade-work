import random
import arcade

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.02
SPRITE_SCALING_LASER = 0.8
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_SPEED = 10


class MyGame(arcade.Window):
    """ Main application class. """

    class EnemySprite(arcade.Sprite):
        """ Enemy ship class that tracks how long it has been since firing. """

        def __init__(self, image_file, scale, bullet_list, time_between_firing):
            """ Set up the enemy """
            super().__init__(image_file, scale)

            # How long has it been since we last fired?
            self.time_since_last_firing = 0.0

            # How often do we fire?
            self.time_between_firing = time_between_firing

            # When we fire, what list tracks the bullets?
            self.bullet_list = bullet_list

        def on_update(self, delta_time: float = 1 / 60):
            """ Update this sprite. """

            # Track time since we last fired
            self.time_since_last_firing += delta_time

            # If we are past the firing time, then fire
            if self.time_since_last_firing >= self.time_between_firing:
                # Reset timer
                self.time_since_last_firing = 0

                # Fire the bullet
                bullet = arcade.Sprite("laserBlue01.png")
                bullet.center_x = self.center_x
                bullet.angle = -90
                bullet.top = self.bottom
                bullet.change_y = -2
                self.bullet_list.append(bullet)

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprites and Bullets Demo")

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.bullet_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):

        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        # Set up the player
        self.score = 0

        # Image from kenney.nl
        self.player_sprite = arcade.Sprite("spaceship.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.player_list.append(self.player_sprite)



        # Create the coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            oil = arcade.Sprite("Green oil.png", SPRITE_SCALING_COIN)

            # Position the coin
            oil.center_x = random.randrange(SCREEN_WIDTH)
            oil.center_y = random.randrange(120, SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(oil)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        arcade.start_render()

        # Draw all the sprites.
        self.coin_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()

        # Render the text
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """
        self.player_sprite.center_x = x

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked.
        """

        # Create a bullet
        bullet = arcade.Sprite("laserBlue01.png", SPRITE_SCALING_LASER)
        bullet.angle = 90
        bullet.center_x = self.player_sprite.center_x
        bullet.bottom = self.player_sprite.top
        bullet.change_y = BULLET_SPEED

        # Add the bullet to the appropriate lists
        self.bullet_list.append(bullet)

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.coin_list.update()
        self.bullet_list.update()

        # Loop through each bullet
        for bullet in self.bullet_list:

            # Check this bullet to see if it hit a coin list)


            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()
                # play sound here

            for coin in hit_list:
                self.score += 1
                coin.remove_from_sprite_lists()

            # If the bullet flies off-screen, remove it.
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()


def main():
    window = MyGame()
    window.setup()
    arcade.run()
main()