# coding: utf-8
# license: GPLv3
from solar_stats import *
from solar_main import get_physical_time
gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.
    **space_objects** — список объектов, которые воздействуют на тело.
    """
    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!
        if obj.type == 'star':
            add_stats(body, obj)
            print(get_physical_time())
        r = ((body.x - obj.x)**2 + (body.y - obj.y)**2)**0.5
        body.Fx +=  gravitational_constant*body.m*obj.m*(1/r**2)*((obj.x - body.x)/r)
        body.Fy += gravitational_constant*body.m*obj.m*(1/r**2)*((obj.y - body.y)/r)
        print(physical_time)
        #print(body.Fx)
        #print(body.Fy)


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """

    ax = body.Fx/body.m
    body.x += body.Vx*dt + (ax/2)*dt**2
    body.Vx += ax*dt
    ay = body.Fy/body.m
    body.y += body.Vy*dt + (ay/2)*dt**2
    body.Vy += ay*dt



def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
