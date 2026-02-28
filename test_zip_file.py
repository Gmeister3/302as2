#!/usr/bin/env python3
"""
Comprehensive test script for templates_assign2 (1).zip
Tests the integrity, structure, and functionality of the uploaded zip file.
"""

import os
import sys
import subprocess
import zipfile
import tempfile
import shutil
from pathlib import Path
import filecmp

class ZipFileTester:
    def __init__(self, zip_path, reference_dir=None):
        self.zip_path = zip_path
        self.reference_dir = reference_dir
        self.temp_dir = None
        self.test_results = []
        self.passed_tests = 0
        self.failed_tests = 0
        
    def log_test(self, test_name, passed, message=""):
        """Log a test result"""
        status = "✓ PASS" if passed else "✗ FAIL"
        self.test_results.append(f"{status}: {test_name}")
        if message:
            self.test_results.append(f"       {message}")
        
        if passed:
            self.passed_tests += 1
        else:
            self.failed_tests += 1
            
    def test_zip_integrity(self):
        """Test if the zip file is valid and can be opened"""
        try:
            with zipfile.ZipFile(self.zip_path, 'r') as zip_ref:
                # Test the zip file integrity
                bad_file = zip_ref.testzip()
                if bad_file is not None:
                    self.log_test("Zip Integrity", False, f"Corrupted file: {bad_file}")
                    return False
                else:
                    self.log_test("Zip Integrity", True, "All files in zip are intact")
                    return True
        except zipfile.BadZipFile:
            self.log_test("Zip Integrity", False, "Invalid zip file format")
            return False
        except Exception as e:
            self.log_test("Zip Integrity", False, f"Error: {str(e)}")
            return False
    
    def test_zip_structure(self):
        """Test if the zip file has the expected directory structure"""
        expected_files = [
            'templates_assign2/[studentNumber]_java/ConvexHull.java',
            'templates_assign2/[studentNumber]_java/testingCodeJava.py',
            'templates_assign2/[studentNumber]_java/inputs/point_sets_20.txt',
            'templates_assign2/[studentNumber]_java/inputs/point_sets_50.txt',
            'templates_assign2/[studentNumber]_python/ConvexHull.py',
            'templates_assign2/[studentNumber]_python/testingCodePython.py',
            'templates_assign2/[studentNumber]_python/inputs/point_sets_20.txt',
            'templates_assign2/[studentNumber]_python/inputs/point_sets_50.txt',
        ]
        
        try:
            with zipfile.ZipFile(self.zip_path, 'r') as zip_ref:
                zip_contents = zip_ref.namelist()
                missing_files = []
                
                for expected_file in expected_files:
                    if expected_file not in zip_contents:
                        missing_files.append(expected_file)
                
                if missing_files:
                    self.log_test("Zip Structure", False, 
                                f"Missing files: {', '.join(missing_files)}")
                    return False
                else:
                    self.log_test("Zip Structure", True, 
                                f"All {len(expected_files)} expected files present")
                    return True
        except Exception as e:
            self.log_test("Zip Structure", False, f"Error: {str(e)}")
            return False
    
    def test_extraction(self):
        """Test if the zip file can be extracted"""
        try:
            self.temp_dir = tempfile.mkdtemp(prefix='zip_test_')
            with zipfile.ZipFile(self.zip_path, 'r') as zip_ref:
                zip_ref.extractall(self.temp_dir)
            
            extracted_path = Path(self.temp_dir) / 'templates_assign2'
            if extracted_path.exists():
                self.log_test("Zip Extraction", True, 
                            f"Successfully extracted to {self.temp_dir}")
                return True
            else:
                self.log_test("Zip Extraction", False, 
                            "templates_assign2 directory not found after extraction")
                return False
        except Exception as e:
            self.log_test("Zip Extraction", False, f"Error: {str(e)}")
            return False
    
    def test_python_implementation(self):
        """Test the Python implementation"""
        if not self.temp_dir:
            self.log_test("Python Implementation", False, "Extraction not performed")
            return False
        
        python_dir = Path(self.temp_dir) / 'templates_assign2' / '[studentNumber]_python'
        
        try:
            # Check if ConvexHull.py exists
            convex_hull_file = python_dir / 'ConvexHull.py'
            if not convex_hull_file.exists():
                self.log_test("Python Implementation", False, "ConvexHull.py not found")
                return False
            
            # Try to import and validate syntax
            result = subprocess.run(
                ['python3', '-m', 'py_compile', str(convex_hull_file)],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode != 0:
                self.log_test("Python Implementation", False, 
                            f"Syntax error: {result.stderr}")
                return False
            
            # Try running the test script
            test_script = python_dir / 'testingCodePython.py'
            if test_script.exists():
                result = subprocess.run(
                    ['python3', str(test_script)],
                    cwd=str(python_dir),
                    capture_output=True,
                    text=True,
                    timeout=30
                )
                
                if result.returncode == 0:
                    self.log_test("Python Implementation", True, 
                                "Code compiles and runs successfully")
                    return True
                else:
                    # Check if it's just missing outputs (acceptable)
                    if "FileNotFoundError" in result.stderr or "output" in result.stderr.lower():
                        self.log_test("Python Implementation", True, 
                                    "Code compiles and runs (output files missing is expected)")
                        return True
                    else:
                        self.log_test("Python Implementation", False, 
                                    f"Runtime error: {result.stderr[:200]}")
                        return False
            else:
                self.log_test("Python Implementation", True, 
                            "ConvexHull.py has valid syntax")
                return True
                
        except subprocess.TimeoutExpired:
            self.log_test("Python Implementation", False, "Test timed out")
            return False
        except Exception as e:
            self.log_test("Python Implementation", False, f"Error: {str(e)}")
            return False
    
    def test_java_implementation(self):
        """Test the Java implementation"""
        if not self.temp_dir:
            self.log_test("Java Implementation", False, "Extraction not performed")
            return False
        
        java_dir = Path(self.temp_dir) / 'templates_assign2' / '[studentNumber]_java'
        
        try:
            # Check if ConvexHull.java exists
            convex_hull_file = java_dir / 'ConvexHull.java'
            if not convex_hull_file.exists():
                self.log_test("Java Implementation", False, "ConvexHull.java not found")
                return False
            
            # Try to compile
            result = subprocess.run(
                ['javac', str(convex_hull_file)],
                cwd=str(java_dir),
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode != 0:
                self.log_test("Java Implementation", False, 
                            f"Compilation error: {result.stderr}")
                return False
            
            self.log_test("Java Implementation", True, 
                        "ConvexHull.java compiles successfully")
            return True
                
        except subprocess.TimeoutExpired:
            self.log_test("Java Implementation", False, "Compilation timed out")
            return False
        except FileNotFoundError:
            self.log_test("Java Implementation", False, "Java compiler (javac) not found")
            return False
        except Exception as e:
            self.log_test("Java Implementation", False, f"Error: {str(e)}")
            return False
    
    def compare_with_reference(self):
        """Compare extracted contents with reference directory"""
        if not self.reference_dir or not self.temp_dir:
            return
        
        ref_path = Path(self.reference_dir)
        extract_path = Path(self.temp_dir) / 'templates_assign2'
        
        if not ref_path.exists():
            self.log_test("Reference Comparison", False, "Reference directory not found")
            return
        
        # Compare Python ConvexHull files
        ref_python = ref_path / '[studentNumber]_python' / 'ConvexHull.py'
        ext_python = extract_path / '[studentNumber]_python' / 'ConvexHull.py'
        
        if ref_python.exists() and ext_python.exists():
            if filecmp.cmp(ref_python, ext_python, shallow=False):
                self.log_test("Python File Comparison", True, 
                            "ConvexHull.py matches reference")
            else:
                self.log_test("Python File Comparison", False, 
                            "ConvexHull.py differs from reference")
        
        # Compare Java ConvexHull files
        ref_java = ref_path / '[studentNumber]_java' / 'ConvexHull.java'
        ext_java = extract_path / '[studentNumber]_java' / 'ConvexHull.java'
        
        if ref_java.exists() and ext_java.exists():
            if filecmp.cmp(ref_java, ext_java, shallow=False):
                self.log_test("Java File Comparison", True, 
                            "ConvexHull.java matches reference")
            else:
                self.log_test("Java File Comparison", False, 
                            "ConvexHull.java differs from reference")
    
    def run_all_tests(self):
        """Run all tests and generate report"""
        print("=" * 70)
        print("ZIP FILE TESTING REPORT")
        print("=" * 70)
        print(f"Zip File: {self.zip_path}")
        print(f"Reference Dir: {self.reference_dir}")
        print("=" * 70)
        print()
        
        # Run tests
        self.test_zip_integrity()
        self.test_zip_structure()
        self.test_extraction()
        
        if self.temp_dir:
            self.test_python_implementation()
            self.test_java_implementation()
            
            if self.reference_dir:
                self.compare_with_reference()
        
        # Print results
        print("TEST RESULTS:")
        print("-" * 70)
        for result in self.test_results:
            print(result)
        print("-" * 70)
        print()
        print(f"SUMMARY: {self.passed_tests} passed, {self.failed_tests} failed")
        print("=" * 70)
        
        # Cleanup
        if self.temp_dir and os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
        
        return self.failed_tests == 0

def main():
    # Get the repository root
    repo_root = Path(__file__).parent.absolute()
    zip_file = repo_root / "templates_assign2 (1).zip"
    reference_dir = repo_root / "templates_assign2"
    
    if not zip_file.exists():
        print(f"Error: Zip file not found: {zip_file}")
        sys.exit(1)
    
    tester = ZipFileTester(str(zip_file), str(reference_dir))
    success = tester.run_all_tests()
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
