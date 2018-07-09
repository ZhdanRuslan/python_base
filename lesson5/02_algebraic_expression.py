import math

#circle square
def square_circle(r):
    return math.pi*r**2
#custom func example
def cust_expression(n):
    return n*2+7*n

#main loop
i = -5
while i <= 5:
    print("i:\t {0:>} \t first func:\t {1:>}\t second func:\t {2:>}".format(i, square_circle(i), cust_expression(i), "<"))
    i += 0.5