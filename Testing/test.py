"""
This is a sample program to show how to draw using Python and the Arcade library.
"""
import arcade
#opens window
arcade.open_window(800, 800, "drawing example")
arcade.set_background_color((197, 241, 250))
arcade.start_render()
arcade.finish_render()
#ensures window stays open until close
arcade.run()



