# bounce.py
#
# Exercise 1.5
height = 100
bounceBackValue = 0.6
bounces = 1

while bounces < 11:
    height = height * 0.6
    print(bounces, round(height, 4))
    bounces = bounces + 1