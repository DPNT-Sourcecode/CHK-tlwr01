from solutions.FIZ.fizz_buzz_solution import fizz_buzz  # Make sure the path is correct

def test_fizzbuzz():
    test_cases = [
        (1, "1"),
        (3, "Fizz"),
        (5, "Buzz"),
        (15, "FizzBuzz"),
        (30, "FizzBuzz"),
        (7, "7"),
    ]

    for num, expected in test_cases:
        result = fizz_buzz(num)
        assert result == expected, f"Test failed for input {num}. Expected {expected}, got {result}"
    
    print("✅ All tests passed for FizzBuzz!")

if __name__ == "__main__":
    test_fizzbuzz()
