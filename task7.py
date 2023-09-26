import numpy as np

def calculate_statistics(data):
    # Calculate the mean and standard deviation using numpy
    mean = np.mean(data)
    std_dev = np.std(data)
    return mean, std_dev


import pytest

def test_calculate_statistics():
    data = [1, 2, 3, 4, 5]
    mean, std_dev = calculate_statistics(data)
    assert mean == pytest.approx(3.0)  
    assert std_dev == pytest.approx(1.5811, abs=1e-4)  # 

# Run the test cases
if __name__ == "__main__":
    # pytest.main()
  test_calculate_statistics()
