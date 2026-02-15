import subprocess
import sys
import os

def run_java_with_input(class_name="ConvexHull", java_file=None, input_files=None):
    if java_file is None:
        java_file = f"{class_name}.java"
    
    if input_files is None:
        input_files = []
    
    subprocess.run(["javac", java_file])
    subprocess.run(["java", class_name] + input_files)

if __name__ == "__main__":
    input_files = [
        os.path.join("inputs", "point_sets_20.txt"),
        os.path.join("inputs", "point_sets_50.txt")
    ]
    
    run_java_with_input("ConvexHull", input_files=input_files)