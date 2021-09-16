"""
This is a sample program to show how to draw using Python and the Arcade library.
"""
import arcade
#opens window
arcade.open_window(600, 600, "drawing example")
arcade.set_background_color((197, 241, 250))
arcade.start_render()
#will draw the base of the Belfast City Hall
arcade.draw_ellipse_filled(300, 5, 200, 100, arcade.csscolor.WHITE)
arcade.draw_lrtb_rectangle_filled(0, 599,300, 0, arcade.color.WHITE)
arcade.draw_lrtb_rectangle_filled(0, 599, 40, 0, arcade.color.GREEN)
arcade.draw_rectangle_filled(50, 300, 200, 250, arcade.color.WHITE)
arcade.draw_lrtb_rectangle_filled(200, 400, 500, 100, arcade.color.WHITE)
arcade.draw_rectangle_filled(550, 300, 200, 250, arcade.color.WHITE)
#will draw the oxididsed domes atop the city hall
arcade.draw_arc_filled(535, 400, 175, 200, arcade.csscolor.AQUAMARINE, 0, 180)
arcade.draw_arc_filled(64, 400, 175, 200, arcade.csscolor.AQUAMARINE, 0, 180)
arcade.draw_arc_filled(300, 500, 200, 200, arcade.csscolor.AQUAMARINE, 0, 180)
#will draw a sun in the top corner
arcade.draw_circle_filled(500, 550, 40, arcade.color.YELLOW)
arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3)
arcade.finish_render()
#ensures window stays open until close
arcade.run()