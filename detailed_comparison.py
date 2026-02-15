#!/usr/bin/env python3
"""
Detailed comparison script to show differences between zip and reference directory
"""

import zipfile
import os
import difflib
from pathlib import Path
import tempfile
import shutil

def compare_files(file1, file2, name):
    """Compare two files and show differences"""
    print(f"\n{'='*70}")
    print(f"Comparing: {name}")
    print('='*70)
    
    with open(file1, 'r', encoding='utf-8', errors='ignore') as f1:
        content1 = f1.readlines()
    
    with open(file2, 'r', encoding='utf-8', errors='ignore') as f2:
        content2 = f2.readlines()
    
    if content1 == content2:
        print("✓ Files are identical")
        return True
    else:
        print("✗ Files differ:")
        diff = difflib.unified_diff(content1, content2, 
                                   fromfile='Reference', 
                                   tofile='Zip File',
                                   lineterm='')
        diff_lines = list(diff)
        
        # Show first 50 lines of diff
        for line in diff_lines[:50]:
            print(line)
        
        if len(diff_lines) > 50:
            print(f"\n... ({len(diff_lines) - 50} more lines)")
        
        return False

def main():
    repo_root = Path('/home/runner/work/302as2/302as2')
    zip_file = repo_root / "templates_assign2 (1).zip"
    reference_dir = repo_root / "templates_assign2"
    
    # Extract zip to temp directory
    temp_dir = tempfile.mkdtemp(prefix='zip_compare_')
    
    try:
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
        
        extract_path = Path(temp_dir) / 'templates_assign2'
        
        print("DETAILED FILE COMPARISON REPORT")
        print("="*70)
        
        # Compare key files
        files_to_compare = [
            ('[studentNumber]_python/ConvexHull.py', 'Python ConvexHull'),
            ('[studentNumber]_java/ConvexHull.java', 'Java ConvexHull'),
            ('[studentNumber]_python/testingCodePython.py', 'Python Test Script'),
            ('[studentNumber]_java/testingCodeJava.py', 'Java Test Script'),
        ]
        
        identical_count = 0
        different_count = 0
        
        for file_path, name in files_to_compare:
            ref_file = reference_dir / file_path
            zip_file_path = extract_path / file_path
            
            if ref_file.exists() and zip_file_path.exists():
                if compare_files(ref_file, zip_file_path, name):
                    identical_count += 1
                else:
                    different_count += 1
            else:
                print(f"\n{'='*70}")
                print(f"Comparing: {name}")
                print('='*70)
                print(f"✗ File not found in one or both locations")
                print(f"   Reference: {ref_file.exists()}")
                print(f"   Zip: {zip_file_path.exists()}")
                different_count += 1
        
        print(f"\n{'='*70}")
        print(f"SUMMARY: {identical_count} identical, {different_count} different")
        print('='*70)
        
        # List all files in both directories
        print("\n\nFILE INVENTORY:")
        print('='*70)
        print("\nFiles in ZIP:")
        print('-'*70)
        for root, dirs, files in os.walk(extract_path):
            for file in sorted(files):
                rel_path = Path(root).relative_to(extract_path) / file
                size = os.path.getsize(Path(root) / file)
                print(f"  {rel_path} ({size} bytes)")
        
        print("\nFiles in REFERENCE:")
        print('-'*70)
        for root, dirs, files in os.walk(reference_dir):
            for file in sorted(files):
                rel_path = Path(root).relative_to(reference_dir) / file
                size = os.path.getsize(Path(root) / file)
                print(f"  {rel_path} ({size} bytes)")
        
    finally:
        # Cleanup
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)

if __name__ == "__main__":
    main()
