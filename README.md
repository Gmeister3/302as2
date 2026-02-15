# COSC 3P03 Assignment 2 Solutions

This repository contains the solutions for COSC 3P03 Assignment 2.

## Contents


## Questions Completed

1. **Q1**: Non-recursive Tower of Hanoi - Complete analysis of 4 algorithms with move tables
2. **Q2**: StoogeSort Algorithm Analysis - Recurrence relations, proofs, and complexity analysis
3. **Q3**: Bonus Question (QuickSelect) - Complete algorithm analysis with average/worst case complexity
4. **Q4**: Searching Lower and Upper Bounds - Adversarial search analysis
5. **Q5**: Convex Hull Implementation - Graham's Scan algorithm implemented in Python and Java

## Q5 - Convex Hull Implementation

The convex hull implementation is available in both Python and Java:

### Python Implementation
Location: `templates_assign2/[studentNumber]_python/ConvexHull.py`

To run:
```bash
cd templates_assign2/[studentNumber]_python
python3 testingCodePython.py
```

### Java Implementation
Location: `templates_assign2/[studentNumber]_java/ConvexHull.java`

To run:
```bash
cd templates_assign2/[studentNumber]_java
javac ConvexHull.java
python3 testingCodeJava.py
```

### Algorithm Used
Both implementations use **Graham's Scan** algorithm:
- Time Complexity: O(n log n) due to sorting
- Space Complexity: O(n)
- The algorithm sorts points lexicographically, then builds lower and upper hulls separately

### Test Results
- **point_sets_20.txt**: Successfully identified 9 points on the convex hull
- **point_sets_50.txt**: Successfully identified 11 points on the convex hull

## Viewing Solutions

- **Markdown Format**: Open `assignment2_solutions.md` to view the complete solutions with detailed explanations, proofs, and examples.
- **PDF Format**: Open `assignment2_solutions.pdf` for a professionally formatted PDF document with proper mathematical typesetting.
- **LaTeX Source**: The LaTeX source is available in `assignment2_solutions.tex` and can be recompiled if needed.
