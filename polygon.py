class Polygon:

    def __init__(self):
        pass

    def get_area(self):
        raise NotImplementedError(
            "This method should be overridden by subclasses")

    def get_perimeter(self):
        raise NotImplementedError(
            "This method should be overridden by subclasses")

    def get_picture(self):
        raise NotImplementedError(
            "This method should be overridden by subclasses")

    def get_amount_inside(self, shape):
        return int(self.get_area() / shape.get_area())
