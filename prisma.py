import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def plot_prism(base_points, height):
    bottom_points = []
    top_points = []

    for x, y in base_points:
        bottom_points.append([x, y, 0])
        top_points.append([x, y, height])

    faces = []

    faces.append(bottom_points)
    faces.append(top_points)

    number_of_points = len(base_points)

    for i in range(number_of_points):
        next_i = (i + 1) % number_of_points

        side_face = [
            bottom_points[i],
            bottom_points[next_i],
            top_points[next_i],
            top_points[i]
        ]

        faces.append(side_face)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    ax.add_collection3d(
        Poly3DCollection(faces, alpha=0.5, edgecolor="black")
    )

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    ax.set_xlim(-1, 4)
    ax.set_ylim(-1, 4)
    ax.set_zlim(0, height + 1)

    plt.show()

square = [
    [0, 0],
    [2, 0],
    [2, 2],
    [0, 2]
]

pentagon = [
    [1, 0],
    [2.5, 1],
    [2, 2.5],
    [0, 2.5],
    [-0.5, 1]
]
#plot_prism(square, 3)
plot_prism(pentagon, 3)

