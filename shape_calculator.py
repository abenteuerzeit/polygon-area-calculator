from rectangle import Rectangle
from square import Square

if __name__ == "__main__":
    r = Rectangle(5, 10)
    print(r.get_area())
    print(r.get_perimeter())
    s = Square(9)
    print(s.get_area())
    print(s.get_perimeter())
    print(s.get_picture())
