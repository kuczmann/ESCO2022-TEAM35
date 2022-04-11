from digital_twin_distiller import geometry
from digital_twin_distiller.objects import Rectangle


def add_turn(geo, current, x0, y0):
    w = 3.  # mm
    h = 10.  # mm

    rect = Rectangle(x0, y0, width=w, height=h)

    geo.add_rectangle(rect)

    return


if __name__ == '__main__':
    geo = geometry.Geometry()
    add_turn(geo, 0, 0, 0)
    print(geo)
