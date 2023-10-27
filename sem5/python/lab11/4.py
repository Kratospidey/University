class Shape:
    def __init__(self, sides):
        self.sides = sides

    def no_of_sides(self):
        print(f"Sides: {self.sides}")

    def two_dimensional(self):
        return True


class Square(Shape):
    def __init__(self, sides, colour):
        super().__init__(sides)
        self.colour = colour

    def no_of_sides(self):
        print(f"Sides: 4")

    def display_colour(self):
        print(f"Colour: {self.colour}")


def main():
    s = Square(4, "Blue")
    s.no_of_sides()
    s.display_colour()


main()
