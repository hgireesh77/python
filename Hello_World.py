import sys

# Initialize a dictionary to store mapped incoming arguments
parsed_args = {}

# Loop through command-line arguments (skipping the script filename at index 0)
for arg in sys.argv[1:]:
    if "=" in arg:
        key, value = arg.split("=", 1)
        parsed_args[key] = value

# Safely extract the 'name' value with a fallback default
name = parsed_args.get("name", "No Name Received")

print(f"Hello World....{name}")
