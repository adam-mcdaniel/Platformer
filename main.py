from easy_mobile.setup import *

# Setup screen
screen = setup(
    level_width=1200,
    level_height=1000,
    title='Platformer'
)

# Define the Player type
# It inherits from Sprite
class Player(Sprite):
    def __init__(self, x, y):
        # Call the base class's constructor
        super().__init__(x, y, image="shroom.png")
        self.x_speed = 0
        self.y_speed = 0

    # Define a function to set the x speed
    def set_x_speed(self, x_speed):
        self.x_speed = x_speed

    # Define the update function that the screen will call
    def update(self, screen):
        
        # Accelerate downward due to gravity.
        self.y_speed -= 1
        # Limit the speed due to gravity to 12 pixels per update
        self.y_speed = max(-12, self.y_speed)

        # Move on the x axis
        self.move(self.x_speed, 0)
        # Check if you hit a block
        for entity in screen:
            self.check_collisions(self.x_speed, 0, entity)

        # Move on the y axis
        self.move(0, self.y_speed)
        # Check if you hit a block
        for entity in screen:
            self.check_collisions(0, self.y_speed, entity)
    
    def check_collisions(self, x_speed, y_speed, entity):
        # Collision logic
        if type(entity) == Block:
            if self.collide(entity):

                if x_speed > 0:
                    self.goto(
                        entity.getX() - self.getWidth(),
                        self.getY()
                        )
                elif x_speed < 0:
                    self.goto(
                        entity.getX() + entity.getWidth(),
                        self.getY()
                        )


                if y_speed > 0:
                    self.goto(
                        self.getX(),
                        entity.getY() - self.getHeight()
                        )
                elif y_speed < 0:
                    self.goto(
                        self.getX(),
                        entity.getY() + entity.getHeight()
                        )



class Block(Sprite):
    def __init__(self, x, y):
        super().__init__(x, y, image="block.png")


# Create a player
player = Player(500, 1000)
# Append player to screen
screen.append(player)


# List of block sprites
blocks = [
    Block(80, 700),
    Block(240, 700),
    Block(400, 700),
    Block(560, 700),


    Block(560, 400),
    Block(720, 400),
    Block(880, 400),


    Block(80, 100),
    Block(240, 100),
    Block(400, 100),
    ]

# Add blocks to screen
# The screen's add method takes a list
# and adds each element in the list to the screen
screen.add(blocks)

def event_loop():
    # focus camera on player
    screen.focus(player)

    # If the mouse is clicked
    if screen.getTouchDown():
        # If the mouse is on the left half of the screen
        if screen.getTouch().pos[0] < screen.getWidth()/2:
            # Go left
            player.set_x_speed(-10)
        # If the mouse is on the right half of the screen
        elif screen.getTouch().pos[0] > screen.getWidth()/2:
            # Go right
            player.set_x_speed(10)
    else:
        player.set_x_speed(0)


# Give screen the event_loop function to run
screen.run(event_loop)
