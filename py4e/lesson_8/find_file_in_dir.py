import os

# folder path
dir_path = r'C:\\Users\\student\\Documents\\GitHub\\Computer-Science-Stuff\\py4e\\lesson_8\\'

# list to store files
res = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        res.append(path)
print(res)

# having this file path does not work. YOU NEED TO HAVE ONLY ONE BACKSLASH NOT TWO
fn = r'C:\\Users\\student\\Documents\\GitHub\\Computer-Science-Stuff\\py4e\\lesson_8\\file.txt\\'
# the reason why only one backslash works is because when you put the r in front of the path, it will automatically put two
    # backslashes when you run the code