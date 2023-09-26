import pytest

def calculate_discount(price, discount):
    if discount < 0 or discount > 100:
        raise ValueError("Discount percentage must be between 0 and 100")
    
    discounted_price = price - (price * (discount / 100))
    return discounted_price


# Test cases for calculate_discount function
def test_discount_integer():
    assert calculate_discount(400, 1) == 396
    assert calculate_discount(100, 25) == 75

def test_discount_mixed_val():
    assert calculate_discount(1000, 10.0) == 900.0
    assert calculate_discount(150.0, 15) == 127.5

def test__discount_invalid_val():
    with pytest.raises(ValueError):
        calculate_discount(100, -10)
    with pytest.raises(ValueError):
        calculate_discount(50, 110)

# Run the test cases
if __name__ == "__main__":
  test_discount_integer()
  test__discount_invalid_val()
  test_discount_mixed_val()
  
  
