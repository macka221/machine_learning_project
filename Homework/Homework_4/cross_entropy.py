# e constant
e = 2.7182818284

# initial values
i1, i2 = 0.05, 0.10

# initial weights
w1, w2, w3, w4, w5, w6, w7, w8 = (
        0.15, 0.20, 0.25, 0.30, 0.40, 0.45, 0.50, 0.55
        )

# bias
b1, b2 = 0.35, 0.60

# targets
To1, To2 = 0.01, 0.99

print(f"value of f: {w1*i1 + w3*i2 + b1}")
print(f"value of g: {w2*i1 + w4*i2 + b1}")
# forward propagation
h1 = 1 / (1 + e ** (- (w1 * i1 + w3 * i2 + b1)))
print(f"h1: {h1}")

h2 = 1 / (1 + e ** (- (w2 * i1 + w4 * i2 + b1)))
print(f"h2: {h2}")

print(f"value of f2: {w5*h1+w7*h2+b2}")
print(f"value of g2: {w6*h1+w8*h2+b2}")
o1 = 1 / (1 + e ** (- (w5 * h1 + w7 * h2 + b2)))
print(f"o1: {o1}")

o2 = 1 / (1 + e ** (- (w6 * h1 + w8 * h2 + b2)))
print(f"o2: {o2}")

# Error
Eo1 = 0.5 * (To1 - o1) ** 2
print(f"Error o1: {Eo1}")

Eo2 = 0.5 * (To2 - o2) ** 2
print(f"Error o2: {Eo2}")

E = Eo1 + Eo2
print(f"Total error: {E}")
