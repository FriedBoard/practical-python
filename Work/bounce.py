# bounce.py
#
# Exercise 1.5

start_Height = 100
height = start_Height
bounces = 10

for bounce in range(1, 1+bounces):
    height = height * (3/5)
    print(bounce, round(height, 4))