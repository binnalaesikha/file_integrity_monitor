import hashlib
import os

print("===================================")
print("     FILE INTEGRITY MONITOR")
print("===================================")

file_path = input("Enter file path: ")

def calculate_hash(path):
    sha256 = hashlib.sha256()

    with open(path, "rb") as file:
        for data in iter(lambda: file.read(4096), b""):
            sha256.update(data)

    return sha256.hexdigest()

baseline_file = file_path + ".sha256"

try:
    current_hash = calculate_hash(file_path)

    if not os.path.exists(baseline_file):
        with open(baseline_file, "w") as file:
            file.write(current_hash)

        print("\nBaseline created successfully!")

    else:
        with open(baseline_file, "r") as file:
            original_hash = file.read()

        if original_hash == current_hash:
            print("\nFile Status: SAFE")
            print("No changes detected.")
        else:
            print("\nWARNING: FILE MODIFIED!")
            print("Changes detected in the file.")

except FileNotFoundError:
    print("Error: File not found!")

print("\n===================================")