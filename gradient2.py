next_x = 1  # We start the search at x=6
next_y = 2
gamma = 0.05  # Step size multiplier
precision = 0.00001  # Desired precision of result
max_iters = 100  # Maximum number of iterations

# Derivative function
def dfx(x):
    return 2*x
def dfy(y):
    return -2*y

def f(x,y):
    return x**2 - y**2 + 1

#def sign(x):
#    return 1 if x>0 else -1 if x<0 else 0

for _i in range(max_iters):
    current_x = next_x
    current_y = next_y
    next_x = current_x - gamma * dfx(current_x) * f(current_x,current_y)
    next_y = current_y - gamma * dfy(current_y) * f(current_x,current_y)

    stepx = next_x - current_x
    stepy = next_y - current_y
    if abs(stepx) <= precision and abs(stepy) <= precision :
        break

print("Minimum at ", f(next_x,next_y),next_x,next_y, _i)

