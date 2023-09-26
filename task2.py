# Integer
num = 42

# Float
sal = 58000.56

# String
my_string = "Hello World!"

# List
values = [1, 2, 3, 4, 5]

# Dictionary
my_info = {"name": "smatil", "age": 30, "city": "wrgl"}


# Test cases for data types
def test_data_types():
  # Test integer
  assert isinstance(num, int)

  # Test float
  assert isinstance(sal, float)

  # Test string
  assert isinstance(my_string, str)

  # Test list
  assert isinstance(values, list)

  # Test dictionary
  assert isinstance(my_info, dict)


if __name__ == "__main__":
  test_data_types()
