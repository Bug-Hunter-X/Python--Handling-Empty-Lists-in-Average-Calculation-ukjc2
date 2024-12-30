# Python: Handling Empty Lists in Average Calculation

This repository demonstrates a common error in Python when calculating the average of a list of numbers and shows how to improve the error handling.

## Bug
The original `calculate_average` function handles empty lists by returning 0. However, in some situations, it might be more appropriate to raise an exception, for example, a `ValueError`, indicating that an average cannot be calculated from an empty list.

## Solution
The improved function explicitly checks for the empty list case and raises a `ValueError` instead of returning 0.

Feel free to use and modify this example to learn more about robust error handling in Python.
