import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


# Визначення функції та межі інтегрування
def f(x):
    return x**2


def monte_carlo_integrate(func, a, b, y_min, y_max, num_points):
    x = np.random.uniform(a, b, num_points)
    y = np.random.uniform(y_min, y_max, num_points)
    under_curve = np.sum(y < func(x))
    area = (b - a) * (y_max - y_min) * (under_curve / num_points)
    return area


if __name__ == "__main__":
    a = 0  # Нижня межа
    b = 2  # Верхня межа

    # Обчислення інтеграла за допомогою quad
    result, error = spi.quad(f, a, b)

    print("Інтеграл, визначений за допомогою quad: ", result, error)

    mc_result = monte_carlo_integrate(f, a, b, 0, 4, 100_000)
    print(
        "Інтеграл, визначений за допомогою методу Монте-Карло з 100_000 випробуваннями: ",
        mc_result,
    )

    mc_result2 = monte_carlo_integrate(f, a, b, 0, 4, 1_000_000)
    print(
        "Інтеграл, визначений за допомогою методу Монте-Карло з 1_000_000 випробуваннями: ",
        mc_result2,
    )

    mc_result3 = monte_carlo_integrate(f, a, b, 0, 4, 10_000_000)
    print(
        "Інтеграл, визначений за допомогою методу Монте-Карло з 10_000_000 випробуваннями: ",
        mc_result3,
    )

    # Створення діапазону значень для x
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, "r", linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color="gray", alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color="gray", linestyle="--")
    ax.axvline(x=b, color="gray", linestyle="--")
    ax.set_title("Графік інтегрування f(x) = x^2 від " + str(a) + " до " + str(b))
    plt.grid()
    plt.show()
