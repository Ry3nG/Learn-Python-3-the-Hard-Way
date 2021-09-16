from sys import argv

scrpit, filename = argv

txt = open(filename) # open filename in default mode

print(f"Here's file {filename}")
print(txt.read())
txt.close()

print("Type the filename again:")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
