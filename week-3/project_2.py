import math 
import cmath
#find the roots of a cubic equation
print("finding the root of a cubic equation in the format ax³ + bx² + cx + d = 0")
a = float(input("Input your value for a"))
b = float(input("Input your value for b"))
c = float(input("Input your value for c"))
d = float(input("Input your value for d"))

print(f"your equation is :{a}x³ {b}x² {c}x {d}")
q = ((3 * a * c) -(b**2)) / (9 * (a**2))
r = ((9*a*b*c) - (27 * a**2 *d )- (2 * (b**3))) / (54 * (a**3))
s = (r + (((q**3 + r**2)))**0.5) **(1/3)
t = (r - ((q**3 + r**2)**0.5))
t = t ** (1/3)
print(t)
print(r - (((q**3 + r**2)))**0.5)
h = -2.65712393117584 ** (1/3)
print(h)


x1 = (s + t) - (b/(3*a))
x2 = -(s+t)/2 - b/(3*a) + (cmath.sqrt(-3) * (s - t))/2
x3 = -(s+t)/2 - b/(3*a) - (cmath.sqrt(-3) * (s - t))/2

print(f"The roots of this equation are {x1}, {x2}, and {x3}")