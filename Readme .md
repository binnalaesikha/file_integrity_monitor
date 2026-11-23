File Integrity Monitor

Project Description

The File Integrity Monitor is a Python-based project that detects changes made to files using SHA-256 hashing.

It creates a baseline hash of a file and compares it with the current hash to identify modifications.

Features

- Uses SHA-256 hashing algorithm.
- Creates and stores the original file hash.
- Compares original and current file hashes.
- Detects file modifications.
- Displays file status as SAFE or WARNING.

Technologies Used

- Python
- hashlib module
- os module

How to Run

1. Open the project in Pydroid 3.
2. Run "file_integrity_monitor.py".
3. Enter the file name (example: "sample.txt").
4. The program creates a baseline during the first run.
5. Modify the sample file and run the program again to check for changes.

Output

- Baseline created successfully!
- File Status: SAFE
- WARNING: FILE MODIFIED!

Conclusion

This project demonstrates how file integrity can be monitored using SHA-256 hashing in Python.
