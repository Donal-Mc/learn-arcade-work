import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MOVEMENT_SPEED = 5
DEAD_ZONE = 0.1


class NeonBall:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x



        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius

class Square:
    def __init__(self, position_x, position_y, change_x, change_y, width, height, color):

        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        arcade.draw_rectangle_filled(self.position_x,
                                     self.position_y,
                                     self.width,
                                     self.height,
                                     self.color)

    def update(self):
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the square hit the edge of the screen. If so, change direction
        if self.position_x < self.height * self.width:
            self.position_x = self.height * self.width

        if self.position_x > SCREEN_WIDTH - self.height * self.width:
            self.position_x = SCREEN_WIDTH - self.height * self.width

        if self.position_y < self.height * self.width:
            self.position_y = self.height * self.width

        if self.position_y > SCREEN_HEIGHT - self.height * self.width:
            self.position_y = SCREEN_HEIGHT - self.height * self.width



class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ONYX)

        # Create our ball
        self.ball = NeonBall(50, 50, 0, 0, 15, arcade.color.NEON_GREEN)

        # create our square
        self.square = Square(175, 100, 20, 20, 20, 20, arcade.color.NEON_FUCHSIA)

        # Get a list of all the game controllers that are plugged in
        joysticks = arcade.get_joysticks()

        # If we have a game controller plugged in, grab it and
        # make an instance variable out of it.
        if joysticks:
            self.joystick = joysticks[0]
            self.joystick.open()
        else:
            print("There are no joysticks.")
            self.joystick = None

    def on_draw(self):

        """ Called whenever we need to draw the window. """
        arcade.start_render()

        # will draw sinister semi circles
        arcade.draw_arc_filled(300, 350, 110, 110, arcade.csscolor.AQUAMARINE, 0, 180)
        arcade.draw_arc_filled(100, 350, 110, 110, arcade.csscolor.AQUAMARINE, 0, 180)
        arcade.draw_arc_filled(500, 350, 110, 110, arcade.csscolor.AQUAMARINE, 0, 180)

        arcade.draw_arc_filled(300, 100, 110, 110, arcade.csscolor.AQUAMARINE, 180, 360)
        arcade.draw_arc_filled(100, 100, 110, 110, arcade.csscolor.AQUAMARINE, 180, 360)
        arcade.draw_arc_filled(500, 100, 110, 110, arcade.csscolor.AQUAMARINE, 180, 360)

        self.ball.draw()
        self.square.draw()

    def update(self, delta_time):

        # Update the position according to the game controller
        if self.joystick:

            # Set a "dead zone" to prevent drive from a centered joystick
            if abs(self.joystick.x) < DEAD_ZONE:
                self.ball.change_x = 0
            else:
                self.ball.change_x = self.joystick.x * MOVEMENT_SPEED

            # Set a "dead zone" to prevent drive from a centered joystick
            if abs(self.joystick.y) < DEAD_ZONE:
                self.ball.change_y = 0
            else:
                self.ball.change_y = -self.joystick.y * MOVEMENT_SPEED

        def on_key_press(self, key, modifiers):
            """ Called whenever the user presses a key. """
            if key == arcade.key.LEFT:
                self.square.change_x = -MOVEMENT_SPEED
            elif key == arcade.key.RIGHT:
                self.square.change_x = MOVEMENT_SPEED
            elif key == arcade.key.UP:
                self.square.change_y = MOVEMENT_SPEED
            elif key == arcade.key.DOWN:
                self.square.change_y = -MOVEMENT_SPEED

        def on_key_release(self, key, modifiers):
            """ Called whenever a user releases a key. """
            if key == arcade.key.LEFT or key == arcade.key.RIGHT:
                self.square.change_x = 0
            elif key == arcade.key.UP or key == arcade.key.DOWN:
                self.square.change_y = 0

        self.ball.update()
        self.square.update()


def main():
    window = MyGame(640, 480, "Drawing Example")
    arcade.run()


main()
