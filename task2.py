import scipy.integrate as spi
import numpy as np


# Визначення функції та межі інтегрування
def func(x):
    return x**2


func_str = "x^2"

a = 0  # Нижня межа
b = 2  # Верхня межа
y_low = 0
y_up = 4


def monte_carlo(func, x_low, x_up, y_low, y_up, n):
    x = np.random.uniform(x_low, x_up, n)
    y = np.random.uniform(y_low, y_up, n)

    under_curve = np.sum(y < func(x))
    area = (x_up - x_low) * (y_up - y_low) * (under_curve / n)

    return area


def main():
    # Обчислення інтеграла за допомогою методу Монте-Карло
    print("Результати обчислень за допомогою методу Монте-Карло:")
    print("Кількість точок: 1_000_000")

    mc_result = monte_carlo(func, a, b, y_low, y_up, 1_000_000)
    print("Інтеграл: ", format(mc_result, ".6f"))

    print("\n")

    # Обчислення інтеграла за допомогою бібліотеки scipy.integrate
    spi_result, error = spi.quad(func, a, b)

    print("Результати обчислень за допомогою бібліотеки scipy.integrate:")
    print("Інтеграл: ", spi_result)
    print("Похибка: ", format(error, ".20f"))


if __name__ == "__main__":
    main()
