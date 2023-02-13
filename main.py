from os import setegid
from turtle import Screen, Turtle, width
from snake import Snake
from scoreboard import Scoreboard
import time
from food import Food


screen = Screen()
food = Food()
scoreboard = Scoreboard()
# def turn_north():
    


screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Nokia Snake Game")
screen.tracer(0)

snake = Snake(width = 600, height=600)


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_continue = True

while game_continue:
    screen.update()  
    time.sleep(.2)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
        
        
    if snake.head.xcor()  < -300 or snake.head.xcor() > 280 or snake.head.ycor()  < -290 or snake.head.ycor() > 290:
        game_continue =  False
        scoreboard.game_over()
       
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif segment.distance(snake.head) < 15:
    #         game_continue =  False
    #         scoreboard.game_over()


        
       
        








screen.exitonclick()