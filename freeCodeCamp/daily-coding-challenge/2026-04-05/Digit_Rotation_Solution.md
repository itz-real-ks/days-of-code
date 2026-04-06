# 🌀 Digit Rotation Escape - Python Solution

Hey there! 👋 This is my quick and dirty Python solution for the "Digit Rotation Escape" coding challenge. 

The goal of the challenge is simple: take a positive integer and check if it's evenly divisible by its total number of digits. If it isn't, you "rotate" the number by moving the first digit to the very end, and try again. You keep doing this until you find a match or run out of rotations.

## 🧠 The Thought Process (How it Works)

Instead of trying to do complicated modulo math to strip and append digits, I decided to lean into Python's string manipulation because it's just so much easier to read. 

Here is the step-by-step logic:

1. [cite_start]**String Conversion:** Right off the bat, the function takes the integer `n` and converts it into a string `numstr`[cite: 1]. 
2. [cite_start]**The Loop:** We loop through a range based on the length of the string[cite: 1]. This ensures we only check up to the maximum number of unique rotations.
3. [cite_start]**The Math Check:** Inside the loop, we convert the current `numstr` back to an integer and use the modulo operator (`%`) to check if it divides cleanly by the length of the string[cite: 1].
4. **Success!** If the remainder is `0`, we found a valid rotation! [cite_start]The function immediately returns the current `rotation` count[cite: 2].
5. **The Spin:** If it doesn't divide evenly, we add `1` to the rotation counter and rotate the string. [cite_start]This is done with a quick slice: `numstr[1:] + numstr[:1]` grabs everything but the first character, and then sticks that first character on the end[cite: 2].
6. [cite_start]**The "None" Catch:** If the loop exhausts every possible rotation and still hasn't returned a match, it drops out of the loop and returns `"none"`[cite: 2].

## 🚀 Usage

Just pass an integer (without zeros) into the `get_rotation()` function:

```python
print(get_rotation(123))         # Returns: 0
print(get_rotation(13579))       # Returns: 3
print(get_rotation(24681))       # Returns: "none"
