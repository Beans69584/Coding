import os
cwd = "C:\\"
total_files = 0
for root, dirs, files in os.walk(cwd):
    for file in files:
        total_files += 1
print("Total number of files: ", total_files)