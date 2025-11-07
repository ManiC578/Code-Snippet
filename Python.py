import random

# Generate a random integer between 1 and 100
random_int = random.randint(1, 100)
print("Random Integer:", random_int)

# Generate a random float between 0 and 1
random_float = random.random()
print("Random Float:", random_float)

# Generate a random number from a given list
numbers = [10, 20, 30, 40, 50]
random_choice = random.choice(numbers)
print("Random Choice from List:", random_choice)

# Generate multiple random integers
random_list = [random.randint(1, 100) for _ in range(5)]
print("Random List:", random_list)
