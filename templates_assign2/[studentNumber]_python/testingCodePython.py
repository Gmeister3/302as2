import subprocess
import sys
import os

def run_python_with_input(script_name="ConvexHull", python_file=None, input_files=None):
    if python_file is None:
        python_file = f"{script_name}.py"
    
    if input_files is None:
        input_files = []
    
    subprocess.run(["python", python_file] + input_files)

if __name__ == "__main__":
    input_files = [
        os.path.join("inputs", "point_sets_20.txt"),
        os.path.join("inputs", "point_sets_50.txt")
    ]
    
    run_python_with_input("ConvexHull", input_files=input_files)