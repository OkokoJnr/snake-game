from turtle import Turtle
class Snake:
    def __init__(self):
        self.positions = [(0,0), (-20,0), (-40,0)]
        self.segments = []
        self.create_snake()
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
            