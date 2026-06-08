"""
## 3. Contains Duplicate  *(Easy)*

=================================================
CONTAINS DUPLICATE
=================================================

Problem Statement:
You are given a list of integers. Return TRUE
if any value appears AT LEAST TWICE in the
list, otherwise return FALSE.

Write the BRUTE-FORCE O(n^2) version FIRST,
then optimize it to O(n) using a SET.

-------------------------------------------------
Instructions:
Write TWO functions:

1. has_duplicate_brute(nums)
   - Use two nested for loops to compare every
     pair (i, j) with i < j.
   - Return True as soon as nums[i] == nums[j].
   - If no duplicate is found, return False.
   - Time complexity:  O(n^2)
   - Space complexity: O(1)

2. has_duplicate_fast(nums)
   - Create an empty SET called `seen`.
   - Use a SINGLE for loop over nums:
        - if the value is already in `seen`,
          return True
        - otherwise, add it to `seen`
   - If the loop finishes without finding
     a duplicate, return False.
   - Time complexity:  O(n)
   - Space complexity: O(n)

Do NOT use:
   - list.count()
   - len(set(nums)) trick
   - sorted() / list.sort()
   - any external library

Call BOTH functions on the same input and
print both results.

-------------------------------------------------
Input Example 1:
nums = [1, 2, 3, 1]

Output Example 1:
Brute Force: True   # O(n^2)
Optimized:   True   # O(n)

-------------------------------------------------
Input Example 2:
nums = [1, 2, 3, 4]

Output Example 2:
Brute Force: False  # O(n^2)
Optimized:   False  # O(n)
=================================================

"""
def contains_duplicate(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                return True

    return False



nums = [1, 2, 3, 4, 2]
print(contains_duplicate(nums))