# Easy Pong Game in Python3 for Beginners
# By Fractured (Manager: Fran)
# Requirements: Have Python Installed (I am using Python 3.9.6) - link in desc

# Part 1: Setting up the window and Game Loop
# All episodes will be found on my Github - link in desc

# First we will import the turtle library which is what we will build our game from

import turtle
# This is easier than using pygame as it doesn't require any installing :)


# Now we will define our Width & Height
Width = 800 # Width of Window
Height = 600 # Height of Window

# We will now create our Screen & use the declared width/height to create it fully

win = turtle.Screen() # Name "win" whatever suits you - I have named it "win" for "window"
win.title("Pong Tutorial by Fran") # Sets our Title
win.bgcolor("black") # American spelling & Sets our background colour
win.setup(Width, Height) # Uses our declared variables to setup the window
win.tracer(0) # According to my notes this helps us control our game updates

# Main Game Loop
while True:
    win.update()
# While the game is running we constantly update!
# Lets test!
# The colour can be any colour! watch!
# We will be sticking with black
















# Lets recap:
# 1. We Imported "Turtle" lib which we will be building our game off of
# 2. We set the Width & Height to save space and to make them Constant Variables 
# 3. We setup the screen, the Title and the background colour.
# 4. We called the Width & Height and put them into our screen setup.
# 5. We used Tracer to help us control updates & set the Game Loop to constantly update the screen.



