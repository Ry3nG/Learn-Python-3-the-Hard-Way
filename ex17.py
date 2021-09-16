from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long.")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()


""" When writing to a file
    the data may not be written to disk until the file is closed.
    When you say "output.write(...)",
    the data is often cached in memory and doesn't hit the hard drive
    until the file is closed. The longer you keep the file open,
    the greater the chance that you will lose data.
"""
