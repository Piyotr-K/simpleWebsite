import turtle
import os
import winsound
import math
import random
from pygame import mixer

def move_left():
    global player, playerspeed
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    global player, playerspeed
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    global bulletstate, bullet, player
    if bulletstate == "ready":
        #os.system("afplay laser.wav&")
        winsound.PlaySound("laser.wav", winsound.SND_ASYNC)
        bulletstate = "fire"
        # Move the bullet to just above the player.
        x = player.xcor()
        y = player.ycor()
        bullet.setpos(x, y)
        bullet.st()

def isCollision(t1, t2):
    # Distance between 2 points from MATH
    x_diff = t1.xcor() - t2.xcor()
    y_diff = t1.ycor() - t2.ycor()
    distance = math.sqrt(math.pow(x_diff, 2) + math.pow(y_diff, 2))
    if distance < 15:
        return True
    else:
        return False

# Screen setup
wn = turtle.Screen()
wn.setup(800, 800)
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("space_invaders_background.gif")

# Register our own custom images
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

# Draw Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.pu()
border_pen.setposition(-300,-300)
border_pen.pd()
border_pen.pensize(3)

for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.ht()

# Score
score = 0

# Display the score on screen
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: {}".format(score)
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.ht()

# Make a new player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

# Enemies
number_of_enemies = 5
# Create an empty list of enemies
enemies = []

# Add enemies to the list
for i in range(number_of_enemies):
    # Create the enemy
    enemies.append(turtle.Turtle())

# Give the enemies appearance
for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.pu()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

# Enemy's movement speed
enemyspeed = 2

# Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.pu()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.ht()

bulletspeed = 20

# Define bullet state
# If the state is ready, the bullet will fire
# If not, the bullet will not
bulletstate = "ready"

# Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

mixer.init()
mixer.music.load('AmberCanvas.mp3')
mixer.music.play()

while True:

    for enemy in enemies:
        # Move enemies
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # If enemies hit the right most of the screen
        if enemy.xcor() > 280:
            # Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change enemy direction
            enemyspeed *= -1
        
        # If enemies hit the left most of the screen
        if enemy.xcor() < -280:
            # Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change enemy direction
            enemyspeed *= -1
        
        # If the enemies hit the bottom of the screen
        if enemy.ycor() < -250:
            print("Game Over")
            os.sys.exit()
        
        # Check for collision between a bullet and the enemy
        if isCollision(bullet, enemy):
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            # Reset bullet
            bullet.ht()
            bulletstate = "ready"
            bullet.setpos(0, -400)
            # Reset the enemy hit
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setpos(x, y)
            # Update the score
            score += 10
            scorestring = "Score: {}".format(score)
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
        
        # Check for collision between the player and an enemy
        if isCollision(player, enemy):
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            player.ht()
            enemy.ht()
            print("Game Over")
            os.sys.exit()
    
    # Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
    
    # Check to see if the bullet has gone to the top of the screen
    if bullet.ycor() > 275:
        bullet.ht()
        bulletstate = "ready"
