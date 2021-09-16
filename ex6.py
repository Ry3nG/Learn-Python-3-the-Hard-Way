types_of_people = 10 # 10 is binary 2
x = f"There are {types_of_people} types of people." # store the print parameter

binary = "binary" # binary representation
do_not = "don't" # do_not = "don't"
y = f"Those who know {binary} and those who {do_not}." # store the other print parameter

print(x) # output of line 2
print(y) # output of line 3

print(f"I said: {x}") # add feature I said
print(f"I also said: {y}") # add feature I also said

hilarious = False # default: not hilarious
joke_evaluation = "Isn't that joke so funny?! {}" # store the print parameter

print(joke_evaluation.format(hilarious)) # use the format function to print hilarious

w = "This is the left side of..." # string
e = "a string with a right side..." # string

print(w + e) # add to strings to form a longer string
