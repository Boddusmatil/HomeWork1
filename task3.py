# Function to check if a number is positive, negative, or zero
def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

# Function to find the sum of all numbers between 1-100
def sum_numbers(n):
    result = 0
    i = 1
    while i <= n:
        result += i
        i += 1
    return result

# Test cases 
def test_control_structures():
    assert check_number(79) == "Positive"
    assert check_number(-1) == "Negative"
    assert check_number(0) == "Zero"

    # Test prime numbers
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for i in range(10):
        assert is_prime(primes[i]) == True

    # Test sum of all numbers from 1 to 100
    assert sum_numbers(100) == 5050

# Run the test cases
if __name__ == "__main__":
    test_control_structures()
    
