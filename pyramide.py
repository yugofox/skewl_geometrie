import math


def pyramid_scanner(a, h):
    G = a ** 2
    h_a = math.sqrt(h ** 2 + (a / 2) ** 2)
    M = 2 * a * h_a
    O = G + M
    V = 1 / 3 * G * h

    if h > a:
        status = "STEEP_STRUCTURE"
    elif h == a:
        status = "BALANCED_STRUCTURE"
    else:
        status = "LOW_STRUCTURE"

    print("=== PYRAMIDEN RECHNER ===")
    print("STATUS:", status)
    print("-----------------------")
    print("Grundkante a:", a, "cm")
    print("Körperhöhe h:", h, "cm")
    print("TRACE: h_a² = h² + (a/2)²")
    print("Seitenhöhe h_a:", round(h_a, 2), "cm")
    print("-----------------------")
    print("Grundfläche G:", round(G, 2), "cm²")
    print("Mantelfläche M:", round(M, 2), "cm²")
    print("Oberfläche O:", round(O, 2), "cm²")
    print("Volumen V:", round(V, 2), "cm³")


pyramid_scanner(8, 12)
