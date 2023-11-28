import os

def longest_common_substring(s1, s2):
    m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]
    longest, x_longest = 0, 0
    for x in range(1, 1 + len(s1)):
        for y in range(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0
    return s1[x_longest - longest: x_longest]


def find_best_matching_file(folder):
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        return "Folder not found."

    file_names = [os.path.splitext(file)[0] for file in files]
    
    # Use the longest common substring method
    folder = folder.split(sep="/")[4]
    folder = folder.lower()
    if folder in file_names:
        return folder
    best_match = max(file_names, key=lambda x: len(longest_common_substring((folder), x)), default="")

    return best_match if best_match else "No matching files found."




# Example usage
with open("directories.txt") as dirs:

    folders = [line.rstrip() for line in dirs]

    with open("sci_bin_all.txt","w") as result:
        for folder in folders:
            file = find_best_matching_file(folder)
            print("Best matching file:", file)
            print("Full Path:", folder + "/" + file)
            result.write(f"{folder}/{file}\n")
