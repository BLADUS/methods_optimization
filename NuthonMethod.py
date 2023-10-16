import sympy as sp

def newton_method():
    # Введите начальную точку и точность
    x0 = float(input("Введите начальную точку x0: "))
    tolerance = 0.0001

    # Определите символьную переменную x
    x = sp.symbols('x')

    # Введите производную функции с правильным синтаксисом
    f_prime_expression = input("Введите производную функции f'(x) (используйте 2*x вместо 2x): ")
    f_prime = sp.sympify(f_prime_expression)

    # Вычислите производную второго порядка f''(x)
    f_double_prime = sp.diff(f_prime, x)

    step = 1
    while True:
        # Вычислите значение производной f'(x0)
        f_prime_value = f_prime.subs(x, x0)

        # Вычислите значение производной второго порядка f''(x0)
        f_double_prime_value = f_double_prime.subs(x, x0)

        # Вычислите xk
        xk = x0 - f_prime_value / f_double_prime_value

        # Выведите информацию о текущем шаге
        print(f"Шаг {step}: xk = {xk}, f'(xk) = {f_prime_value}, f''(xk) = {f_double_prime_value}")

        # Проверьте условие остановки
        if abs(f_prime_value) < tolerance:
            print(f"Решение найдено: x = {xk}")
            break

        # Обновите x0 для следующего шага
        x0 = xk
        step += 1

if __name__ == "__main__":
    newton_method()
