# A function to check whether a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Get the range of numbers from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

numbers = list(range(start, end + 1))
prime_numbers = []
sum_of_primes = 0
for number in numbers:
    if is_prime(number):
        sum_of_primes += number
        prime_numbers.append(numbers)

max_number = max(numbers)

print("Sum of prime numbers between", start, "and", end, ":", sum_of_primes)
print("Maximum number between", start, "and", end, ":", max_number)
print(prime_numbers)
