# Roman-Arabic-Numeral-Converter
This Python script allows you to convert numbers between Roman numerals and Arabic numerals. It provides a simple command-line interface to perform conversions in both directions.

# Features
Convert Roman numerals to Arabic numbers.
Convert Arabic numbers (1–3999) to Roman numerals.
Input validation:
  Rejects empty inputs.
  Checks for invalid Roman numeral characters.
  Prevents more than 3 identical Roman symbols in a row.
  Validates Arabic numbers to be in the range 1–3999.
Continuous loop until the user chooses to quit.

# How to Use
1. Run the script:
python roman_converter.py
# 2. You will be prompted to choose an option:
  Enter a to convert Roman → Arabic.
  Enter b to convert Arabic → Roman.
  Enter q to quit the program.
3. Follow the on-screen instructions to input your number.
4. The result will be displayed immediately.

# Requirements
Python 3.x
No external libraries are needed.

# Notes
Only English letters are used for Roman numerals (I, V, X, L, C, D, M).
Arabic numbers are limited to 1–3999 due to standard Roman numeral conventions.
The program automatically removes spaces from input.
