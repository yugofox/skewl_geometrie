import math
import numpy as np
import matplotlib.pyplot as plt


def cone_scanner(r, h):
    theta = np.linspace(0, 2 * math.pi, 50)
    z = np.linspace(0, h, 30)

    T, Z = np.meshgrid(theta, z)
    R = r * (1 - Z / h)

    X = R * np.cos(T)
    Y = R * np.sin(T)

    s = math.sqrt(r ** 2 + h ** 2)
    G = math.pi * r ** 2
    M = math.pi * r * s
    O = G + M
    V = 1 / 3 * G * h

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    ax.plot_surface(X, Y, Z, alpha=0.5, edgecolor="black")
    ax.plot([0, 0], [0, 0], [0, h], linestyle="--")
    ax.plot([r, 0], [0, 0], [0, h])

    ax.set_title("SIGMA_SCAN: Kegel")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    print("=== CONE SCANNER ===")
    print("")
    print("Radius r:", r, "cm")
    print("Höhe h:", h, "cm")
    print("Mantellinie s:", round(s, 2), "cm")
    print("Grundfläche G:", round(G, 2), "cm²")
    print("Mantelfläche M:", round(M, 2), "cm²")
    print("Oberfläche O:", round(O, 2), "cm²")
    print("Volumen V:", round(V, 2), "cm³")

    plt.show()


cone_scanner(4, 9)
