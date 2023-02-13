from turtle import Turtle, width

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:

    def __init__(self, width, height):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.width = width
        self.height = height
        
    def create_snake(self):
       
        x= -240
        y=190

        for _ in range(3):
            
            self.add_segment(x,y)
            x-= -20
        
    def move(self):
        
        for seg in range(len(self.segments) - 1, 0, -1):
            self.segments[seg].goto(self.segments[seg - 1].pos())
        self.head.forward(20)
        
    def add_segment(self, x_axis, y_axis):
        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.setposition(x_axis,y_axis)
        self.segments.append(new_seg)
       

    def extend(self):
        self.add_segment(self.segments[-1].xcor(), self.segments[-1].ycor())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP) 

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN) 

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT) 

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT) 
       
    