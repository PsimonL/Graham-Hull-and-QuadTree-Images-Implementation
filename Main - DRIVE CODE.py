import matplotlib.pyplot as plt
from math import sqrt
from Rectangle_if_4_points import Rectangle
from QuadTree import Quadtree
from ConvexHull import draw
from ConvexHull import convex_hull
from GUI import gui_for_project

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanceToCenter(self, center):
        distance = sqrt((center.x - self.x)*(center.x - self.x)
                        + (center.y - self.y)*(center.y - self.y))
        return distance

class Start:
    def __init__(self, dictionary):
        width, height = 100, 100

        list_of_ps = []
        for each in dictionary.values():
            for point in each:
                list_of_ps.append(Point(point[0], point[1]))

        domain = Rectangle(Point(width / 2, height / 2), width / 2, height / 2)
        qtree = Quadtree(domain)

        for point in list_of_ps:
            qtree.insert(point)
        #print("Total list_of_ps: ", len(qtree))

        # Drawing qt
        draw(dictionary, plt.subplot())
        plt.subplot().set_xlim(0, width)
        plt.subplot().set_ylim(0, height)

        # Drawing rectangles
        qtree.draw(plt.subplot())
        # Drawing list_of_ps of all
        plt.subplot().scatter([p.x for p in list_of_ps], [p.y for p in list_of_ps], s=4)

        plt.axis('off')
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    n = 7
    i = 0
    dictionary = {}

    while i < n:
        dictionary[i] = []
        convex_list = convex_hull(n)
        print("Main print: ", convex_list)
        dictionary[i] = convex_list
        i += 1
    print(dictionary)

    gui_for_project()
    Start(dictionary)
