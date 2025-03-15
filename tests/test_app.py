import pytest
from myapp.app import multiply_by_two, divide_by_two

# Define fixtures for reusable data
@pytest.fixture
def numbers():
    a = 10
    b = 20
    return [a, b]

@pytest.fixture
def student_id():
    return 62  

class TestApp:
    def test_multiplication(self, numbers):
        res = multiply_by_two(numbers[0])
        assert res == numbers[1]  # 10 * 2 = 20

    def test_division(self, numbers):
        res = divide_by_two(numbers[1])
        assert res == numbers[0]  # 20 / 2 = 10

    # New test for student ID requirement
    def test_student_id_multiplication(self, student_id):
        res = multiply_by_two(student_id)
        assert res == student_id * 2  # 62 * 2 = 124

    # Modify 
