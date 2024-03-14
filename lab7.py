#Task 1
filename = "learning.txt"

# Method 1: Read in the entire file at once
print("Reading the entire file at once:")
with open(filename, 'r') as file:
    contents = file.readlines()
    for line in contents:
        print(f"In Python you can: {line}")

# Method 2: Loop over the file object
print("\nReading the file by looping over the file object:")
with open(filename, 'r') as file:
    for line in file:
        print(f"In Python you can: {line.rstrip()}")

# Method 3: Store the lines in a list and then work with them outside the with block
print("\nReading the file by storing lines in a list:")
with open(filename, 'r') as file:
    lines = file.readlines()

for line in lines:
    print(f"In Python you can: {line.rstrip()}")

#Task 2
filename = 'guest_book.txt'

while True:
    name = input("Please enter your name (enter 'quit' to exit): ")

    if name.lower() == 'quit':
        break

    print(f"Welcome, {name}!")

    with open(filename, 'a') as file:
        file.write(name + '\n')

print("Your visit has been recorded in the guest book.")

#Task 3
def word_count(file_name):
    lines = 0
    words = 0
    characters = 0

    with open(file_name, 'r') as file:
        for line in file:
            lines += 1
            words += len(line.split())
            characters += len(line)

    return lines, words, characters

def main():
    file_name = input("Enter the file name: ")

    try:
        lines, words, characters = word_count(file_name)
        print(f"Number of lines: {lines}")
        print(f"Number of words: {words}")
        print(f"Number of characters: {characters}")
    except FileNotFoundError:
        print("File not found. Please make sure the file exists and try again.")

if __name__ == "__main__":
    main()

