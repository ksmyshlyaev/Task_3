import os

# Get all file names and store them in list
filenames = input('Please specify the file names separated with space (e.g. "file1.txt file2.txt"): ')
filenames = list(filenames.split(" "))

# Read all files with stored names and write their names and content to dict
files_content = {}
for filename in filenames:
    file_full_path = os.path.join("files", filename)
    try:
        f = open(file_full_path, "r")
        files_content[filename] = f.read()
    except FileNotFoundError:
        print(f'File with name "{filename}" does not exist')

# Iterate through files content and write to result list file names with firstly met content
temp = []
result = []
for key, val in files_content.items():
    if val not in temp:
        temp.append(val)
        result.append(key)

print(*result)

# Test data: file1.txt file2.txt file3.txt file4.txt file5.txt
