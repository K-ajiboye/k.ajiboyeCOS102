# simple interest
r = 3
t = 5
p = 3

b = r/100
c = b * t
d = 1 + c
simple_interest = p * d
print("simple_interest")

#compound interest 
p = 7
n = 2
t = 4 
r = 6

z = r/n
y = 1 + z
x = y ** (n * t)
compound_interest = p * x 

print("compound_interest") 

#annuity plan 
pmt = 5
p = 8
n = 4
t = 3
r = 5

o = r/n 
k = 1 + o 
j = k ** (n * t)
m = j - 1
g = m/o
annuity_plan = pmt * g
print("annuity_plan")