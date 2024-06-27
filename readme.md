What is Pytest?

- Testing Framework for python
- Auto-discovery of tests
- Rich assertion introspection
- Support parameterized and fixture-based testing

Why Pytest?

- Simplified Syntax
- Rich Assertion Introspection
- Powerful Fixture System
- Compatbility
- Extensibility

Execute:

1. To run a pytest file: pytest tests/test_file_name.py
2. To only run slow tests: pytest -m slow

Naming conventions to remember:

1. setup_method(self, method)
2. teardown_method(self, method)
3. fixtures global file name - conftest.py

Strucuture for reference

1. @pytest.fixture
2. @pytest.mark.slow
3. @pytest.mark.skip(reason="This feature is being tested")
4. @pytest.mark.xfail(reason="we cannot divide by zero, expected to fail")

5. Examples of parametrize 
```python
@pytest.mark.parametrize("length, expected_area", [(5, 25), (6, 36), (4, 16)])
   def test_multiple_square_areas(length, expected_area):
      assert Square(length=length).area() == expected_area

@pytest.mark.parametrize("length, expected_perimeter", [(5, 20), (3, 12), (4, 16)])
def test_multiple_perimeter(length, expected_perimeter):
   assert Square(length=length).perimeter() == expected_perimeter
```
Module vs Function Import: Patching works best when you import the module and reference the function through the module. This ensures that the patch affects the function call.
```python
@mock.patch("requests.get")
def test_get_users(mock_get):
   mock_response = mock.Mock()
   mock_response.status_code = 200
   mock_response.json.return_value = {"id": 1, "name": "J1sdfdsa"}
   mock_get.return_value = mock_response
   data = service.get_users()
   assert data == {"id": 1, "name": "J1sdfdsa"}
```
