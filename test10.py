import turtle
import time
import random

# Setup the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

# Game state
paused = False

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Normal food (π)
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0, 100)
food.hideturtle()
food.write("π", align="center", font=("Courier", 24, "normal"))

# Special food (X)
special_food = turtle.Turtle()
special_food.speed(0)
special_food.shape("square")
special_food.color("blue")
special_food.penup()
special_food.goto(0, -100)
special_food.hideturtle()
special_food.write("X", align="center", font=("Courier", 24, "normal"))

# Snake body segments
segments = []

# Obstacles
obstacles = []

# Score
score = 0
high_score = 0

# Pen for score display
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions to control the snake
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def toggle_pause():
    global paused
    paused = not paused

# Keyboard bindings
wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")
wn.onkey(toggle_pause, "space")

# Generate obstacles
def generate_obstacles():
    num_obstacles = int(0.05 * (600 // 20) * (600 // 20) / 5)
    for _ in range(num_obstacles):
        horizontal = random.choice([True, False])
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        current_obstacle = []
        for i in range(5):
            obstacle = turtle.Turtle()
            obstacle.speed(0)
            obstacle.shape("square")
            obstacle.color("gray")
            obstacle.penup()
            if horizontal:
                obstacle.goto(x + i * 20, y)
            else:
                obstacle.goto(x, y + i * 20)
            current_obstacle.append(obstacle)
        obstacles.append(current_obstacle)

# Check for collision with obstacles
def check_obstacle_collision():
    for obstacle_group in obstacles:
        for obstacle in obstacle_group:
            if head.distance(obstacle) < 20:
                return True
    return False

# Main game loop
generate_obstacles()
while True:
    wn.update()

    if not paused:
        # Check for collision with the border
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        # Check for collision with obstacles
        if check_obstacle_collision():
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        # Check for collision with the food
        if head.distance(food) < 20:
            # Move the food to a random spot
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.clear()
            food.goto(x, y)
            food.write("π", align="center", font=("Courier", 24, "normal"))

            # Add a segment to the snake
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("grey")
            new_segment.penup()
            segments.append(new_segment)

            # Increase the score
            score += 10
            if score > high_score:
                high_score = score

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        # Check for collision with the special food
        if head.distance(special_food) < 20:
            # Move the special food to a random spot
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            special_food.clear()
            special_food.goto(x, y)
            special_food.write("X", align="center", font=("Courier", 24, "normal"))

            # Shrink the snake if its length is greater than 1
            if len(segments) > 1:
                segments.pop()

            # Decrease the score
            score -= 5
            if score < 0:
                score = 0
            if score > high_score:
                high_score = score

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        # Move the end segments first in reverse order
        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].goto(x, y)

        # Move segment 0 to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)

        move()

        # Check for head collision with body segments
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"

                # Hide the segments
                for segment in segments:
                    segment.goto(1000, 1000)

                # Clear the segments list
                segments.clear()

                # Reset the score
                score = 0
                pen.clear()
                pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        time.sleep(0.1)

wn.mainloop()
