
# Open the input file in read mode
with open("assignment_8_input.txt", "r") as file:
    # Read all lines from the input file
    lines = file.readlines()

# Count and display the total number of lines
print("Total number of lines:", len(lines))

# Extract the first two lines
first_two_lines = lines[:2]

# Open the output file in write mode
with open("assignment_8_output.txt", "w") as file:
    # Write the first two lines into the output file
    file.writelines(first_two_lines)

# Display the extracted lines
print("First two lines:")
print("".join(first_two_lines))

print("Data saved to assignment8_output.txt")
