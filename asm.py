def calculate_pi(n):
    pi = 0
    for k in range(n):
        pi += (1 / 16**k) * (
            4 / (8 * k + 1) -
            2 / (8 * k + 4) -
            1 / (8 * k + 5) -
            1 / (8 * k + 6)
        )
    return pi

# Set the number of iterations (higher for more accuracy)
iterations = 100000

# Calculate Pi to the specified number of iterations
pi_value = calculate_pi(iterations)

# Print the calculated value of Pi
print(f"Calculated value of Pi: {pi_value}")
