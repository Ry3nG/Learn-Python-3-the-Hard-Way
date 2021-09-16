from sys import argv

script, input_file = argv[0], argv[1] # unfold argv

def print_all(f):
    """[print all of the file contents.]

    Args:
        f ([file]): [the file to operate on]
    """
    print(f.read())

def rewind(f):
    """[put the cursor back to the beginning]

    Args:
        f ([file]): [the file to operate on]
    """
    f.seek(0)

def print_a_line(line_count, f):
    """[print a line of the file contents]

    Args:
        line_count ([integer]): [counts the lines of the file]
        f ([file]): [the file to operate on]
    """
    print(line_count, f.readline())

current_file = open(input_file) # open the file in default

print("Fist let's print the whole file.\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file) # put the cursor back to the beginning

print("Lets print three lines:")

# print the first three lines
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)


