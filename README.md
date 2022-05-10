# Graham-Hull-and-QuadTree-Images-Implementation

## Description of Graham-Hull and QuadTree Algrithms:
### Graham-Hull scan
It's algorithm which on the input takes given set of points on the plane. On the next step it creates the convex hull of the set points is the smallest convex for polygon. So algorithm, finds all vertices of the convex hull and marks out sides of created polygon. Complexity reaches _ _O(n logn)_ _ values.
### QuadTree
In short we can say that quadtree is a tree data sctructere in which every single node hase at moust 4 children. Quadtrees are the two-dimensional analog of octrees (https://en.wikipedia.org/wiki/Octree/). The idea is pretty simple. We divide our 2D plane recursively into four quadrants or regions under condition only if in our subrectangle we can find more than 4 points and it's on and on until condition is false - boolean 0. Complexity is also _ _O(n logn)_ _.

Graham-Hull is being used in for instance in **collision avoidance** or all kinda of **shape analysis**. On the other hand QuadTree is implemented for example in **image compression**, but also in **satellite maps - Google Maps**.

## Requirements:
Project has been done in [PyCharm University Edition] https://www.jetbrains.com/pycharm-edu/.
- Version of Python: Python 3
- Used libraries:
```Python
pip install random
pip install tkinter 
pip install math
```
## Usage:
To run program just compile **Main - DRIVE CODE.py**. In **ConvexHull.py** fille it will draw 7 points in certain cloud point from 0 to 100 values. Every single coordinate will, argument and values, will be from range 0 to 100. You can easily change it simply by putting other values into arguments of `sample(range(from, to), no_points)`. Number of clouds you can change in **Main - DRIVE CODE.py** file being set as `n` variable.
GUI part is not being finished so if window pops out DO NOT click `Exit.` button cause it will shut down whole program. Simply close window using:

![X](https://user-images.githubusercontent.com/92062717/167656438-2eb18b75-3373-4f00-acdc-d07a94898910.png)

After closing GUI window. The final view will pop out on your screen in another window or will pop out in `SciView` section on the right side of your screen (***Pycharm!!!***) in .png format.
Compiler will print last list of points of certain convex and dictionary whose keys are natural numbers from 0 to n where n means number of clouds as well ass values which are lists of tuples. For example if we declare 10 clouds, we will get keys 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 so 10 keys. And every key will get it's own list of tuples.
## Example:
10 clouds are being created where argumenst and values are being drawn from range 11 to 135. Every list contains 7 points, and there are 7 clouds - <0, 7).

![Example](https://user-images.githubusercontent.com/92062717/167663019-39eeb97f-d0cb-4bf8-af12-283a0d9564f5.png)

## Authors:
AGH University of Tehcnology students, Poland 2022.
- Szymon Rogowski
- Hubert Piskorski
