import math

# Atom coordinates
carbon_x = 26.100  
carbon_y = 29.253
carbon_z = 5.202
nitrogen_x = 26.849
nitrogen_y = 29.656
nitrogen_z = 6.217

# Calculate the difference between coordinates
diff_x = carbon_x - nitrogen_x
diff_y = carbon_y - nitrogen_y
diff_z = carbon_z - nitrogen_z

# Calculate the square of each difference
square_x = diff_x**2
square_y = diff_y**2
square_z = diff_z**2

# Sum the squared differences
sum_squares = square_x + square_y + square_z

# Take the square root of the sum
distance = math.sqrt(sum_squares)

# Print the distance
print(distance)
