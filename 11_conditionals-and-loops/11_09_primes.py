# Print out every prime number between 1 and 1000.

# for number in range(1, 100):
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             pass
#         else:
#             print(number)

def is_prime(n):
    if n <= 1:
        return False
    # Check for factors from 2 to n // 2
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Iterate through numbers from 1 to 1000
for number in range(1, 1001):
    if is_prime(number):
        print(number)