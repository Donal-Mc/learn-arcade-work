import arcade
import os

SPRITE_SCALING = 3

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Walls"

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Sprite lists
        self.coin_list = None
        self.wall_list = None
        self.player_list = None

        # Set up the player
        self.player_sprite = None
        self.physics_engine = None

    def setup(self):
        """ Set up the game and initialize the variables. """
        # All sprites courtesy of Kenny
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite("character_0001.png",
                                           SPRITE_SCALING)
        self.player_sprite.center_x = 40
        self.player_sprite.center_y = 40
        self.player_list.append(self.player_sprite)

        coordinate_list = [[65, 580],
                           [100, 580],
                           [150, 580],
                           [200, 580],
                           [250, 580],
                           [350, 580],
                           [400, 580],
                           [300, 580],
                           [450, 580],
                           [500, 580],
                           [550, 580],
                           [600, 580],
                           [650, 580],
                           [700, 580],
                           [750, 580],
                           [800, 580]]

        # Loop through coordinates
        for coordinate in coordinate_list:
            wall = arcade.Sprite("tile_0073.png", SPRITE_SCALING)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        coordinate_list = [[200, 150],
                           [200, 200],
                           [200, 250],
                           [200, 300],
                           [200, 350],
                           [200, 400],
                           [200, 450]]

        # Loop through coordinates
        for coordinate in coordinate_list:
            wall = arcade.Sprite("tile_0013.png", SPRITE_SCALING)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        coordinate_list = [[500, 150],
                           [500, 200],
                           [500, 250],
                           [500, 300],
                           [500, 350],
                           [500, 400],
                           [500, 450]]

        # Loop through coordinates
        for coordinate in coordinate_list:
            wall = arcade.Sprite("tile_0013.png", SPRITE_SCALING)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        coordinate_list = [[650, 150],
                           [650, 200],
                           [650, 250],
                           [650, 300],
                           [650, 350],
                           [650, 400],
                           [650, 450]]

        # Loop through coordinates
        for coordinate in coordinate_list:
            wall = arcade.Sprite("tile_0013.png", SPRITE_SCALING)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        coordinate_list = [[725, 300],
                           [703, 300]]

        # Loop through coordinates
        for coordinate in coordinate_list:
            wall = arcade.Sprite("tile_0013.png", SPRITE_SCALING)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        coordinate_list = [[100, 150],
                           [150, 150],
                           [60, 150]]

        # Loop through coordinates
        for coordinate in coordinate_list:
            wall = arcade.Sprite("tile_0013.png", SPRITE_SCALING)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)


        coordinate_list = [[20, 10],
                           [50, 10],
                           [100, 10],
                           [150, 10],
                           [200, 10],
                           [250, 10],
                           [350, 10],
                           [400, 10],
                           [300, 10],
                           [450, 10],
                           [500, 10],
                           [550, 10],
                           [600, 10],
                           [650, 10],
                           [700, 10],
                           [750, 10],
                           [800, 10]]

        # Loop through coordinates
        for coordinate in coordinate_list:
            wall = arcade.Sprite("tile_0001.png", SPRITE_SCALING)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        coordinate_list = [[780, 60],
                           [780, 100],
                           [780, 150],
                           [780, 200],
                           [780, 250],
                           [780, 300],
                           [780, 350],
                           [780, 400],
                           [780, 450],
                           [780, 500],
                           [780, 550],
                           [780, 600]]

        # Loop through coordinates
        for coordinate in coordinate_list:
            wall = arcade.Sprite("tile_0054.png", SPRITE_SCALING)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        coordinate_list = [[10, 60],
                           [10, 100],
                           [10, 150],
                           [10, 200],
                           [10, 250],
                           [10, 300]]

        # Loop through coordinates
        for coordinate in coordinate_list:
            wall = arcade.Sprite("tile_0054.png", SPRITE_SCALING)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        coordinate_list = [[10, 350],
                           [10, 400],
                           [10, 450],
                           [10, 500],
                           [10, 550],
                           [10, 600]]

        # Loop through coordinates
        for coordinate in coordinate_list:
            wall = arcade.Sprite("tile_0054.png", SPRITE_SCALING)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                         self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()


def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()