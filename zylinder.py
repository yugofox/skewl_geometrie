import math

def simulate_cylinder_volume(r, h, precision=0.0001): #stackt unendlich veiele dünne Zylinderscheiben
    total_volume = 0
    current_h = 0
    

    while current_h < h:

        layer_area = math.pi * (r**2)
        

        total_volume += layer_area * precision
        current_h += precision
        
    return round(total_volume, 2)


radius = 6
height = 7
result = simulate_cylinder_volume(radius, height)

print(f"Status: yayy, gescchaft! :3 | Volumen: {result}")

