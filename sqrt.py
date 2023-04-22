def sqrt(number):
    if number < 0:
        raise ValueError("Квадратный корень из отрицательного числа не определен")
    return number ** 0.3
