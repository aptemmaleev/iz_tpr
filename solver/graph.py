import numpy as np

from matplotlib import pyplot as plt   

# Найти точку пересечения двух прямых
def get_intersect(a1, a2, b1, b2):
    """ 
    a1: [x, y] a point on the first line
    a2: [x, y] another point on the first line
    b1: [x, y] a point on the second line
    b2: [x, y] another point on the second line
    """
    s = np.vstack([a1,a2,b1,b2])        # s for stacked
    h = np.hstack((s, np.ones((4, 1)))) # h for homogeneous
    l1 = np.cross(h[0], h[1])           # get first line
    l2 = np.cross(h[2], h[3])           # get second line
    x, y, z = np.cross(l1, l2)          # point of intersection
    if z == 0:                          # lines are parallel
        return (float('inf'), float('inf'))
    return (x/z, y/z)

# Получить прямые из матрицы
def convert_matrix_to_lines(matrix):
    lines = []
    for row in matrix:
        lines.append((([0, row[0]], [1, row[1]])))
    return lines

# Поулчить точки пересечений отрезков
def get_lines_intersect(lines: list):
    points = list()
    for i in range(len(lines) - 1):
        for j in range(1, len(lines)):
            point = get_intersect(*lines[i], *lines[j])
            if point[0] == float("inf"):
                continue
            if 0 <= point[0] <= 1:
                points.append(point)
    return points

# Поулчаем нижнюю точку     
def lower_y_point(points: list):
    lower_point = (0, 99999)
    for point in points:
        if lower_point[1] > point[1]:
            lower_point = point
    print(lower_point)
    return lower_point

# Получаем верхнюю точку     
def upper_y_point(points: list):
    upper_point = (0, -99999)
    for point in points:
        if upper_point[1] < point[1]:
            upper_point = point
    return upper_point

# Проверить матрицу
def validate_matrix(matrix):
    if min(len(matrix), len(matrix[0])) != 2:
        return False
    return True

# Перевертнуть матрицу на 90 градусов
def rotate_90_degree(matrix):
    new_matrix = []
    for i in range(len(matrix[0]), 0, -1):
        new_matrix.append(list(map(lambda x: x[i-1], matrix)))
    return new_matrix

def rotate_270_degree(matrix):
    matrix = rotate_90_degree(matrix)
    matrix = rotate_90_degree(matrix)
    return rotate_90_degree(matrix)

# Нарисовать график
def draw_graph(matrix, player=1):
    rotated = False
    # Проверяем матрицу
    if not validate_matrix(matrix):
        raise ValueError('Matrix should be 2xN or Nx2 size')
    if player == 2:
        rotated = True
        matrix = rotate_90_degree(matrix)
    
    # Доп. Переменные
    x_values = [0, 1]
    y_pad = 1
    fig, ax = plt.subplots()
    
    # Определяем размеры для графика
    max_height = -99999
    min_height = 99999
    for row in matrix:
        max_height = max(max_height, *row)
        min_height = min(min_height, *row)
    if min_height > 0:
        min_height = 0
    max_height += 3
    min_height -= 3

    # Рисуем вертикальные и горизонтальную прямые
    for x in x_values:
        ax.plot([x, x], [min_height, max_height], color='black')
    ax.plot([0, 1], [0, 0], color='black')

    # Отображаем прямые из матрицы
    for i in range(len(matrix)):
        ax.plot([0, 1], matrix[i])
        if rotated:
            ax.text(-0.05, matrix[i][0], f'b{i+1}', color='gray')
            ax.text(1, matrix[i][1], f'b{i+1}', color='gray')
        else:
            ax.text(-0.05, matrix[i][0], f'a{i+1}', color='gray')
            ax.text(1, matrix[i][1], f'a{i+1}', color='gray')

    # Получаем точки пересечений линий
    lines = convert_matrix_to_lines(matrix)
    points = get_lines_intersect(lines)

    # Находим нижнюю точку
    if rotated:
        max_point = upper_y_point(points)
    else:
        max_point = lower_y_point(points)

    # Рисуем линию до точки оси X
    ax.text(max_point[0] + 0.01, max_point[1] - 2, f'V*={round(max_point[1], 2)}', color='red', fontsize=8)
    ax.plot([max_point[0], max_point[0]], [0, max_point[1]], linestyle = 'dotted', linewidth = 2, color='red')
    ax.scatter(x=max_point[0], y=max_point[1], c='r', linewidths=0.5)

    # Вид графика
    ax.set_xlim(-0.1, max(x_values) + 0.1)  # Установка границ по оси X
    ax.set_ylim(-y_pad + min_height, max_height + y_pad)  # Установка границ по оси Y
    
    # Выводим ответ на графике
    P2 = (1 - max_point[0]) / 1
    P1 = (max_point[0]) / 1
    ax.set_xlabel(f'V*={max_point[1]:.2f}; P = ({P2:.2f}, {P1:.2f})')
    if not rotated:
        ax.set_title('II Игрок')
    else:
        ax.set_title('I Игрок')

    plt.show(block=False)
