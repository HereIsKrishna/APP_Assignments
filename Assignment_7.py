
import re

# Accept text from the user
text = input("Enter text: ")

# Define a regex pattern to match email addresses
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Find all email addresses in the text
emails = re.findall(pattern, text)

# Display the email addresses found
if emails:
    print("Email addresses found:")
    for email in emails:
        print(email)
else:
    print("No email addresses found.")
