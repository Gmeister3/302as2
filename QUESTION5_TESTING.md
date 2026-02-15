# Question 5: Convex Hull Implementation - Testing Guide

## Overview

Question 5 requires the implementation of a Convex Hull algorithm. Both Python and Java implementations have been completed using **Graham's Scan** algorithm.

## Algorithm Details

- **Algorithm:** Graham's Scan
- **Time Complexity:** O(n log n) - dominated by the sorting step
- **Space Complexity:** O(n)
- **Strategy:** Build lower and upper hulls separately, then combine them

## Implementations

### Python Implementation
- **Location:** `templates_assign2/[studentNumber]_python/ConvexHull.py`
- **Test Script:** `templates_assign2/[studentNumber]_python/testingCodePython.py`

### Java Implementation
- **Location:** `templates_assign2/[studentNumber]_java/ConvexHull.java`
- **Test Script:** `templates_assign2/[studentNumber]_java/testingCodeJava.py`

## Test Files

### Input Files
1. `inputs/point_sets_20.txt` - 20 random points
2. `inputs/point_sets_50.txt` - 50 random points

### Output Files
Both implementations generate output files in the `outputs/` directory:
- `outputs/output_point_sets_20.txt` - Convex hull with 9 points
- `outputs/output_point_sets_50.txt` - Convex hull with 11 points

## Running the Tests

### Option 1: Run Individual Tests

#### Python:
```bash
cd templates_assign2/[studentNumber]_python
python3 testingCodePython.py
```

#### Java:
```bash
cd templates_assign2/[studentNumber]_java
python3 testingCodeJava.py
```

### Option 2: Run Comprehensive Test Suite

From the repository root:
```bash
python3 test_question5.py
```

This comprehensive test script will:
1. ✅ Test the Python implementation
2. ✅ Test the Java implementation  
3. ✅ Verify both implementations produce identical output
4. ✅ Verify the output matches expected results

## Expected Results

### Test: point_sets_20.txt
- **Input:** 20 points
- **Output:** 9 points on convex hull
- **Hull points (counter-clockwise):**
  - (-60, -27), (-23, -59), (5, -34), (21, -4), (37, 29)
  - (-27, 56), (-50, 42), (-51, 41), (-59, -13)

### Test: point_sets_50.txt
- **Input:** 50 points
- **Output:** 11 points on convex hull
- **Hull points (counter-clockwise):**
  - (-59, -23), (-53, -47), (-4, -58), (50, -58), (55, -51)
  - (56, -25), (55, 0), (52, 31), (46, 56), (-10, 57), (-36, 31)

## Verification

All tests pass successfully:
- ✅ Python implementation works correctly
- ✅ Java implementation works correctly
- ✅ Both implementations produce identical results
- ✅ Results match expected convex hull calculations

## Output Format

The output files follow this format:
```
<number_of_hull_points>
<x1>, <y1>
<x2>, <y2>
...
```

Example:
```
9
-60, -27
-23, -59
5, -34
...
```

## Notes

- Both implementations use the same Graham's Scan algorithm
- Points are sorted lexicographically (first by x, then by y)
- The convex hull is returned in counter-clockwise order
- The implementations handle edge cases including collinear points
- The Java output format was updated to match the Python format (comma separator)
