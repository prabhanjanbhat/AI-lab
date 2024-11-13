import math
import random

def objective_function(x):
    return x**2+2*x+1

def acceptance_function(T, delta_E):
    if delta_E < 0:
        return True
    else:
        r = random.random()
        return r < math.exp(-delta_E / T)

def simulated_annealing(T_max, T_min, E_th, alpha):
    T = T_max
    x = random.uniform(-10, 10)
    E = objective_function(x)

    best_solution = x
    best_energy = E
    iteration_count = 0

    while T > T_min and E > E_th:
        x_new = x + random.uniform(-1, 1)
        E_new = objective_function(x_new)
        delta_E = E_new - E

        if acceptance_function(T, delta_E):
            x = x_new
            E = E_new

            if E < best_energy:
                best_solution = x
                best_energy = E

        T *= alpha
        iteration_count += 1

    return best_solution, best_energy, iteration_count

if __name__ == "__main__":
    T_max = 1000
    T_min = 0.01
    E_th = 1e-8
    alpha = 0.9

    solution, energy, iterations = simulated_annealing(T_max, T_min, E_th, alpha)

    print(f"Best solution: x = {solution}")
    print(f"Best energy: f(x) = {energy}")
    print(f"Total iterations: {iterations}")
