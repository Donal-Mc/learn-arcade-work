import arcade

screen_width = 600
screen_height = 600

def draw_city_hall_base(30, 100):
    """Will draw the main building of City Hall"""

    #draws a point at 300, 300 for reference
    arcade.draw_point(30, 100, arcade.color.RED, 5)

    #The domes
    arcade.draw_arc_filled(535, 400, 175, 200, arcade.csscolor.AQUAMARINE, 0, 180)
    arcade.draw_arc_filled(64, 400, 175, 200, arcade.csscolor.AQUAMARINE, 0, 180)
    arcade.draw_arc_filled(300, 500, 200, 200, arcade.csscolor.AQUAMARINE, 0, 180)

    #The main building
    arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(0, 599, 40, 0, arcade.color.GREEN)
    arcade.draw_ellipse_filled(300, 10, 200, 100, arcade.csscolor.WHITE)
    arcade.draw_rectangle_filled(50, 300, 200, 250, arcade.color.WHITE)
    arcade.draw_lrtb_rectangle_filled(200, 400, 500, 100, arcade.color.WHITE)
    arcade.draw_rectangle_filled(550, 300, 200, 250, arcade.color.WHITE)

def main():
    arcade.open_window(600, 600, "drawing example")
    arcade.set_background_color((81, 123, 201))
    arcade.start_render()

    draw_city_hall_base()

    # will draw a sun in the top right corner
    arcade.draw_circle_filled(500, 550, 40, arcade.color.YELLOW)
    arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 500, 490, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW, 3)
    arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3)

    # will create details on the city hall itself
    arcade.draw_text("Belfast City Hall",
                     240, 220,
                     arcade.color.MAHOGANY)
    arcade.draw_rectangle_filled(300, 90, 100, 100,
                                 arcade.color.ANTIQUE_BRONZE)
    arcade.draw_circle_filled(280, 78, 7, arcade.csscolor.BLACK)
    arcade.draw_circle_filled(320, 78, 7, arcade.csscolor.BLACK)
    arcade.draw_line(300, 140, 300, 40, arcade.color.BLACK)

    arcade.finish_render()

    # ensures window stays open until close
    arcade.run()

#Call the main function to get the program started.
main()