import matplotlib.pyplot as plt
import numpy as np
from task2 import func, func_str, a, b


def main():
    # Створення діапазону значень для x
    x = np.linspace(a - 0.5, b + 0.5, 400)
    y = func(x)

    # Створення графіка
    _, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, "r", linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = func(ix)
    ax.fill_between(ix, iy, color="gray", alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color="gray", linestyle="--")
    ax.axvline(x=b, color="gray", linestyle="--")
    ax.set_title(f"Графік інтегрування f(x) = {func_str} від {a} до {b}")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
