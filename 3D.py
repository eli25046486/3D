import time
import numpy as np
from OpenGL.GL import *
import pygame

def pyopengl_circle(radius, segments):
    glBegin(GL_LINE_LOOP)
    for i in range(segments):
        theta = 2.0 * np.pi * i / segments
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        glVertex2f(x, y)
    glEnd()

def bresenham_circle(xc, yc, r):
    x, y = 0, r
    d = 3 - (2 * r)
    points = []

    while y >= x:
        points.extend([
            (xc + x, yc + y), (xc - x, yc + y),
            (xc + x, yc - y), (xc - x, yc - y),
            (xc + y, yc + x), (xc - y, yc + x),
            (xc + y, yc - x), (xc - y, yc - x)
        ])
        if d <= 0:
            d += 4 * x + 6
        else:
            d += 4 * (x - y) + 10
            y -= 1
        x += 1

    return points

def measure_time(function, *args):
    start_time = time.time()
    function(*args)
    end_time = time.time()
    return end_time - start_time

# Параметры теста: начнем с меньшего количества итераций
iterations = 1000
radius = 100

# Инициализация Pygame и окна OpenGL
pygame.init()
pygame.display.set_mode((800, 600), pygame.DOUBLEBUF | pygame.OPENGL)

# Тестирование алгоритма Брезенхема
bresenham_duration = measure_time(lambda: [bresenham_circle(0, 0, radius) for _ in range(iterations)])
print(f"Алгоритм Брезенхема: {bresenham_duration:.6f} секунд")

# Тестирование метода OpenGL
pyopengl_duration = measure_time(lambda: [pyopengl_circle(radius, 36) for _ in range(iterations)])
print(f"Метод OpenGL: {pyopengl_duration:.6f} секунд")

# Завершение и закрытие Pygame
pygame.quit()