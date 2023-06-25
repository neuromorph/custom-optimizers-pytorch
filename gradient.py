next_x = -1  # We start the search at x=6
gamma = 0.005  # Step size multiplier
precision = 0.00001  # Desired precision of result
max_iters = 100  # Maximum number of iterations

# Derivative function
def df(x):
    return 4 * x ** 3 - 9 * x ** 2

def f(x):
    return x ** 4 - 3 * x ** 3 + 20

#def sign(x):
#    return 1 if x>0 else -1 if x<0 else 0

for _i in range(max_iters):
    current_x = next_x
    next_x = current_x - gamma * df(current_x) * f(current_x)

    step = next_x - current_x
    if abs(step) <= precision:
        break

print("Minimum at ", next_x, _i)

