class shape:
    def draw(self):
        print("drawing a shape")

class rectangle(shape):
    def draw(self):
        print("drawing a rectangle")


class square(shape):
    def draw(self):
        print("drawing a square")

sh = shape()
sh.draw()

r = rectangle()
r.draw()

s = square()
s.draw()