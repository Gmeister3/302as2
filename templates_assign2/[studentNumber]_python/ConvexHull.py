import sys
import os


if __name__ == "__main__":
    print("All arguments (excluding script name):")
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"sys.argv[{i}] = {arg}")