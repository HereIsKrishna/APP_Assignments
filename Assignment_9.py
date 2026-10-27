
import csv
import json

# Open the input CSV file in read mode
with open("assignment_9_input.csv", "r") as csv_file:

    # Read CSV data as dictionaries
    reader = csv.DictReader(csv_file)
    data = list(reader)

# Open the output JSON file in write mode
with open("assignment_9_output.json", "w") as json_file:

    # Convert data into JSON format and write it
    json.dump(data, json_file, indent=4)

# Display the success message
print("CSV data converted to JSON successfully.")
print("Output saved in assignment_9_output.json")
