import sys
import os


def cross_product(o, a, b):
    """
    Calculate the cross product of vectors OA and OB.
    Returns positive if counter-clockwise, negative if clockwise, 0 if collinear.
    """
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def convex_hull(points):
    """
    Compute the convex hull using Graham's Scan algorithm.
    Returns the points on the convex hull in counter-clockwise order.
    """
    # Sort points lexicographically (first by x, then by y)
    points = sorted(points)
    
    # Build lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    
    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    
    # Remove the last point of each half because it's repeated at the beginning of the other half
    return lower[:-1] + upper[:-1]


def read_points_from_file(filename):
    """
    Read points from input file.
    First line: number of points
    Subsequent lines: x y coordinates
    """
    points = []
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        for _ in range(n):
            line = f.readline().strip()
            if line:
                x, y = map(int, line.split())
                points.append((x, y))
    return points


def write_hull_to_file(hull, output_filename):
    """
    Write convex hull to output file.
    First line: number of hull points
    Subsequent lines: x, y coordinates
    """
    with open(output_filename, 'w') as f:
        f.write(f"{len(hull)}\n")
        for x, y in hull:
            f.write(f"{x}, {y}\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ConvexHull.py <input_file1> [input_file2] ...")
        sys.exit(1)
    
    for input_file in sys.argv[1:]:
        print(f"Processing: {input_file}")
        
        # Read points
        points = read_points_from_file(input_file)
        
        # Compute convex hull
        hull = convex_hull(points)
        
        # Generate output filename
        base_name = os.path.splitext(os.path.basename(input_file))[0]
        output_file = os.path.join("outputs", f"output_{base_name}.txt")
        
        # Write output
        write_hull_to_file(hull, output_file)
        
        print(f"Convex hull with {len(hull)} points written to {output_file}")