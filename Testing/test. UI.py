# -- Set up the walls
# Create a row of boxes
for x in range(173, 650, 80):
    wall = arcade.Sprite("tile_0001.png",
                         SPRITE_SCALING)
    wall.center_x = x
    wall.center_y = 100
    self.wall_list.append(wall)
for x in range(173, 650, 80):
    wall = arcade.Sprite("tile_0001.png",
                         SPRITE_SCALING)
    wall.center_x = x
    wall.center_y = 550
    self.wall_list.append(wall)

# Create a column of boxes
for y in range(273, 500, 64):
    wall = arcade.Sprite("tile_0006.png",
                         SPRITE_SCALING)
    wall.center_x = 50
    wall.center_y = y
    self.wall_list.append(wall)
for y in range(273, 500, 64):
    wall = arcade.Sprite("tile_0010.png",
                         SPRITE_SCALING)
    wall.center_x = 300
    wall.center_y = y
    self.wall_list.append(wall)
for y in range(273, 500, 64):
    wall = arcade.Sprite("tile_0073.png",
                         SPRITE_SCALING)
    wall.center_x = 500
    wall.center_y = y
    self.wall_list.append(wall)
for y in range(273, 500, 64):
    wall = arcade.Sprite("tile_0001.png",
                         SPRITE_SCALING)
    wall.center_x = 700
    wall.center_y = y
    self.wall_list.append(wall)