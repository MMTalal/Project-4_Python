# Subject Grade Calculator

This is a simple Python program that calculates a student's total grade based on six subject grades, and then provides feedback on the performance.

## Features

- Prompts the user to enter the grade for each of the six subjects, with a range of 0 to 20.
- Validates the input to ensure that the grade is within the valid range.
- Calculates the total grade as a percentage.
- Provides feedback on the student's performance based on the calculated grade.

## Usage

1. Run the Python script.
2. Follow the prompts and enter the grade for each of the six subjects.
3. The program will display the total grade as a percentage and provide feedback on the student's performance.

## Example Output

```
Subject Grade Calculator
--------------------------------------------------
What's your grade for subject one out of 20? 18
What's your grade for subject two out of 20? 16
What's your grade for subject three out of 20? 15
What's your grade for subject four out of 20? 17
What's your grade for subject five out of 20? 19
What's your grade for subject six out of 20? 18
Your total grade is 83.33%
Congratulations! Your grade is above 75%. You are very good.
```

## Limitations

- The program assumes that the subject grades are between 0 and 20. It does not handle cases where the grades are outside this range.
- The program does not provide any functionality to store or retrieve the grades for multiple students.

## Future Improvements

- Implement error handling for cases where the user enters non-numeric input.
- Add support for saving and loading student grades to/from a file or database.
- Enhance the user interface by providing a menu-driven system or a graphical user interface (GUI).