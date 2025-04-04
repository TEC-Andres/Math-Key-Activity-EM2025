from sympy import symbols, pi, integrate, sympify
from mpmath import mp
class RevolutionIntegralSolver:
    def __init__(self, precision=50):
        self.x = symbols('x')
        mp.dps = precision
        self.total_volume = mp.mpf(0)

    def compute_volume(self, function, lower_bound, upper_bound):
        f = sympify(function)
        lower = sympify(lower_bound)
        upper = sympify(upper_bound)
        volume = pi * integrate(f**2, (self.x, lower, upper))
        return mp.mpf(volume.evalf(mp.dps))

    def solve(self, functions):
        for func, lower, upper in functions:
            volume = self.compute_volume(func, lower, upper)
            self.total_volume += volume
            print(f"Revolution integral for {func} from {lower} to {upper}: {volume}")

        print(f"Total volume: {self.total_volume}")
        return self.total_volume

if __name__ == "__main__":
    functions_to_solve = [
        # Integral, lower limit, upper limit.
        ("5.5", "10.5", "23.19"),
        ("-2.32*sin(0.24*x) + 3.975", "23.19", "32.243"),
        ("-((0.10*x - 2)**2) + 6.4", "8.01", "10.5"),
        ("((0.297*x - 1.7)**2) + 4.5", "4.3", "8.01"),
        ("-((0.29*x - 0.29)**2) + 5.6", "0", "4.3"),
        ("0*x + 2.05", "32.5", "34.4"),
        ("-((5*x - 162)**2) + 2.28", "32.243", "32.5"),
        ("-((1.65*x - 56.56)**4) + 2.05", "34.4", "35"),
        ("-0.2*x**2 + 5.5159", "-3", "0"),
        ("abs(sqrt((x + 4.3)/0.4) + 1.5)", "-4.3", "-3.1"),
        ("abs(-sqrt((x + 4.3)/0.4) + 1.5)", "-4.3", "-3.1"),
        ("5.67*x + 20.809", "-3.1", "-3.01")
    ]

    solver = RevolutionIntegralSolver(precision=50)
    solver.solve(functions_to_solve)
    print("Solved all revolution integrals.")
