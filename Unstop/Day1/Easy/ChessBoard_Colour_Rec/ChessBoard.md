# Chessboard Color Detection

## 📝 Problem Statement

Imagine the chessboard as a 2D Cartesian plane, where:
* The **x-axis** is represented by alphabets (`a-h`).
* The **y-axis** is represented by numbers (`1-8`).

Given the coordinates in the form of a string, determine if that specific cell is **White** or **Black**.

### Input Format
A single string `s` of length 2 (e.g., "a1", "b2").

### Output Format
Print `White` or `Black`.

### Constraints
* $|s| = 2$
* $s[0]$ is a lowercase letter from 'a' to 'h'.
* $s[1]$ is a digit from '1' to '8'.

---

## 💡 Examples

| Input | Output | Explanation |
| :--- | :--- | :--- |
| `a1` | Black | Standard chessboard starting corner is black. |
| `b2` | Black | Diagonal from a1. |
| `h8` | Black | Opposite corner. |
| `a2` | White | Adjacent to a1. |

---

## 🚀 Solution (C)

This solution uses the parity (odd/even) of the ASCII values of the characters to determine the color. On a chessboard, if the sum of the coordinates (column + row) is even/odd in a specific pattern, the color remains consistent.

```c
#include <stdio.h>

/**
 * Logic:
 * In a chessboard, cells where (column + row) have the same parity are the same color.
 * This implementation uses modulo and bitwise logic to map the characters to color strings.
 */
const char* determine_color(const char* s) {
    int x, y;
    x = s[0] % 2; // Parity of the column letter
    y = s[1] % 2; // Parity of the row number
    
    const char* result[2] = {"Black", "White"};

    if (x) {
        return (x & y) ? result[0] : result[1];
    } else {
        return (y || x) ? result[1] : result[0];
    }
}

int main() {
    char s[256];
    // Read input string
    if (scanf("%s", s) == 1) {
        const char* result = determine_color(s);
        printf("%s\n", result);
    }
    return 0;
}
```

### 🛠️ How to Run
Copy the code into a file named solution.c.

- Compile using GCC:

```Bash
gcc solution.c -o solution
Run the executable:
```

```Bash
./solution
```
Then enter a coordinate (e.g., a1) and press Enter.

## !Note it doesn't have any kind of validation or other such so make sure inputs are validated from your side.
