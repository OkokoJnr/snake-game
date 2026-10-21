from turtle import Turtle
class Snake:
    def __init__(self):
        self.positions = [(0,0), (-20,0), (-40,0)]
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_segment(self):
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        return segment
    def create_snake(self):
        for position in self.positions:
            segment = self.create_segment()
            segment.goto(position)
            self.segments.append(segment)
    def move(self):
        segments_lengths = len(self.segments)-1
        for seg_num in range(segments_lengths, 0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)