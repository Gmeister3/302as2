import java.io.*;
import java.util.*;

public class ConvexHull {

    static class Point implements Comparable<Point> {
        int x, y;

        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public int compareTo(Point other) {
            if (this.x != other.x) {
                return Integer.compare(this.x, other.x);
            }
            return Integer.compare(this.y, other.y);
        }

        @Override
        public String toString() {
            return x + " " + y;
        }
    }

    static long crossProduct(Point o, Point a, Point b) {
        return (long)(a.x - o.x) * (b.y - o.y) - (long)(a.y - o.y) * (b.x - o.x);
    }


    static List<Point> convexHullGregorySampson(List<Point> points) {
        Collections.sort(points);

        // Build lower hull
        List<Point> lower = new ArrayList<>();
        for (Point p : points) {
            while (lower.size() >= 2 && crossProduct(lower.get(lower.size() - 2),
                    lower.get(lower.size() - 1), p) <= 0) {
                lower.remove(lower.size() - 1);
            }
            lower.add(p);
        }

        // Build upper hull
        List<Point> upper = new ArrayList<>();
        for (int i = points.size() - 1; i >= 0; i--) {
            Point p = points.get(i);
            while (upper.size() >= 2 && crossProduct(upper.get(upper.size() - 2),
                    upper.get(upper.size() - 1), p) <= 0) {
                upper.remove(upper.size() - 1);
            }
            upper.add(p);
        }

        // Remove the last point of each half because it's repeated
        lower.remove(lower.size() - 1);
        upper.remove(upper.size() - 1);

        lower.addAll(upper);
        return lower;
    }

    static List<Point> readPointsFromFileGregorySampson(String filename) throws IOException {
        List<Point> points = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            int n = Integer.parseInt(br.readLine().trim());
            for (int i = 0; i < n; i++) {
                String line = br.readLine().trim();
                String[] parts = line.split("\\s+");
                int x = Integer.parseInt(parts[0]);
                int y = Integer.parseInt(parts[1]);
                points.add(new Point(x, y));
            }
        }

        return points;
    }


    static void writeHullToFileGregorySampson(List<Point> hull, String outputFilename) throws IOException {
        try (PrintWriter pw = new PrintWriter(new FileWriter(outputFilename))) {
            pw.println(hull.size());
            for (Point p : hull) {
                pw.println(p);
            }
        }
    }

    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Usage: java ConvexHull <input_file1> [input_file2] ...");
            return;
        }

        for (String inputFile : args) {
            try {
                System.out.println("Processing: " + inputFile);

                // Read points
                List<Point> points = readPointsFromFileGregorySampson(inputFile);

                // Compute convex hull
                List<Point> hull = convexHullGregorySampson(points);

                // Generate output filename
                String baseName = new File(inputFile).getName().replace(".txt", "");
                String outputFile = "outputs/output_" + baseName + ".txt";

                // Write output
                writeHullToFileGregorySampson(hull, outputFile);

                System.out.println("Convex hull with " + hull.size() + " points written to " + outputFile);
            } catch (IOException e) {
                System.err.println("Error processing " + inputFile + ": " + e.getMessage());
            }
        }
    }
}