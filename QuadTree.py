from Rectangle_if_4_points import Rectangle
from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_center(self, center):
        distance = sqrt((center.x - self.x)*(center.x - self.x)
                        + (center.y - self.y)*(center.y - self.y))
        return distance

class Quadtree:
    def __init__(self, boundary, capacity=1):
        self.boundary = boundary
        self.capacity = capacity
        self.points = []
        self.divided = False

    def insert(self, point):
        # if the point is in the range of current quadtree
        if not self.boundary.containsPoint(point):
            return False
        # if has not reached capacity
        if len(self.points) < self.capacity:
            self.points.append(point)
            return True
        if not self.divided:
            self.divide()
            self.divided = True
        if self.north_west.insert(point):
            return True
        elif self.north_east.insert(point):
            return True
        elif self.south_west.insert(point):
            return True
        elif self.south_east.insert(point):
            return True
        return False

    def query_range(self, range):
        found_points = []
        if not self.boundary.intersects(range):
            return []
        for point in self.points:
            if range.containsPoint(point):
                found_points.append(point)
        if self.divided:
            found_points.extend(self.north_west.query_range(range))
            found_points.extend(self.north_east.query_range(range))
            found_points.extend(self.south_west.query_range(range))
            found_points.extend(self.south_east.query_range(range))
        return found_points

    def query_radius(self, range, center):
        list_of_foung_points = []
        if not self.boundary.intersects(range):
            return []
        for point in self.points:
            if range.containsPoint(point) and point.distance_to_center(center) <= range.width:
                list_of_foung_points.append(point)
        if self.divided:
            list_of_foung_points.extend(self.north_west.query_radius(range, center))
            list_of_foung_points.extend(self.north_east.query_radius(range, center))
            list_of_foung_points.extend(self.south_west.query_radius(range, center))
            list_of_foung_points.extend(self.south_east.query_radius(range, center))
        return list_of_foung_points

    def divide(self):
        center_x = self.boundary.center.x
        center_y = self.boundary.center.y
        new_width = self.boundary.width / 2
        new_height = self.boundary.height / 2

        nw = Rectangle(Point(center_x - new_width, center_y - new_height), new_width, new_height)
        self.north_west = Quadtree(nw)
        ne = Rectangle(Point(center_x + new_width, center_y - new_height), new_width, new_height)
        self.north_east = Quadtree(ne)
        sw = Rectangle(Point(center_x - new_width, center_y + new_height), new_width, new_height)
        self.south_west = Quadtree(sw)
        se = Rectangle(Point(center_x + new_width, center_y + new_height), new_width, new_height)
        self.south_east = Quadtree(se)

    def __len__(self):
        count = len(self.points)
        if self.divided:
            count += len(self.north_west) + len(self.north_east) + len(self.south_east) + len(self.south_west)
        return count

    def draw(self, ax):
        self.boundary.draw(ax)
        if self.divided:
            self.north_west.draw(ax)
            self.north_east.draw(ax)
            self.south_west.draw(ax)
            self.south_east.draw(ax)
