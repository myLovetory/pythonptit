def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines


def laytuduynhat(lines):
    words = set()
    for line in lines:
        line = line.strip().lower()
        if line:
            words.update(line.split())
    return words


def sosanhfile(file1, file2):
    lines1 = read_file(file1)
    lines2 = read_file(file2)

    words1 = laytuduynhat(lines1)
    words2 = laytuduynhat(lines2)

    tufile1 = sorted(words1 - words2)
    tufile2 = sorted(words2 - words1)

    return tufile1, tufile2


# Đường dẫn tới các file input
f1 = 'DATA1.in'
f2 = 'DATA2.in'

# So sánh hai file và lấy kết quả
one, two = sosanhfile(f1, f2)

# In kết quả
print(' '.join(one))
print(' '.join(two))