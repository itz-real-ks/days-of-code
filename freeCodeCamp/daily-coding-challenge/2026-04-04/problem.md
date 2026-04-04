# Equation Validation

Create a function `is_valid_equation` that evaluates a mathematical string to determine if the equation is balanced and correct.

## Problem Description

You are given a string representing a mathematical equation. Your goal is to return **True** if the left side of the equation equals the right side, and **False** otherwise.

### Constraints & Rules

* **Left Side:** Contains two or three positive integers separated by operators.
* **Operators:** Includes addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
* **Right Side:** Always a single integer.
* **Order of Operations:** You must follow standard mathematical precedence (PEMDAS). Multiplication and division must be evaluated before addition and subtraction.
* **Format:** The input string follows the pattern `"number operator number = number"` or `"number operator number operator number = number"`.

---

## Examples

| Input | Evaluation Process | Result |
| :--- | :--- | :--- |
| `"2 + 3 - 1 = 4"` | 2 + 3 - 1 = 4 | `True` |
| `"2 + 9 / 3 = 5"` | 2 + (9 / 3) = 5 | `True` |
| `"20 - 2 * 3 = 14"` | 20 - (2 * 3) = 14 | `True` |
| `"10 - 2 * 3 = 24"` | 10 - 6 = 4 (Not 24) | `False` |

---

## Test Cases

Your implementation should pass the following tests:

```python
is_valid_equation("2 + 2 = 4")           # True
is_valid_equation("2 + 3 - 1 = 4")       # True
is_valid_equation("8 / 2 = 4")           # True
is_valid_equation("10 * 5 = 50")         # True
is_valid_equation("2 - 2 = 0")           # True
is_valid_equation("2 + 9 / 3 = 5")       # True
is_valid_equation("20 - 2 * 3 = 14")     # True
is_valid_equation("2 + 5 = 6")           # False
is_valid_equation("10 - 2 * 3 = 24")     # False
is_valid_equation("3 + 9 / 3 = 4")       # False
