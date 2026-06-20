# Prime Factorization

Given an integer greater than 1, return its prime factorization as an array of numbers in ascending order.

A prime factorization is the set of prime numbers that multiply together to produce the given integer. Each number has exactly one unique set. For example, the prime factorization of 20 is `[2, 2, 5]` because $2 \times 2 \times 5 = 20$.

If the given integer is itself prime, return it in a single-element array.

## Examples

### Example 1
- **Input:** `20`
- **Output:** `[2, 2, 5]`
- **Explanation:** $2 \times 2 \times 5 = 20$, where 2 and 5 are prime numbers.

### Example 2
- **Input:** `17`
- **Output:** `[17]`
- **Explanation:** 17 is already a prime number, so it returns itself in a single-element array.

## Test Cases

The solution should pass the following test suites:

| # | Function Call | Expected Return Value |
|---|---------------|-----------------------|
| 1 | `prime_factorization(20)` | `[2, 2, 5]` |
| 2 | `prime_factorization(17)` | `[17]` |
| 3 | `prime_factorization(15)` | `[3, 5]` |
| 4 | `prime_factorization(35)` | `[5, 7]` |
| 5 | `prime_factorization(999)` | `[3, 3, 3, 37]` |
| 6 | `prime_factorization(360)` | `[2, 2, 2, 3, 3, 5]` |
| 7 | `prime_factorization(510510)` | `[2, 3, 5, 7, 11, 13, 17]` |

## Constraints
- `n > 1` (where `n` is the input integer)
