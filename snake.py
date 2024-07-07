from turtle import Turtle
STARTING_POSITION = [(0,0), (-20,0), (-40, 0)]
MOVING_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()


    def up(self):
        self.segments[0].seth(90)

    def down(self):
        self.segments[0].seth(270)

    def left(self):
        self.segments[0].seth(180)

    def right(self):
        self.segments[0].seth(0)


    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.setpos(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):

        for seg_num in range(int(len(self.segments)) - 1, 0, -1):
            new_xcor = self.segments[(seg_num - 1)].xcor()
            new_ycor = self.segments[(seg_num) - 1].ycor()
            self.segments[seg_num].goto(new_xcor, new_ycor)

        self.segments[0].forward(10)

