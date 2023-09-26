# Dictionary to store data
data = {}

# Function to get a value from the dictionary
def get_value(key):
  return data.get(key, None)

# Function to set a value in the dictionary
def set_value(key, value):
  data[key] = value

#Test cases
def test_key():
  # Test getting a value with an existing key
  set_value("name", "Alice")
  result = get_value("name")
  assert data['name'] == result

def test_new_key():
  # Test setting a value with a new key
  set_value("city", "New York")
  res = get_value("city")
  assert data['city'] == res


if __name__ == "__main__":

  test_key()
  test_new_key()
