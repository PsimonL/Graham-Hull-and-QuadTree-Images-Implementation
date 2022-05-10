from math import acos
from math import dist
from math import sqrt
from random import sample


def convex_hull(n):
    for i in range(n):
        list_of_x = sample(range(11, 135), 7)
        list_of_y = sample(range(11, 135), 7)
        # list_of_x = [-81, 68, 27, -47, -24, 38, -6, -76, 20, -8]
        # list_of_y = [43,-93, 10,-76,-71, -66, 26, -33, 4, -89]
        # list_of_x = [3, 5, 2, 6, 4, 2]
        # list_of_y = [1, 1, 2, 3, 4, 0]

        entry_list = list(zip(list_of_x, list_of_y))
        # print("Lista punktow: ", entry_list)
        entry_list.sort()
        # print("Posortowana lista punktow: ", entry_list)

        vector_x = entry_list[0][0]
        vector_y = entry_list[0][1]
        list_points_x = []
        list_points_y = []
        for i in range(len(entry_list)):
            if entry_list[i][0] - vector_x < 0:
                list_points_x.append(-(entry_list[i][0] - vector_x))
            else:
                list_points_x.append(entry_list[i][0] - vector_x)

            if entry_list[i][1] - vector_y < 0:
                list_points_y.append(-(entry_list[i][1] - vector_y))
            else:
                list_points_y.append(entry_list[i][1] - vector_y)

        list_of_points = list(zip(list_points_x, list_points_y))
        # print("Lista punktow z sr uk w (0, 0) - list_of_points:", list_of_points)

        x_0 = entry_list[0][0] - vector_x
        y_0 = entry_list[0][1] - vector_y
        degree_list = []
        distance_list = []

        for i in range(1, len(entry_list)):
            x = list_of_points[i][0]
            y = list_of_points[i][1]
            tuple_of_0_0 = (x_0, y_0)
            tuple_of_points = (x, y)
            distance = dist(tuple_of_0_0, tuple_of_points)
            distance_list.append(distance)
            # vec_0 = (0 , -1)
            vec_0_x = 0
            vec_0_y = -1
            #length_of_vec_0 = 1

            #vec_i = (x, y)
            #vec_i_x = x
            #vec_i_y = y

            #scalar_product
            scalar_product = vec_0_x * x + vec_0_y * y
            length_of_vec_i = sqrt(x*x + y*y)
            value = scalar_product/length_of_vec_i
            alfa = acos(value)
            temp_degrees = (180 * alfa) / 3.14
            if temp_degrees < 0:
                temp_degrees = -temp_degrees
            degree_list.append(temp_degrees)

        # print(degree_list)
        # print(distance_list)

        del list_of_points[0]
        list_pom = list(zip(list_of_points, degree_list))
        list_pom.sort(key=lambda x: x[1])
        list_3_elems = list_pom
        # print("list_3_elems lista: ", list_3_elems)
        final_list = []
        for i in list_3_elems:
            final_list.append(i[0])
        final_list.insert(0, (0, 0))
        final_list.append((0, 0))
        # print("Finala lista to: ", final_list)

        convex_list = []
        lista_srodka = []
        for i in range(1, len(final_list)-1, 1):
            # print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            tail = final_list[i-1]
            # print("Poczatek wektora: ", tail)
            medium = final_list[i]
            # print("Wartosc srodkowa: ", medium)
            head = final_list[i+1]
            # print("Koniec wektora: ", head)
            # print("Dzialam dla iteracji o numerze  i = ", i)

            xt = tail[0]
            yt = tail[1]
            xm = medium[0]
            ym = medium[1]
            xh = head[0]
            yh = head[1]

            det = xt * yh + xh * ym + xm * yt - xm * yh - xt * ym - xh * yt
            if det < 0:
                # print("Punkt znajduje sie z prawej strony wektora")
                convex_list.append(medium)
            elif det > 0:
                # print("Punkt znajduje sie z lewej strony wektora")
                pass

        convex_list.insert(0, (0, 0))
        convex_list.append((0, 0))
        print("=======================================================")
        #print("Lista otoczki: ", convex_list)

        return convex_list


def draw(dictionary, axis):
    for i in range(1, len(dictionary), 1):
        list_dic = dictionary[i]
        list_of_X, list_of_Y = map(list, zip(*list_dic))
        axis.fill(list_of_X, list_of_Y, c="orange")
