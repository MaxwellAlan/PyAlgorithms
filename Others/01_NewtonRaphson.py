# Newton-Raphson 寻找平方根
# 求解 x^2 -24=0 即求24得平方根
epsilon = 0.01
target = 24.0
guess = target / 2.0
while abs(guess*guess - target) >= epsilon:
    guess = guess - ((guess ** 2) - target)/(2 * guess)
print('Square root of',target,'is about',guess)