class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22 / 7) * (self.radius**2)

    def perimeter(self):
        return 2 * (22 / 7) * self.radius


def main():
    rad = int(input("Radius: "))

    c = Circle(rad)

    print(f"Area: {c.area():.3f}")
    print(f"Perimeter: {c.perimeter():.3f}")


main()
