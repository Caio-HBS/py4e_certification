class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return diagonal

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        lines = self.height
        columns = self.width
        
        picture = "*" * columns + "\n"
        picture *= lines
        return picture

    def get_amount_inside(self, shape):
        fit_inside = self.get_area() // shape.get_area()
        return fit_inside


class Square(Rectangle):
    def __init__(self, length):
        self.width = length
        self.height = length

    def __str__(self):
        return f"Square(side={self.width})"
    
    def set_side(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side
    
    def set_width(self, side):
        self.width = side
        self.height = side


rect = Rectangle(5, 10)
print("Get area:",rect.get_area())
rect.set_width(3)
print("Get perimeter:",rect.get_perimeter())
print("Rectangle:", rect)

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)